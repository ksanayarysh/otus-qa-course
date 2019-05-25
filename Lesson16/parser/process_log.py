"""Parse logs"""
import argparse
import os

from Lesson16.parser.apache_log import Log


def create_parser():
    """Using command line options"""
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--dir', default="",
                        help="Use to specify the path to log file or dir, if dir then all log files will be parsed")

    return parser


if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args()
    apache_log = ""
    if os.path.exists(namespace.dir):
        if os.path.isfile(namespace.dir):
            apache_log = Log(namespace.dir)
        elif os.path.isdir(namespace.dir):
            files = os.listdir(namespace.dir)
            for file in files:
                if os.path.splitext(os.path.basename(file))[1] == '.log':
                    apache_log = Log("".join([namespace.dir, file]))
        if apache_log:
            apache_log.analyze_all()
    else:
        print("not found")

