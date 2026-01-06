from pydantic import BaseModel, Field

class TicketsSearchRequest(BaseModel):
    title_query: str = Field(..., description="Search string for tickets")
    limit: int = Field(10, ge=1, le=50)
    offset: int = Field(0, ge=0)