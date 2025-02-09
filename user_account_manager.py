import os
import subprocess
import logging

# Configure logging
logging.basicConfig(
    filename="user_account_manager.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def create_user(username, password):
    """Create a new local user with the specified username and password."""
    try:
        subprocess.run(f'net user {username} {password} /add', check=True, shell=True)
        print(f"User '{username}' created successfully.")
        logging.info(f"User '{username}' created successfully.")
    except subprocess.CalledProcessError:
        print(f"Failed to create user '{username}'.")
        logging.error(f"Failed to create user '{username}'.")


def delete_user(username):
    """Delete an existing local user."""
    try:
        subprocess.run(f'net user {username} /delete', check=True, shell=True)
        print(f"User '{username}' deleted successfully.")
        logging.info(f"User '{username}' deleted successfully.")
    except subprocess.CalledProcessError:
        print(f"Failed to delete user '{username}'.")
        logging.error(f"Failed to delete user '{username}'.")


def list_users():
    """List all local user accounts."""
    try:
        print("Listing all local user accounts:")
        subprocess.run('net user', check=True, shell=True)
        logging.info("Listed all local user accounts.")
    except subprocess.CalledProcessError:
        print("Failed to list users.")
        logging.error("Failed to list users.")


def disable_user(username):
    """Disable a local user account."""
    try:
        subprocess.run(f'net user {username} /active:no', check=True, shell=True)
        print(f"User '{username}' disabled successfully.")
        logging.info(f"User '{username}' disabled successfully.")
    except subprocess.CalledProcessError:
        print(f"Failed to disable user '{username}'.")
        logging.error(f"Failed to disable user '{username}'.")


def enable_user(username):
    """Enable a local user account."""
    try:
        subprocess.run(f'net user {username} /active:yes', check=True, shell=True)
        print(f"User '{username}' enabled successfully.")
        logging.info(f"User '{username}' enabled successfully.")
    except subprocess.CalledProcessError:
        print(f"Failed to enable user '{username}'.")
        logging.error(f"Failed to enable user '{username}'.")


if __name__ == "__main__":
    print("User Account Management Script")
    print("1. Create User")
    print("2. Delete User")
    print("3. List Users")
    print("4. Disable User")
    print("5. Enable User")

    choice = input("Enter your choice: ")
    if choice == "1":
        username = input("Enter the username: ")
        password = input("Enter the password: ")
        create_user(username, password)
    elif choice == "2":
        username = input("Enter the username to delete: ")
        delete_user(username)
    elif choice == "3":
        list_users()
    elif choice == "4":
        username = input("Enter the username to disable: ")
        disable_user(username)
    elif choice == "5":
        username = input("Enter the username to enable: ")
        enable_user(username)
    else:
        print("Invalid choice.")
        logging.warning("Invalid choice entered in the menu.")
