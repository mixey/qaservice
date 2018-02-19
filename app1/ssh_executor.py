import paramiko

SSH_HOST = "dev.magdv.com"
SSH_USERNAME = "m.tkachev"
SSH_PRIVATE_KEY_FILE = "OpenSsh"
SSH_PRIVATE_PASS_FILE = "ssh.password"

 
class SshExecutor(object):        

    def __init__(self, stand):
        with open(SSH_PRIVATE_PASS_FILE, 'r') as infile:
            private_key_password = infile.read()
    
        pkey = paramiko.RSAKey.from_private_key_file(SSH_PRIVATE_KEY_FILE, private_key_password)
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(hostname=SSH_HOST, port=42244, username=SSH_USERNAME, pkey=pkey)
                    
    def execute(self, command):  
        print "Executing {}".format(command)
        stdin , stdout, stderr = self.ssh.exec_command(command)
        print stdout.read()
        erros_mesg = stderr.read()
        if (erros_mesg):
            raise Exception(erros_mesg) 
    
    def close(self):
        self.ssh.close()
        
