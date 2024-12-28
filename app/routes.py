from fastapi import APIRouter
from app.utils import fetch_movie_by_title  # Import the utility function

router = APIRouter()

@router.get("/movie/{title}")
async def get_movie(title: str):
    """
    Endpoint to fetch movie data by title, including poster URL.
    :param title: Movie title to fetch.
    :return: JSON response with movie details and poster URL or error message.
    """
    movie_data = fetch_movie_by_title(title)
    return movie_data

