# 🔐 Remote Access & Automation of Cisco Router on EVE-NG using Netmiko

This project demonstrates how to enable SSH-based remote access to a Cisco router hosted on EVE-NG and use **Netmiko** (a Python SSH library) to automate network tasks.

---

## 🛠️ Project Overview

In this setup:
- A **Cisco IOSv router** is running in EVE-NG.
- The **host machine** is configured to remotely access the router via **SSH**.
- **Netmiko** is used to automate interactions like entering privileged mode and sending commands.

---

## 📦 Requirements

- Python 3.x
- EVE-NG (running Cisco IOSv router)
- Netmiko: `pip install netmiko`
- Proper interface bridging between EVE-NG and host machine

---

## 🧪 Lab Setup

1. **On the Cisco Router (in EVE-NG):**
   ```bash
   conf t
   hostname Router1
   interface GigabitEthernet0/0
     ip address 192.168.44.129 255.255.255.0
     no shutdown
   exit
   ip domain-name local
   crypto key generate rsa
   username admin privilege 15 secret admin
   line vty 0 4
     transport input ssh
     login local
     privilege level 15
   exit
   enable secret admin
