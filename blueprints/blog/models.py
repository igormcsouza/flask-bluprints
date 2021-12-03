from typing import Any, Dict, List


class ValidationError(Exception):
    """Exception class to raise Validation Errors."""
    pass


# Models Definitions 
class Post:
    """Post model and validation."""

    def __init__(self, title: str, body: str, liked: bool):

        self.title = self.valid_title(title)
        self.body = body
        self.liked = liked

    @staticmethod
    def valid_title(title: str) -> str:
        """Validate the title."""
        try:
            assert len(title) > 15
        except AssertionError:
            raise ValidationError("Title is too short.")
        finally:
            return title

    def to_dict(self) -> Dict[str, Any]:
        """Prepare data to be jsonified."""
        return {
            "title": self.title,
            "body": self.body,
            "liked": self.liked
        }

# Connection with DB
db = [
    Post("Homero with at least 15 characters.", "Era um grande cara", True)
]

# Repositories
class Repository:
    """Data management class."""

    @staticmethod
    def store(post: Post):
        """Put the new post on the database."""
        db.append(post)

    @staticmethod
    def get_all() -> List[Dict[str, Any]]:
        """Retrieve the information present on db."""
        return [instance.to_dict() for instance in db]