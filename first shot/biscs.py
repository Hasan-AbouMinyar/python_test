


import sqlite3
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field
from datetime import date
from typing import List
import uvicorn
import asyncio


# --- Configuration ---
DATABASE_FILE = "people_data.db"

# --- Database Layer ---

def get_db_connection():
    """Dependency: Creates and yields a database connection."""
    conn = sqlite3.connect(DATABASE_FILE)
    conn.row_factory = sqlite3.Row  # Makes rows behave like dictionaries
    try:
        yield conn
    finally:
        conn.close()

def setup_database(conn: sqlite3.Connection):
    """Creates the 'people' table if it doesn't exist."""
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS people (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        birth_year INTEGER NOT NULL
    );
    """)
    # Add initial data only if table is empty
    cursor.execute("SELECT COUNT(*) FROM people")
    if cursor.fetchone()[0] == 0:
        initial_data = [
            ('Hasan', 2003),
            ('Sarah', 2010),
            ('Ali', 1960),
            ('Mona', 2023)
        ]
        cursor.executemany("INSERT INTO people (name, birth_year) VALUES (?, ?)", initial_data)
    conn.commit()
    print("Database initialized and checked successfully.")


# --- Pydantic Models (Data Validation Layer) ---

class PersonBase(BaseModel):
    """Base model with common fields."""
    name: str = Field(..., min_length=2, description="The person's full name.")
    birth_year: int = Field(..., gt=1900, le=date.today().year, description="The person's year of birth.")

class PersonCreate(PersonBase):
    """Model used for creating a new person via API."""
    pass

class PersonResponse(PersonBase):
    """Model for returning person data from the API, includes calculated fields."""
    id: int
    age: int
    category: str
    is_centenarian: bool = Field(description="Is the person 100 years old or more?")

# --- FastAPI Application ---

app = FastAPI(
    title="People Data API 🧑‍💻",
    description="A hyper-advanced API to manage, create, and retrieve data about people.",
    version="3.0.0"
)

@app.on_event("startup")
async def startup_event():
    """Initialize the database when the application starts."""
    # Run setup in a separate thread to avoid blocking the event loop
    await asyncio.to_thread(setup_database, next(get_db_connection()))


# --- API Endpoints (Routes) ---

@app.post("/people/", response_model=PersonResponse, status_code=201)
async def create_person(
    person: PersonCreate, 
    db: sqlite3.Connection = Depends(get_db_connection)
):
    """
    Creates a new person record in the database.
    """
    try:
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO people (name, birth_year) VALUES (?, ?)",
            (person.name, person.birth_year)
        )
        db.commit()
        new_id = cursor.lastrowid
        return await get_person(new_id, db)
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=400, detail="An error occurred while creating the person.")


@app.get("/people/", response_model=List[PersonResponse])
async def list_people(db: sqlite3.Connection = Depends(get_db_connection)):
    """
    Retrieves a list of all people from the database with calculated age data.
    """
    cursor = db.cursor()
    cursor.execute("SELECT id, name, birth_year FROM people")
    people_rows = cursor.fetchall()
    
    # Process rows into response models
    current_year = date.today().year
    response_list = []
    for row in people_rows:
        age = current_year - row['birth_year']
        category = "Senior" if age >= 65 else "Adult" if age >= 18 else "Teenager" if age >= 13 else "Child" if age >= 3 else "Baby"
        response_list.append(
            PersonResponse(
                id=row['id'],
                name=row['name'],
                birth_year=row['birth_year'],
                age=age,
                category=category,
                is_centenarian=(age >= 100)
            )
        )
    return response_list


@app.get("/people/{person_id}", response_model=PersonResponse)
async def get_person(
    person_id: int, 
    db: sqlite3.Connection = Depends(get_db_connection)
):
    """
    Retrieves a single person by their unique ID.
    """
    cursor = db.cursor()
    cursor.execute("SELECT id, name, birth_year FROM people WHERE id = ?", (person_id,))
    row = cursor.fetchone()
    if row is None:
        raise HTTPException(status_code=404, detail=f"Person with ID {person_id} not found.")

    age = date.today().year - row['birth_year']
    category = "Senior" if age >= 65 else "Adult" if age >= 18 else "Teenager" if age >= 13 else "Child" if age >= 3 else "Baby"
    return PersonResponse(
        id=row['id'],
        name=row['name'],
        birth_year=row['birth_year'],
        age=age,
        category=category,
        is_centenarian=(age >= 100)
    )

# --- To run the app directly (for development) ---
if __name__ == "__main__":
    print("🚀 Starting API server... Access documentation at http://127.0.0.1:8000/docs")
    uvicorn.run(app, host="127.0.0.1", port=8000)
