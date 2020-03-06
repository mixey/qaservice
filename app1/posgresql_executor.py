import psycopg2
import urllib2
import re

DB_HOST = '10.2.3.1'  # stand.bmp.magdv
DB_NAME = "bmp"
DB_USERNAME = "bmp"
DB_PASSWORD = "bmp"


class PostgreSqlExec(object):

    def __init__(self, stand):
        response = re.search('data.+?(\d+)',
                             urllib2.urlopen('http://127.0.0.1:8080/api/db-port/%s' % stand).read()).group(1)
        db_port = int(response)
        self.cnx = psycopg2.connect(
            user=DB_USERNAME,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=db_port,
            dbname=DB_NAME)

        self.cursor = self.cnx.cursor()

    def execute_fetch(self, command):
        try:
            self.execute(command)
            return self.cursor.fetchall()
        except IOError, msg:
            print "Command skipped: ", msg
            raise msg

    def execute(self, command):
        try:
            if command.strip() != '':
                self.cursor.execute(command)
        except IOError, msg:
            print "Command skipped: ", msg
            raise msg

    def execute_batch(self, value):
        sql_commands = value.split(';')
        for command in sql_commands:
            self.execute(command)

    def statement(self, value):
        sql_commands = value.split(';')
        for command in sql_commands:
            self.execute_fetch(command)

    def exec_file(self, filename):
        fd = open(filename, 'r')
        sql_file = fd.read()
        fd.close()
        self.statement(sql_file)

    def render_template(self, filename, args):
        fd = open(filename, 'r')
        template = fd.read()
        fd.close()
        for key in args.keys():
            template = template.replace("{{ " + key + " }}", args.get(key))
        return template

    def commit(self):
        self.cnx.commit()

    def close(self):
        self.cnx.close()
