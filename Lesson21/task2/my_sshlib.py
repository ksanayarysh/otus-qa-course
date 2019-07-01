import logging

import paramiko

str = 'listen=NO\n' \
      'listen_ipv6=YES\n' \
      'anonymous_enable=NO\n' \
      'local_enable=YES\n' \
      'write_enable=YES\n' \
      'local_umask=022\n' \
      'dirmessage_enable=YES\n' \
      'use_localtime=YES\n' \
      'xferlog_enable=YES\n' \
      'connect_from_port_20=YES\n' \
      'chroot_local_user=YES\n' \
      'secure_chroot_dir=/var/run/vsftpd/empty\n' \
      'pam_service_name=vsftpd\n' \
      'rsa_cert_file=/etc/ssl/certs/ssl-cert-snakeoil.pem\n' \
      'rsa_private_key_file=/etc/ssl/private/ssl-cert-snakeoil.key\n' \
      'ssl_enable=NO\n' \
      'pasv_enable=Yes\n' \
      'pasv_min_port=10000\n' \
      'pasv_max_port=10100\n' \
      'allow_writeable_chroot=YES\n'


class MySsh:
    secret = ""

    def __init__(self, user, secret, host, port):
        self.client = paramiko.SSHClient()
        self.secret = secret
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(hostname=host, username=user, password=secret, port=port)

        transport = paramiko.Transport((host, 22))
        transport.connect(username=user, password=secret)
        self.sftp = paramiko.SFTPClient.from_transport(transport)

    def exec_command_as_root(self, command):
        stdin, stdout, stderr = self.client.exec_command(command, get_pty=True)
        stdin.write(self.secret + "\n")
        stdin.flush()
        print(stdout.channel.recv_exit_status())

    def exec_command(self, command):
        stdin, stdout, stderr = self.client.exec_command(command, get_pty=True)
        print(stdout.channel.recv_exit_status())

    def write_file(self, str):
        f = self.sftp.open("/home/ksenia/Downloads/1.txt", "wb")
        f.write(str)
        f.close()

    def is_ftp_not_installed(self):
        stdin, stdout, stderr = self.client.exec_command("systemctl status vsftpd", get_pty=True)
        data = stdout.read()
        logging.info(data)
        return b"Unit vsftpd.service could not be found" in data

    def install_ftp(self):
        self.exec_command_as_root("sudo apt-get install vsftpd")
        self.exec_command_as_root("sudo systemctl start vsftpd")
        self.exec_command_as_root("sudo systemctl enable vsftpd")
        self.write_file(str)
        self.exec_command_as_root("sudo service vsftpd restart")

    def create_ftp_user(self, user, password):
        self.exec_command_as_root("sudo mkdir /var/ftp_home")
        self.exec_command_as_root("".join(["sudo useradd", user]))
        self.exec_command_as_root("".join(["sudo passwd", user]))
        self.exec_command(password)
        self.exec_command(password)
        self.exec_command_as_root("chown {0}:{1} /var/ftp_home".format(user, user))
        self.exec_command_as_root("usermod -d /var/ftp_home/ {0}".format(user))

    def if_user_exist(self, user):
        stdin, stdout, stderr = self.client.exec_command("cat /etc/passwd | grep {0}".format(user))
        return len(stdout.read()) > 0

    def delete_ftp_user(self, user):
        self.exec_command_as_root("".join(["sudo userdel", user]))


