from netmiko import ConnectHandler

cisco_device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.44.129',
    'username': 'admin',
    'password': 'admin',
    'secret': 'admin',  # This is the enable password
}

# Establish SSH connection
connection = ConnectHandler(**cisco_device)

# Enter enable mode
connection.enable()

# Run privileged command
output = connection.send_command('show running-config')
print(output)

# Disconnect
connection.disconnect()
