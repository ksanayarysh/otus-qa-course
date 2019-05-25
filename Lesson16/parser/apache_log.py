import json
import os
import re
import sys
from collections import Counter
from operator import itemgetter


class Log:
    """Class for parsing logs"""
    report = {}

    def __init__(self, file_name):
        """Inits with the log filename and reads file"""
        self.log_name = file_name
        try:
            with open(self.log_name) as f:
                self.log_file = f.read()
        except IOError:
            print(" ".join(["Can not find file", self.log_name]))
            sys.exit(1)

    def _set_report_value(self, key, value):
        """Adding value to a dictionary"""
        self.report[key] = value

    def all_requests(self):
        """Getting numbers of all requests"""
        regexp = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
        ips_list = re.findall(regexp, self.log_file)
        self._set_report_value("Number of all requests", len(ips_list))

    def request_by_type(self):
        """All requests by type"""
        regexp = r"GET|POST|PUT|DELETE"
        access_requests = re.findall(regexp, self.log_file)
        self._set_report_value("Requests by type", dict(Counter(access_requests)))

    def ten_top_ips(self):
        """IP of top ten requests"""
        regexp = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
        ips_list = re.findall(regexp, self.log_file)
        dict_ip_sorted_by_desc = map(lambda x: x[0], sorted(Counter(ips_list).items(), key=itemgetter(1),
                                                            reverse=True)[:10])
        self._set_report_value("Ten top ip", list(dict_ip_sorted_by_desc))

    def top_ten_longest_requests(self):
        regexp = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(.*)(POST|GET)(.*?)( 2\d\d )(\d*)(.*?)(http:.*?")'
        longest_logs = re.findall(regexp, self.log_file)
        longest_logs_info = list(map(lambda x: (x[2], x[7], x[0], x[5]), longest_logs))
        sorted_list = sorted(Counter(longest_logs_info).items(), key=itemgetter(1), reverse=True)[:10]
        self._set_report_value("Ten top massive requests", list(map(lambda x: x[0], sorted_list)))

    def ten_top_client_errors(self):
        """Info of top ten client errors (starting with 4)"""
        regexp = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(.*)(POST|GET)(.*?)( 4\d\d )(.*?)(http:.*?")'
        client_error_logs = re.findall(regexp, self.log_file)
        client_error_logs_info = list(map(lambda x: (x[0], x[2], x[4], x[6]), client_error_logs))
        sorted_list = sorted(Counter(client_error_logs_info).items(), key=itemgetter(1), reverse=True)[:10]
        self._set_report_value("Ten top client error", list(map(lambda x: x[0], sorted_list)))

    def ten_top_server_errors(self):
        """Top ten server errors (starting with 5)"""
        regexp = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(.*)(POST|GET)(.*?)( 5\d\d )(.*?)(http:.*?")'
        client_error_logs = re.findall(regexp, self.log_file)
        client_error_logs_info = list(map(lambda x: (x[0], x[2], x[4], x[6]), client_error_logs))
        sorted_list = sorted(Counter(client_error_logs_info).items(), key=itemgetter(1), reverse=True)[:10]
        self._set_report_value("Ten top server error", list(map(lambda x: x[0], sorted_list)))

    def save_to_json(self):
        """Save created report to json with the same name"""
        base_name = os.path.basename(self.log_name).split('.')[0]
        full_path = "\\".join([os.path.dirname(self.log_name), base_name])
        full_path = "".join([full_path, '.json'])
        with open(full_path, 'w') as json_file:
            json.dump(self.report, json_file)

    def analyze_all(self):
        self.all_requests()
        self.request_by_type()
        self.ten_top_ips()
        self.top_ten_longest_requests()
        self.ten_top_client_errors()
        self.ten_top_server_errors()
        self.save_to_json()
