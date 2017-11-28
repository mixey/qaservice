import sshtunnel
import mysql.connector
import urllib2


class SqlExec(object):
        
    def __init__(self, stand):
        response = urllib2.urlopen('http://{}.dev.magonline.ru/sql.html'.format(stand))
        sql_port = int(response.read())
        
        self.server = sshtunnel.SSHTunnelForwarder(
            ("dev.magdv.com", 42244),
            ssh_host_key=None,
            ssh_username="m.tkachev",
            ssh_password=None,
            ssh_private_key="d:\DISTR\TOOLS\keys\OpenSsh",
            ssh_private_key_password="ow4cDhjwe",
            remote_bind_address=("localhost", sql_port))
        
        self.server.start()
        
        self.cnx = mysql.connector.connect(
            user='root',
            password='online',
            host='127.0.0.1',
            port=self.server.local_bind_port,
            database='magonline')
        
        self.cursor = self.cnx.cursor()
            
    def execute(self, command):  
        try:
            if command.strip() != '':
                self.cursor.execute(command)
        except IOError, msg:
            print "Command skipped: ", msg
            raise msg

    def statement(self, value):
        sql_commands = value.split(';')
        for command in sql_commands:
            self.execute(command)
            
    def exec_file(self, filename):
        fd = open(filename, 'r')
        sqlFile = fd.read()
        fd.close()
        self.statement(sqlFile)            

    def commit(self):
        self.cnx.commit()
        
    def close(self):        
        self.cnx.close()
        self.server.stop()
