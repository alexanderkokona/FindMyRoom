README: Indoor Navigation API
Project Overview

This project implements an indoor navigation system using a JSON map of nodes and edges. It exposes a FastAPI HTTP API for finding the shortest path to a room from a given starting node. The API can be accessed by web apps (Angular, React, etc.) or other clients.

🛠️ Requirements

Python 3.10+

Packages:

pip install fastapi uvicorn pydantic

Windows, macOS, or Linux

Optional: Angular/React frontend to call the API

📂 Project Structure
Tests directory:
│
├─ Directions.py        # Core navigation logic (Dijkstra algorithm)
├─ api.py               # Main FastAPI app (Includes CORS & Frontend endpoints)
├─ STCf3.json           # Map graph JSON
└─ README Indoor Navigation API.txt # This file

⚡ Running the API

1. Open your terminal in the root project folder.

2. Activate your virtual environment (Windows PowerShell):
   .\.venv\Scripts\Activate.ps1

3. Install the required dependencies:
   pip install fastapi uvicorn pydantic
   (Or run: pip install -r requirements.txt)

4. Navigate to the folder containing the python scripts:
   cd tests

5. Run the API server:
   python -m uvicorn api:app --reload

--reload restarts the server automatically when code changes.
Note: We run `api:app` because `api.py` contains the CORS configuration needed for the Angular frontend to connect successfully without being blocked.

Open your browser at:

http://127.0.0.1:8000/docs

This is FastAPI’s interactive API documentation.

You can test your endpoints directly from there.

🔹 API Endpoint
POST /navigate

Request Body:

{
  "start_node": "ENT_WEST",
  "room_number": "375"
}

Response:

{
  "start": "West Entrance",
  "destination_room": "375",
  "distance": 42,
  "steps": [
    "Walk through the main corridor toward the central staircase",
    "Turn right at the end of the west hallway toward the central corridor"
  ]
}
🌐 Enabling Access from Frontend Apps

If you plan to call this API from an Angular/React frontend, add CORS middleware in Directions.py:

from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost:4200",  # frontend development server
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
🧭 How to Use

Start the API server (see above).

Open /docs in a browser to test manually.

Use a frontend (Angular, React, or curl) to make POST requests to /navigate.

Get shortest-path directions with step-by-step instructions.

⚠️ Notes

The interactive console part (main() function) is disabled when using FastAPI.

JSON file STCf3.json must be in the same folder as Directions.py.

Node IDs and room numbers must match entries in your JSON map.

📦 Optional: Run Example Angular Call
fetch("http://127.0.0.1:8000/navigate", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ start_node: "ENT_WEST", room_number: "375" })
})
.then(res => res.json())
.then(data => console.log(data));