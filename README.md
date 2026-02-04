FindMyRoom
Project Title

Find My Room

Team Members

Alexander Kokona

Thomas Gruber

Kim Josell

Lucas Smith

Software Description

A simple web application that maps out text-based directions for students to find any room on campus. The beginning of this project will be restricted to a more manageable scope of just the STC building and just finding the fastest route before we add the warmest route and text-based directions before UX map directions.

Architecture
+---------------------------+
|        Web / PWA          |
|---------------------------|
|  - Login                  |
|  - Schedule Entry         |
|  - Room Selection         |
|  - Text Directions View   |
+-------------+-------------+
              |
              | HTTPS (JSON)
              v
+---------------------------+
|        Backend API        |
|      (FastAPI / Python)   |
|---------------------------|
|  - Authentication (JWT)   |
|  - Schedule CRUD          |
|  - Route Request Handler  |
+-------------+-------------+
              |
              | Function Calls
              v
+---------------------------+
|     Routing Engine        |
|   (Dijkstra Algorithm)    |
|---------------------------|
|  - Loads Building Graph   |
|  - Computes Fastest Path  |
+-------------+-------------+
              |
              | Reads
              v
+---------------------------+
|   Building Graph Data     |
|   (JSON / GeoJSON File)   |
|---------------------------|
|  - Nodes (rooms, halls)   |
|  - Edges (distance, text) |
+---------------------------+

Programming Languages / Frameworks / Tools

Programming Languages

JavaScript (Frontend)

Python (Backend)

Frameworks

React (Frontend)

FastAPI (Backend)

Data Storage

JSON / GeoJSON files (routing graph)

SQLite or Firebase (future expansion)

Development Tools

Visual Studio Code

GitHub (required)

Postman (API testing)

Data Flow

User selects room

Frontend sends request

Backend validates user

Routing engine finds path

Instruction list returned

Frontend displays steps

Software Features

 Text-based directions to quadrants of rooms

 Still image mapping to each quadrant

 Warmest route option (Sprint 2)

 Text-based directions with landmarks (Sprint 2)

Team Communication

Group Chat and Discord

Team Responsibilities

Backend Lead: Thomas Gruber

Auth + schedule endpoints

Routing engine integration

Frontend Lead: Kim Josell

Login, schedule input, room selection UI

Instruction display component

Data / Graph Lead: Lucas Smith

Nodes and edges data entry

Instruction text writing

QA / Integration Lead: Alexander Kokona

Testing all routes

Connecting frontend and backend

Final demo prep

Everyone contributes to documentation and testing.

Responsibility	Team Member(s)
Conducting Meetings	Thomas Gruber
Maintaining Team Assignment List	Kim Josell
Ensuring GitHub is Working	Alexander Kokona
Maintaining Documentation	Lucas Smith
Create & Display Presentations	Alexander Kokona
Submit Team Assignments	Alexander Kokona
Reflections
