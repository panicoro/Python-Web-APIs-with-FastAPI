from pydantic import BaseModel
from beanie import Document
from typing import List, Optional

class Event(Document):
  title: str
  image: str
  description: str
  tags: List[str]
  location: str
  
  class Config:
    json_schema_extra = {
      "example": {
        "title": "FastAPI Book Launch",
        "image": "https://linktomyimage.com/image.png",
        "description": "We will be discussing the contents of the FastAPI book in this event. Ensure to come with your own copy to win gifts!",
        "tags": ["python", "fastapi", "book", "launch"],
        "location": "Google Meet"
      }
    }
  
  class Settings:
    name = "events"

class EventUpdate(BaseModel):
  title: Optional[str] = None
  image: Optional[str] = None
  description: Optional[str] = None
  tags: Optional[List[str]] = []
  location: str = None
  
  class Config:
    json_schema_extra = {
      "example": {
        "title": "FastAPI Book Launch",
        "image": "https://linktomyimage.com/image.png",
        "description": "We will be discussing the contents of the FastAPI book in this event. Ensure to come with your own copy to win gifts!",
        "tags": ["python", "fastapi", "book", "launch"],
        "location": "Google Meet"
      }
    }