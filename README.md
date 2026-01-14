# FindMyRoom
A simple text-based instruction web app that will support students in finding rooms on campus. This project has a very specific, narrow scope to allow the team to complete the project.

# Project Title
Find My Room

## Team Members
Alexander Kokona
Thomas Gruber
Kim Josell
Lucas Smith

## Software Description
A simple web application that maps out text-based directions for students to find any room on campus. The beginning of this project will be restricted to a more manageable scope of just the STC building and just finding the fastest route before we add the warmest route and text-based directions before UX map directions.

## Architecture
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
|      (FastAPI / Python)  |
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
|   (Dijkstra Algorithm)   |
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
|  - Edges (distance, text)|
+---------------------------+

## Data Flow
User selects room
        ↓
Frontend sends request
        ↓
Backend validates user
        ↓
Routing engine finds path
        ↓
Instruction list returned
        ↓
Frontend displays steps


## Software Features

* [ ] Text-based directions to quadrants of rooms
* [ ] Still image mapping to each quadrant
* [ ] 

## Team Communication
Group Chat and Discord

## Team Responsibility

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

|Responsibility                      |Team Member(s)              |
|------------------------------------|----------------------------|
|Conducting Meetings                 |                            |
|Maintaining Team Assignment List    |                            |
|Ensuring GitHub is Working          |Alexander Kokona|
|Maintaining Documentation           |                            |
|Create & Display Presentations      |                            |
|Submit Team Assignments             |                            |

## Reflections
