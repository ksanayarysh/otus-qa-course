import pytest


@pytest.mark.usefixture("ssh")
class TestsSSH:
    def test_install_vsftpd(self, ssh):
        if ssh.is_ftp_not_installed():
            ssh.install_ftp()
            assert not ssh.is_ftp_not_installed()

    def test_create_user(self, ssh):
        if not ssh.if_user_exist("ftp_user"):
            ssh.create_ftp_user("ftp_user", "1111")
        assert ssh.if_user_exist("ftp_user")

    def test_delete_user(self, ssh):
        if ssh.if_user_exist("ftp_user"):
            ssh.delete_ftp_user("ftp_user")
        assert not ssh.if_user_exist("ftp_user")

    def test_change_port(self, ssh):
        ssh.set_ftp_port(2121)
        listen_str = ssh.get_ftp_port()
        assert listen_str == "listen_port=2121\n"

    def test_ftp_installed(self, ssh):
        assert not ssh.is_ftp_not_installed()
