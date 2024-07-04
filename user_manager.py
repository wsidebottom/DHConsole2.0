# File: user_manager.py

from dahua import DahuaFunctions
from utils import log
from pwdmanager import dahua_gen2_md5_hash

class UserManager:
    def __init__(self, dahua_instance: DahuaFunctions):
        self.dahua = dahua_instance

    def add_user(self, username: str, password: str, role: str) -> bool:
        # Log the operation
        print(f"Adding user {username} with role {role}")

        if not self.dahua.dh_realm:
            log.failure(f'[add_user] no realm exist ({self.dahua.dh_realm})')
            return False

        query_args = {
            'method': 'userManager.getAuthorityList',
            'params': None,
        }
        dh_data = self.dahua.send_call(query_args, error_codes=True)
        authority_list = dh_data.get('params')

        dh_hash = dahua_gen2_md5_hash(
            dh_realm=self.dahua.dh_realm, username=username, password=password, return_hash=True
        )

        query_args = {
            'method': 'userManager.addUser',
            'params': {
                'user': {
                    'AuthorityList': authority_list,
                    'Group': role,
                    'Memo': username,
                    'Name': username,
                    'Password': dh_hash,
                },
            },
        }
        dh_data = self.dahua.send_call(query_args, error_codes=True)
        if dh_data.get('result'):
            log.success('Success')
            return True
        else:
            log.failure('Failed: User already exist?')
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
