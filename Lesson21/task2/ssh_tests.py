from Lesson21.task2.my_sshlib import MySsh


def test_install_vsftpd(creds):
    ssh = MySsh(creds[1], creds[2], creds[0], 22)
    if ssh.is_ftp_not_installed():
        ssh.install_ftp()
        assert not ssh.is_ftp_not_installed()


def test_create_user(creds):
    ssh = MySsh(creds[1], creds[2], creds[0], 22)
    if not ssh.if_user_exist("ftp_user"):
        ssh.create_ftp_user("ftp_user", "1111")
    assert ssh.if_user_exist("ftp_user")


def test_delete_user(creds):
    ssh = MySsh(creds[1], creds[2], creds[0], 22)
    if ssh.if_user_exist("ftp_user"):
        ssh.delete_ftp_user("ftp_user")
    assert not ssh.if_user_exist("ftp_user")