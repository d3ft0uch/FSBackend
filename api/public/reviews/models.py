from datetime import datetime
from typing import Optional
from pydantic import UUID4, model_validator, BaseModel, FieldValidationInfo
from typing import Literal
from sqlalchemy.orm import relationship
from sqlmodel import Field, SQLModel, Relationship
import uuid
from fastapi_users import schemas
from api.utils.generic_models import UserListingLink
from enum import Enum

class Rating(str, Enum):
    GREAT = "GREAT",
    PROBLEMS = "PROBLEMS",
    BAD = "BAD"

class ReviewBase(SQLModel):
    user_id_to: UUID4 = Field(foreign_key='user.id', unique=False, nullable=False)
    rating: Rating
    review_text: str

class ReviewRead(ReviewBase):
    review_id: int = Field(primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = Field(
        default_factory=datetime.utcnow,
        sa_column_kwargs={"onupdate": datetime.utcnow},)

class Review(ReviewRead, table=True):
    user_id_from: UUID4 = Field(foreign_key='user.id', unique=False, nullable=False)

class ReviewCreateOrUpdate(ReviewBase):
    pass
