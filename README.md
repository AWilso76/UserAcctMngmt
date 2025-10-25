# 🧑‍💻 User Account Management Automation Script

# Overview
This project automates **local user account management tasks on Windows systems** using Python. It simulates key responsibilities of an 
**IT Support Specialist / Applications Analyst**, such as creating, disabling, and removing user accounts while maintaining detailed logs for accountability.

# Features
- ✅ Create new local user accounts  
- ❌ Delete existing users  
- 🚫 Disable and 🔓 Enable accounts  
- 📜 List all local users  
- 🧾 Logs all actions to a file (`user_account_manager.log`)  

# Tools & Technologies
- **Language:** Python 3.x  
- **Modules:** `os`, `subprocess`, `logging`  
- **Platform:** Windows 10/11 (Run as Administrator)

# Relevance to IT Support / Applications Analyst Role
User lifecycle management is a core part of IT operations.  
This project demonstrates:
- Automation of repetitive onboarding/offboarding tasks  
- Basic permission and account control  
- Logging and auditing of administrative actions  

# Usage
1. Clone the repository  
2. Open an elevated PowerShell window  
3. Navigate to the project folder  
4. Run the script:
   ```bash
   python user_account_manager.py
5. Select an action from the menu (Create, Delete, Disable, Enable, List Users)

# Example Output

[2025-10-25 14:03:10] Created user: jdoe

[2025-10-25 14:05:42] Disabled user: ataylor

# Future Enhancements

Integrate with Active Directory for domain-wide management

Add bulk import/export via CSV

Include password reset and group management features

#Troubleshooting Note

Initial attempts to create users (awilso718 and awils) were unsuccessful due to insufficient permissions.
After running PyCharm as Administrator and granting system permissions, the script executed successfully on Windows 10.
This will be reflected in the "Logs" screenshot.

# Screenshots

## Create User

Created accounts: "jthur" and "awils", this screenshot showcases "awils" account creation.

<img width="1000" alt="image" src="https://i.imgur.com/kCkK1kP.png">

## List Users

User accounts awils, jthur and nduer displayed in screenshot below.

<img width="1000" alt="image" src="https://i.imgur.com/HgqCiz7.png">

## Disable Users

The user "awils" was disabled in screenshot below.

<img width="1000" alt="image" src="https://i.imgur.com/h9ApaXp.png">

## Enable Users

Enabled "awils" user account in screenshot below.

<img width="1000" alt="image" src="https://i.imgur.com/HWvhiUe.png">

## Delete Users

Deleted user "jthur" in screeshot below.

<img width="1000" alt="image" src="https://i.imgur.com/5JWFsYg.png">

## List Users post account deletion

Listed all user accounts after removing user "jthur".

<img width="1000" alt="image" src="https://i.imgur.com/atFecnv.png">

## Logs example

Initial attempts to create users (awilso718 and awils) were unsuccessful. After running PyCharm as Administrator and granting system permissions,
the script executed successfully on Windows 10

<img width="1000" alt="image" src="https://i.imgur.com/Hj13etH.png">

# License

## MIT License – for educational and professional portfolio use.



