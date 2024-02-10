from models.base_model import BaseModel

class State(BaseModel):
    """
    State class that inherits from BaseModel.

    Public class attributes:
        name (str): State name (initialized as an empty string).
    """
    def __init__(self, *args, **kwargs):
        """Initialize State instance."""
        super().__init__(*args, **kwargs)
        self.name = ""
