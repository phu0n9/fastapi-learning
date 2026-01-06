from pydantic import BaseModel, Field

class UsersResponse(BaseModel):
    id: int
    username: str

    model_config = {
        "from_attributes": True
    }

class UserSearchRequest(BaseModel):
    query: str = Field(..., description="Search string for username")
    limit: int = Field(10, ge=1, le=50)
    offset: int = Field(0, ge=0)

class DeleteUserResponse(BaseModel):
    is_deleted: bool