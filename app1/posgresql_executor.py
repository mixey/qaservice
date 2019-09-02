import sshtunnel
import psycopg2
import urllib2

SSH_HOST = "dev.magdv.com"
SSH_PORT = 42244
SSH_USERNAME = "m.tkachev"
SSH_PRIVATE_KEY_FILE = "OpenSsh"
SSH_PRIVATE_PASS_FILE = "ssh.password"

DB_NAME = "bmp"
DB_USERNAME = "bmp"
DB_PASSWORD = "bmp"


class PostgreSqlExec(object):

    def __init__(self, stand, port=SSH_PORT):
        response = urllib2.urlopen('http://172.21.19.58:82/api/bmp/db-port/%s' % stand)
        sql_port = int(response.read())
        password_file = open(SSH_PRIVATE_PASS_FILE, 'r')
        ssh_password = password_file.read()
        password_file.close()
        self.server = sshtunnel.SSHTunnelForwarder(
            (SSH_HOST, port),
            ssh_host_key=None,
            ssh_username=SSH_USERNAME,
            ssh_password=None,
            ssh_private_key=SSH_PRIVATE_KEY_FILE,
            ssh_private_key_password=ssh_password,
            remote_bind_address=("localhost", sql_port))

        self.server.start()

        self.cnx = psycopg2.connect(
            user=DB_USERNAME,
            password=DB_PASSWORD,
            host='127.0.0.1',
            port=self.server.local_bind_port,
            dbname=DB_NAME)

        self.cursor = self.cnx.cursor()

    def execute(self, command):
        try:
            if command.strip() != '':
                self.cursor.execute(command)
                return self.cursor.fetchall()
        except IOError, msg:
            print "Command skipped: ", msg
            raise msg

    def statement(self, value):
        sql_commands = value.split(';')
        for command in sql_commands:
            self.execute(command)

    def exec_file(self, filename):
        fd = open(filename, 'r')
        sql_file = fd.read()
        fd.close()
        self.statement(sql_file)

    def commit(self):
        self.cnx.commit()

    def close(self):
        self.cnx.close()
        self.server.stop()
