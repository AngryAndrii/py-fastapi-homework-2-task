from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select, func
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from database import get_db, MovieModel
from database.models import CountryModel, GenreModel, ActorModel, LanguageModel


router = APIRouter()

@router.get("/movies/")
async def list_movies(db: AsyncSession = Depends(get_db)):
    # films = await get_films(db)
    return {"Hello": "it is movies here!"}
