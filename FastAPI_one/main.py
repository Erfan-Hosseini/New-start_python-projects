from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field


app = FastAPI()

class Movie(BaseModel):
    id: int = Field(gt=0, description="The ID must be positive")
    title: str = Field(min_length=1, max_length=100)
    director: str = Field(min_length=1, max_length=50)
    year: int = Field(ge=1900, le=2100, description="Movie release date")
    rating: float = Field(ge=0, le=10, default=7.0)
    available: bool = True
movies: list[Movie] = []

# Home
@app.get("/")
def root():
    return {"message": "🎬 Movie API is running!"}


# Create
@app.post("/add-movie", status_code=status.HTTP_201_CREATED)
def add_movie(movie: Movie):
    for m in movies:
        if m.id == movie.id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail=f"Movie {movie.id} already exist"
            )
    movies.append(movie)
    return {"message": f"The {movie.title} was added to the list.", "movie": movie}

# Read all
@app.get("/show-movies", response_model=list[Movie])
def show_movies():
    return movies

# Read by ID (path param)
@app.get("/movie-id/{movie_id}")
def movie_by_id(movie_id: int):
    for m in movies:
        if m.id == movie_id:
            return {"movie": m}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie's ID not found")

# Read by title (path param)
@app.get("/movie-title/{movie_title}")
def movie_by_title(movie_title: str):
    for m in movies:
        if m.title.lower() == movie_title.lower():
            return {"movie": m}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie's title not found")

# Update by ID (body = Movie)
@app.put("/update/{movie_id}")
def update_movie(movie_id: int, updated_movie: Movie):
    for i, m in enumerate(movies):
        if m.id == movie_id:
            movies[i] = updated_movie
            return {"message": f"Movie ID {movie_id} updated successfully!", "movie": updated_movie}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie's ID not found")

# Delete by ID
@app.delete("/delete/{movie_id}", status_code=status.HTTP_200_OK)
def delete_movie(movie_id: int):
    for i, m in enumerate(movies):
        if m.id == movie_id:
            deleted = movies.pop(i)
            return {"message": f"Movie '{deleted.title}' was deleted"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie's ID not found")

# List by director (collect all matches)
@app.get("/directors/{director}")
def by_director(director: str):
    result = [m.dict() for m in movies if m.director.lower() == director.lower()]
    if result:
        return {"movies": result}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Director not found")
