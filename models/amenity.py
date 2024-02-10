from models.base_model import BaseModel

class Amenity(BaseModel):
    """
    Amenity class that inherits from BaseModel.

    Public class attributes:
        name (str): Amenity name (initialized as an empty string).
    """
    def __init__(self, *args, **kwargs):
        """Initialize Amenity instance."""
        super().__init__(*args, **kwargs)
        self.name = ""
