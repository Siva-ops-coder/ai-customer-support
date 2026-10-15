from pydantic import BaseModel, Field

class TicketPreviewRequest(BaseModel):
    subject: str = Field(min_length=3, max_length=100)
    message: str = Field(min_length=10, max_length=2000)
    priority: int = Field(ge=1, le=10)
