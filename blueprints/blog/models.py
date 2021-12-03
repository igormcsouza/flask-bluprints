from typing import Any, Dict, List


class ValidationError(Exception):
    pass


# Models Definitions 
class Post:

    def __init__(self, title: str, body: str, liked: bool):
        try:
            assert len(title) > 30
        except AssertionError:
            raise ValidationError("Title is too short.")
        finally:
            self.title = title

        self.body = body
        self.liked = liked

    def to_dict(self) -> Dict[str, Any]:
        return {
            "title": self.title,
            "body": self.body,
            "liked": self.liked
        }

# Connection with DB
db = [
    Post("Homero jajajajjajajajajjajajajajaj", "Era um grande cara", True)
]

# Repositories
class Repository:

    @staticmethod
    def store(post: Post):
        db.append(post)

    @staticmethod
    def get_all() -> List[Dict[str, Any]]:
        return [instance.to_dict() for instance in db]