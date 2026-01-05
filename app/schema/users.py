from pydantic import BaseModel

class UsersResponse(BaseModel):
    id: int
    username: str

    model_config = {
        "from_attributes": True
    }
