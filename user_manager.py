# File: user_manager.py

from dahua import DahuaFunctions

class UserManager:
    def __init__(self, dahua_instance: DahuaFunctions):
        self.dahua = dahua_instance

    def add_user(self, username: str, password: str, role: str) -> bool:
        # Implementation for adding a user
        print(f"Adding user {username} with role {role}")
        # Example implementation:
        try:
            response = self.dahua.add_user(username, password, role)
            return response
        except Exception as e:
            print(f"Error adding user: {e}")
            return False

    def modify_password(self, username: str, new_password: str) -> bool:
        # Implementation for modifying user password
        print(f"Modifying password for user {username}")
        # Example implementation:
        try:
            response = self.dahua.modify_password(username, new_password)
            return response
        except Exception as e:
            print(f"Error modifying password: {e}")
            return False

    def delete_user(self, username: str) -> bool:
        # Implementation for deleting a user
        print(f"Deleting user {username}")
        # Example implementation:
        try:
            response = self.dahua.delete_user(username)
            return response
        except Exception as e:
            print(f"Error deleting user: {e}")
            return False
