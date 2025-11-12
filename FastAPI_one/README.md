# 🎬 FastAPI Movie API

A simple yet powerful FastAPI application for managing a collection of movies.  
This API demonstrates CRUD operations using **FastAPI** and **Pydantic** models.

---

## 🚀 Features
- Add new movies with validation
- View all movies
- Search movies by:
  - ID
  - Title
  - Director
- Update existing movie details
- Delete movies by ID
- Automatic data validation via Pydantic

---

## 🧠 Technologies Used
- **Python 3.10+**
- **FastAPI**
- **Uvicorn** (ASGI server)
- **Pydantic**

---

## 📦 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/FastAPI_one.git
   cd FastAPI_one

2. **Create & activate a virtual environment**
    python -m venv venv
    source venv/bin/activate   # macOS/Linux
    venv\Scripts\activate      # Windows

3. **Install dependencies**
    pip install fastapi uvicorn

4. **Run the app**
    uvicorn main:app --reload

5. **Open in your browser**
    API Root: http://127.0.0.1:8000

    Interactive Docs: http://127.0.0.1:8000/docs

    Alternate Docs (ReDoc): http://127.0.0.1:8000/redoc

## 📚 API Endpoints

| Method | Endpoint                     | Description            |
| ------ | ---------------------------- | ---------------------- |
| GET    | `/`                          | Root message           |
| POST   | `/add-movie`                 | Add a new movie        |
| GET    | `/show-movies`               | Get all movies         |
| GET    | `/movie-id/{movie_id}`       | Get movie by ID        |
| GET    | `/movie-title/{movie_title}` | Get movie by title     |
| GET    | `/directors/{director}`      | Get movies by director |
| PUT    | `/update/{movie_id}`         | Update movie details   |
| DELETE | `/delete/{movie_id}`         | Delete a movie by ID   |


## 🧩 Example Movie JSON    
{
  "id": 1,
  "title": "Inception",
  "director": "Christopher Nolan",
  "year": 2010,
  "rating": 8.8,
  "available": true
}


## ⚙️ Project Structure
FastAPI_one/
│
├── main.py           # FastAPI app
├── README.md         # Documentation
├── .gitignore
└── requirements.txt  # Optional (pip freeze > requirements.txt)


## 🧾 License
This project is open-source under the MIT License.

## ✨ Author
Github: https://github.com/Erfan-Hosseini
Email: erfan.hosseini2001@gmail.com

