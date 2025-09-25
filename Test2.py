# Functions From D522 OA

def search_number_in_list(number, number_list):
    return number in number_list

# Example:
numbers = [122345, 123456, 987654, 789654]
print(search_number_in_list(123456, numbers))
# Output: True

#print(search_number_in_list(111111, numbers))
# Output: False

def eur_to_usd(eur):
    usd = eur * 1.08
    return f"{usd:.2f} USD"

# Example:
print(eur_to_usd(3.53))
# Output: '3.81 USD'

def tuple_to_dict(network_tuple):
    return dict(network_tuple)

# Example:
network_tuple = (("ip", "192.168.1.1"), ("subnet", "255.255.255.0"), ("gateway", "192.168.1.254"))
print(tuple_to_dict(network_tuple))
# Output: {'ip': '192.168.1.1', 'subnet': '255.255.255.0', 'gateway': '192.168.1.254'}
#
def get_network_devices(device_list):
    return [device for device in device_list if device.startswith("network_device")]

# Example:
device_list = ["network_device1", "network_device2", "network_device3", "coffee_maker", "printer_copier"]
print(get_network_devices(device_list))
# # Output: ['network_device1', 'network_device2', 'network_device3']

def cpu_usage(cpu_list):
    return [i for i, v in enumerate(cpu_list) if v >90.0]

cpu_list = [85.6, 99.2, 74.5, 91.2, 90.1, 62.5, 55.8, 46.7, 37.3, 23.4, 88.5, 81.2]
print(cpu_usage(cpu_list))

# Date Time
from datetime import datetime
def find_latest(submissions):
    date_format = '%m/%d/%Y %I:%M %p'
    # ADDED LINES BELOW
    datetime_objects = [datetime.strptime(s, date_format) for s in submissions]
    return max(datetime_objects)
timestamps_1 = ['12/15/2023 08:45 AM', '12/14/2023 03:30 PM', '12/16/2023 11:20 AM', '12/13/2023 06:15 PM']
print(find_latest(timestamps_1))

# Log Search
def update_log_list(log_list):
    for log in log_list:
        if log.get("app") == "webserver":
            log["level"] = "ERROR"
        if log.get("app") == "database":
            log["timestamp"] = "2023-12-07T12:30:00"
    return log_list


log_sample = [
    {"app": "webserver", "level": "ERROR", "message": "Critical error", "timestamp": "2023-12-07T11:55:00"},
    {"app": "database", "level": "ERROR", "message": "Database connection lost", "timestamp": "2023-12-07T11:50:00"}]
print(update_log_list(log_sample))

# Emp id search
def validate_id(emp_id):
    return len(emp_id) == 8 and emp_id[:3].isupper()

print(validate_id("HRD00123"))
print(validate_id("Ops123456"))
print(validate_id("ENG00123"))
print(validate_id("Pot100123"))

# Subnet check
def same_subnet(ip1, ip2, subnet_mask):
    # convert IP addresses to binary strings
    ip1_bin = ''.join([format(int(x), '08b') for x in ip1.split('.')])
    ip2_bin = ''.join([format(int(x), '08b') for x in ip2.split('.')])
    subnet_bin = ''.join([format(int(x), '08b') for x in subnet_mask.split('.')])
    subnet_len = subnet_bin.count('1')
    network1_bin = ip1_bin[:subnet_len]
    network2_bin = ip2_bin[:subnet_len]
    x = f"{ip1} and {ip2} are in the same subnet"
    y = f"{ip1} and {ip2} are not in the same subnet"

    return x if network1_bin == network2_bin else y  # ADDED THIS LINE ONLY!!!!!

print(same_subnet('192.168.1.100', '192.168.1.200', '255.255.255.0'))

# Line count
def line_count(filename):
    f = open(filename) # CHANGED Open TO open !!!!!
    contents = f.read() # ADDED () AFTER read !!!!!
    lines = contents.split("\n")
    f.close()
    return len(lines) # CHANGED line TO lines !!!!

print(line_count('test.txt'))

# Write to CSV
# import csv
# import os
#
# def write_dict_to_csv(filename):
#
#     fieldnames = ['device_name', 'ip_address']
#
#     data = [
#         {'device_name': 'Router1', 'ip_address': '192.168.1.1'},
#         {'device_name': 'Router2', 'ip_address': '192.168.1.2'}
#     ]
#     file_is_empty = not os.path.exists(filename) or os.path.getsize(filename) == 0
#
#     # ADDED LINES BELOW:
#     with open(filename, 'a', newline='') as file:
#         csv.DictWriter(file, fieldnames=fieldnames).writeheader()
#         csv.DictWriter(file, fieldnames=fieldnames).writerows(data)
#
#     print('\n'.join([','.join(fieldnames)] + [','.join(str(d[field]) for field in fieldnames) for d in data]))
#
# write_dict_to_csv('config.csv')
#
#
# import socket
# import time
# import unittest.mock as mock
#
# def scan_ports(x):
#     # Mock socket
#     with mock.patch('socket.socket') as mock_socket:
#         mock_socket.return_value.connect_ex.return_value = 0  # do not edit
#         target_IP = '127.0.0.1'
#         # Instantiate a socket object.
#         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         # Set a timeout for the socket operations.
#         s.settimeout(5)
#         # Create an empty list to store port status as a list tuples.
#         open_ports = []
#
#         for i in range(0, x + 1):
#             conn = s.connect_ex((target_IP, i))
#             if (conn == 0):
#                 open_ports.append((i, 'OPEN'))  # Changed extend to append, and ((i, 'OPEN'))
#             else:
#                 open_ports.append((i, 'CLOSED'))  # Changed extend to append, and ((i, 'ClOSED'))
#         s.close()
#         return open_ports
#
# print(scan_ports(5))
# help(socket.socket)
# help(socket.socket.connect_ex)
#print(dir(time))
#print(dir(socket))