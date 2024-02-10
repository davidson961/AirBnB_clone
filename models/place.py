from models.base_model import BaseModel

class Place(BaseModel):
    """
    Place class that inherits from BaseModel.

    Public class attributes:
        city_id (str): City ID (initialized as an empty string, linked to City.id).
        user_id (str): User ID (initialized as an empty string, linked to User.id).
        name (str): Place name (initialized as an empty string).
        description (str): Place description (initialized as an empty string).
        number_rooms (int): Number of rooms (initialized as 0).
        number_bathrooms (int): Number of bathrooms (initialized as 0).
        max_guest (int): Maximum number of guests (initialized as 0).
        price_by_night (int): Price per night (initialized as 0).
        latitude (float): Latitude (initialized as 0.0).
        longitude (float): Longitude (initialized as 0.0).
        amenity_ids (list): List of Amenity IDs (initialized as an empty list).
    """
    def __init__(self, *args, **kwargs):
        """Initialize Place instance."""
        super().__init__(*args, **kwargs)
        self.city_id = ""
        self.user_id = ""
        self.name = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = []
