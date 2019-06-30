import logging
import re
import subprocess

logging.basicConfig(level=logging.INFO)


def test_if():
    pat_lo = re.compile(b"lo:.*\\n *inet (\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3})", re.MULTILINE)
    pat_en = re.compile(b"en.*:.*\\n *inet (\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3})", re.MULTILINE)
    pat_wl = re.compile(b"wl.*:.*\\n *inet (\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3})", re.MULTILINE)
    resp = subprocess.check_output(["ifconfig"])

    lo_ip = pat_lo.findall(resp)[0].decode()
    wl_ip = pat_wl.findall(resp)[0].decode()

    logging.info(lo_ip)
    logging.info(wl_ip)

    assert lo_ip == "127.0.0.1"
    assert wl_ip == "192.168.0.2"


def test_check_default_route():
    p1 = subprocess.Popen(['ip', 'r'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    p2 = subprocess.Popen(["grep", "default"], stdin=p1.stdout, stdout=subprocess.PIPE)
    line = p2.stdout.readline()
    pat = re.compile(b"default via (\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3})")
    ip = re.match(pat, line)
    default_route = ip.group(1).decode()
    logging.info(default_route)
    assert "192.168.0.1" == default_route


def test_processor_info():
    print(subprocess.check_output("lscpu").decode())


def test_all_process_info():
    print(subprocess.check_output(["ps", "aux"]).decode())


def test_if_stat():
    print(subprocess.check_output(["tail",  "/proc/net/dev"]).decode())


def test_service_stat():
    resp = subprocess.check_output(["systemctl",  "status", "apache2.service"]).decode()
    pat = re.compile(r"Active: (\w*)", re.MULTILINE)
    status = pat.findall(resp)[0]
    logging.info(status)
    assert status == "active"


def test_cur_dir():
    resp = subprocess.check_output(["pwd"]).decode()
    print(resp)


def test_cernel_version():
    resp = subprocess.check_output(["uname", "-r"]).decode()
    print(resp)


def test_os_version():
    resp = subprocess.check_output(["cat", "/proc/version"]).decode()
    print(resp)

