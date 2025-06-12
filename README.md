# ALT-SOE-024-1902-Second-Semester-Exam
Event Management API System

This is a RESTful API built with FastAPI to manage events, users, speakers, and registrations. 
It supports creating, reading, updating, and deleting (CRUD) entities, as well as managing user registrations for events.

Features
User management: Create, update, deactivate, and delete users
Event management: Create, update, close, and delete events
Speaker management: Manage speakers linked to events
Registration management: Users can register for open events, track attendance, track registrations and validate to prevent duplicates

Technologies Used
Python 3.x    FastAPI  Pydantic for data validation

Project Structure
schemas/: Pydantic models for Users, Events, Speakers, Registrations
services/: Business logic for Users, Events, Registrations
routes/: API route handlers for Users, Events, Registrations, Speakers
Main application initializes routers and runs the API

API Endpoints
Users
Method	Path	Description
GET	/users/	Retrieve all users
GET	/users/{id}/	Retrieve user by ID
POST	/users/	Create a new user
PUT	/users/{id}/	Update existing user
PATCH	/users/{id}/	Deactivate user (set inactive)
DELETE	/users/{id}/	Delete user

Events
Method	Path	Description
GET	/events/	Retrieve all events
GET	/events/{id}/	Retrieve event by ID
POST	/events/	Create a new event
PUT	/events/{id}/	Update existing event
PATCH	/events/{id}/	Close (deactivate) event
DELETE	/events/{id}/	Delete event

Registrations
Method	Path	Description
GET	/registrations/	Retrieve all registrations
GET	/registrations/{user_id}/	Retrieve all registrations for a user
POST	/registrations/	Register a user for an event
PATCH	/registrations/{reg_id}/	Mark attendance for a registration

Data Models
User: id, name, email, is_active
Event: id, title, location, date, is_open, speaker_ids
Speaker: id, name, topic
Registration: id, user_id, event_id, registration_date, attended

Installation
Clone the repo
Install dependencies: fastapi, uvicorn, pydantic 
Run the app: uvicorn main:app --reload
Usage
Use an API client like Postman or curl to interact with the endpoints.

Error Handling
The API returns appropriate HTTP status codes and messages for common errors.

Notes
Data is stored in-memory using Python lists (no database).
Speaker entities exist but are static; linking speakers to events uses their IDs.
