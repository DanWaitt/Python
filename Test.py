# Creating a list

devices = ["router01", "router02", "router03", "switch01", "switch02", "switch03", "switch04", "firewall01", "firewall02"]
print(devices[0])
print(devices[-1])
print(devices[1:6])

# Adding to list

devices.append("switch06")
print(devices)
devices.insert(4, "switch07")
print(devices)

# Removing items from list

devices.remove("switch07")
print(devices)
popped = devices.pop()
print(popped)

# Sorting

devices.sort()
print(devices)
devices.sort(reverse=True)
print(devices)
sorted_copy = sorted(devices)
print(sorted_copy)
print(devices)

# Aliasing

devices = ["router01", "switch01", "firewall01"]
a = devices
a.append("router02")
print(a)
print(devices)

# Copy

b = devices.copy()
b.append("router02")
print(b)
print(devices)

# Joining Lists

devices = ["router01", "switch01", "firewall01"]
more_devices = ["router02", "switch02", "firewall02"]

# Method 1:

combined = devices + more_devices
print("Combined:" combined)

# Tuples

snapshot = ("router01", 80, 512 "online")
print(snapshot)

#creating a tuple

t1 = 1, 2, 3
t2 = (1, 2, 3)
print(t1, t2)

#single-item tuples

one_tuple = (42,) #tuple
not_tuple = (42) #just a number not a tuple

# built-in tuple

devices_list = ["router01", "switch01", "firewall01"]
devices_tuple = tuple(devices_list)
print(devices_tuple)

# Change a Tuple

metrics = ("router1", 8080, "Online")
# Step 1 make it a list
tuple = list(metrics)
# Step 2 make the change
tuple[1] = 90
# Step 3 make a tuple again
metrics = tuple(tuple)
print(metrics)

# Unpacking

network_device = ("router01", 192.168.1.1, "online")
name, ip, status = network_device
print(name)
print(ip)
print(status)

# Loop Unpacking

pairs = [("router1", "192.168.1.2"), ("router2", "192.168.1.3")]

for name, ip in pairs:
    print(name, ip)

 t = ("router1", "192.168.1.2", "255.255.255.0")


# Dictionaries

devices = [ # List of Dictionaries
    {"device_type": "cisco_ios", "ip": "192.168.1.1", "username": "admin1"},
    {"device_type": "cisco_ios", "ip": "192.168.1.2", "username": "admin2"}]
print(devices[0]["username"])
print(devices[1]["ip"])


# Sets

devices1 = {"router01", "switch01", "switch01", "router01", "router02", "switch02"}
print(devices1)

devices1.add("firewall01")
devices1.update(["gateway01", "proxy01"])
print(devices1)

devices1.remove("proxy01")
devices1.discard("gateway02")

if "router01" in devices1:
    devices1.remove("router01")
    print("Router01 removed from devices set!")

# Files
# Read
with open("test.txt", "r") as file:
    print(file.read())

# Write
with open("test.txt", "w") as file:
    file.write("File edited\n")

# Exculsive
with open("test.txt", "x") as file:
    file.write("Backup created successfully\n")

## Old Way to Open file
file = open("test.txt", "a")
file.write("System Started\n")
file.close()

## Better Way to open file
with open("test.txt", "a") as file:
    file.write("System Started\n")

## Writing in a file
with open("test.txt", "a") as file:
    file.write("First Line\n")
    file.write("Second Line\n")

## Reading Files
# Using .read()
with open("test.txt", "r") as file:
    content = file.read()
    print(content)

# Using .readlines()
with open("test.txt", "r") as file:
    lines = file.readlines()
    print(lines)

# Strips out the new line
for line in lines:
    print(line.strip())

# Loop directly
with open("test.txt", "r") as file:
    for line in file:
        print(line.strip())

# Check if file exist
import os
if os.path.exists("test.txt"):
    with open("test.txt", "r") as file:
        for line in file:
            print(line.strip())
else:
    print("File not found")

# CSV files
# using split
with open("test.csv", "r") as file:
    for line in file:
      print(line.strip().split(","))

using import
import csv
with open("test.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"Device: {row['Device Name']}, | Location: {row['Location']}, | Status: {row['Status']}")

# Writing to CSV
with open("test.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["IP", "DOS", "DOR"])
    writer.writeheader()
    writer.writerow({"IP": "192.168.127.12", "DOS": "12/20", "DOR": "12/25"})

Appending CSV
with open("test.csv", "a", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["IP", "DOS", "DOR"])
    writer.writeheader()
    writer.writerow({"IP": "192.168.127.12", "DOS": "12/20", "DOR": "12/25"})

# Exclusive CSV
with open("test.csv", "x", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["IP", "DOS", "DOR"])
    writer.writeheader()
    writer.writerow({"IP": "192.168.127.12", "DOS": "12/20", "DOR": "12/25"})

