from typing import Dict, Tuple


db: Dict[str, Tuple[str, str]] = {
    'igor': ('123456', 'mytoken')
}

class Repository():

    @staticmethod
    def is_valid(username: str, password: str) -> Tuple[bool, str]:
        user = db.get(username, None)

        if not user or user[0] != password:
            return False, ''

        return True, user[1]