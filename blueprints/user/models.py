from typing import Dict, Tuple


# Very simple database.
db: Dict[str, Tuple[str, str]] = {
    'igor': ('123456', 'mytoken'),
    'someone': ('superhardpass', 'superhardtoken')
}

class Repository():
    """Data managment class."""

    @staticmethod
    def is_valid(username: str, password: str) -> Tuple[bool, str]:
        """Validate the user and return its token."""
        user = db.get(username, None)

        if not user or user[0] != password:
            return False, ''

        return True, user[1]