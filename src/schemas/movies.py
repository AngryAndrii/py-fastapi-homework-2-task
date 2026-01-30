import enum
from typing import Optional, List

from pydantic import BaseModel, ConfigDict, Field

from datetime import date

from database.models import MovieStatusEnum
from schemas.actors import ActorSchema
from schemas.countries import CountrySchema
from schemas.genres import GenreSchema
from schemas.languages import LanguageSchema


class MovieBase(BaseModel):
    id: int
    name: str
    date: date
    score: float
    overview: str


class MovieListItemSchema(MovieBase):
    model_config = ConfigDict(from_attributes=True)


class MovieListResponseSchema(BaseModel):
    movies: List[MovieListItemSchema]
    prev_page: Optional[str]
    next_page: Optional[str]

    total_pages: int
    total_items: int


class MovieDetailSchema(MovieBase):
    status: enum.Enum
    budget: float
    revenue: float
    country_id: int
    country: CountrySchema
    genres: List[GenreSchema]
    actors: List[ActorSchema]
    languages: List[LanguageSchema]

    model_config = ConfigDict(from_attributes=True)


class MovieUpdateSchema(BaseModel):
    name: Optional[str] = Field(None, max_length=255)
    date: Optional[date] = None | str
    score: Optional[float] = Field(None, ge=0, le=100)
    overview: Optional[str] = None
    status: Optional[MovieStatusEnum] = None
    budget: Optional[float] = Field(None, ge=0)
    revenue: Optional[float] = Field(None, ge=0)


class MovieCreateSchema(BaseModel):
