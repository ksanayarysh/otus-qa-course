import configparser
import paramiko
import requests

config = configparser.ConfigParser()
config.read('creds.ini')
secret = config['opencart']['secret']
user = config['opencart']['user']
host = config['opencart']['host']
port = config['opencart']['port']

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=host, username=user, password=secret, port=port)

stdin, stdout, stderr = client.exec_command('sudo systemctl stop apache2.service', get_pty=True)
stdin.write("1111" + "\n")
stdin.flush()
stdin, stdout, stderr = client.exec_command('sudo systemctl start apache2.service', get_pty=True)
stdin.write("1111" + "\n")
stdin.flush()
print(stdout.channel.recv_exit_status())

stdin, stdout, stderr = client.exec_command('sudo systemctl stop mysql.service', get_pty=True)
stdin.write("1111" + "\n")
stdin.flush()
stdin, stdout, stderr = client.exec_command('sudo systemctl start mysql.service', get_pty=True)
stdin.write("1111" + "\n")
stdin.flush()
print(stdout.channel.recv_exit_status())

r = requests.get("/".join(["http:/", host, "opencart"]))
assert r.status_code == 200

client.close()

