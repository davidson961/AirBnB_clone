from models.base_model import BaseModel

class Review(BaseModel):
    """
    Review class that inherits from BaseModel.

    Public class attributes:
        place_id (str): Place ID (initialized as an empty string, linked to Place.id).
        user_id (str): User ID (initialized as an empty string, linked to User.id).
        text (str): Review text (initialized as an empty string).
    """
    def __init__(self, *args, **kwargs):
        """Initialize Review instance."""
        super().__init__(*args, **kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""
