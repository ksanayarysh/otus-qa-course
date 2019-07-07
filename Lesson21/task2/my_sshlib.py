import logging

import paramiko

SERVICE_FILENAME = "vsftpd.conf"

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

    def close(self):
        self.client.close()

    def exec_command_as_root(self, command):
        stdin, stdout, stderr = self.client.exec_command(command, get_pty=True)
        stdin.write(self.secret + "\n")
        stdin.flush()
        logging.info("{0} - {1}".format(command, stdout.channel.recv_exit_status()))

    def exec_command(self, command):
        stdin, stdout, stderr = self.client.exec_command(command, get_pty=True)
        logging.info("{0} - {1}".format(command, stdout.channel.recv_exit_status()))

    def write_file(self, str):
        f = self.sftp.open("/home/ksenia/vsftpd.conf", "wb")
        f.write(str)
        f.close()

    def is_ftp_not_installed(self):
        command = "dpkg -s vsftpd  | grep \"install ok installed\""
        stdin, stdout, stderr = self.client.exec_command(command, get_pty=True)
        data = stdout.read()
        logging.info(data.decode())
        return len(data) == 0

    def install_ftp(self):
        self.exec_command_as_root("sudo apt-get install vsftpd")
        self.exec_command_as_root("sudo systemctl start vsftpd")
        self.exec_command_as_root("sudo systemctl enable vsftpd")
        self.write_file(str)
        self.copy_config_file()
        self.restart_ftp()

    def restart_ftp(self):
        self.exec_command_as_root("sudo systemctl restart vsftpd ")

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

    def copy_config_file(self):
        self.exec_command_as_root("sudo rm /etc/vsftpd.conf")
        self.exec_command_as_root("sudo cp /home/ksenia/vsftpd.conf /etc/vsftpd.conf")

    def get_ftp_port(self):
        stdin, stdout, stderr = self.client.exec_command('cat {0} | grep listen_port '.format(SERVICE_FILENAME))
        data = stdout.read().decode()
        print(data)
        return data

    def add_listen_port(self, port):
        self.exec_command_as_root("sudo echo listen_port={0} >> {1}".format(port, SERVICE_FILENAME))

    def change_ftp_port(self, port):
        self.exec_command_as_root(
            "sudo sed -i 's/.*listen_port=.*/listen_port={0}/' {1}".format(port, SERVICE_FILENAME))

    def set_ftp_port(self, port):
        """ Check if port is specified
        if it is, we change string listen_port=
        if not,  we add string listen_port=
        then we reaload service """
        listen_port = self.get_ftp_port()
        logging.info(listen_port)
        if not listen_port:
            self.add_listen_port(port)
        else:
            self.change_ftp_port(port)
        self.copy_config_file()
        self.restart_ftp()


