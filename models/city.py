from models.base_model import BaseModel

class City(BaseModel):
    """
    City class that inherits from BaseModel.

    Public class attributes:
        state_id (str): State ID (initialized as an empty string, linked to State.id).
        name (str): City name (initialized as an empty string).
    """
    def __init__(self, *args, **kwargs):
        """Initialize City instance."""
        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""
