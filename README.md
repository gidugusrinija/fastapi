🚀 Layered Asynchronous User Service: FastAPI + MongoDB (Motor)

This project implements a high-performance backend service designed for user data management. My core objective was to architect a system using FastAPI and the Motor asynchronous driver for MongoDB, strictly adhering to the Separation of Concerns (SoC) principle to ensure long-term stability and testability.

🛠️ Architectural Design

The application is structured into three distinct layers. This decomposition ensures that each component has a singular responsibility and minimizes coupling between the API interface and data persistence.

api_layer: Serves as the presentation and control layer. Its responsibilities include:

Defining HTTP routes and handlers.

Request validation using Pydantic models (UserIn).

Dependency injection (e.g., providing the MongoDB collection).

Translating the final database object into the specified UserOut response format. (e.g., mqproxy.py)

service_layer: Encapsulates the core business logic and transaction orchestration. It operates as the intermediary between the API and data layers.

Applying business rules (e.g., adding a created_at timestamp).

Managing the sequence of data operations. (e.g., insert_valid_user.py)

data_access_layer: Handles all asynchronous persistence operations against MongoDB. This layer is strictly dedicated to CRUD functionality and uses the Motor client directly. It is unaware of any application-specific business logic.

📦 Prerequisites

Successful execution of this service requires the following environment components:

Python 3.10+

pip

MongoDB Server: The database must be running and accessible on the default port 27017.

I utilize mongodb://127.0.0.1:27017 for connections, as this IP address typically resolves more reliably than localhost within asynchronous contexts, preventing ServerSelectionTimeoutError.

⚙️ Project Initialization

1. Repository Cloning

git clone <your-repository-url>
cd <your-repository-folder>


2. Virtual Environment and Activation

I recommend using a dedicated virtual environment for dependency isolation.

# Using venv
python -m venv venv
source venv/bin/activate 

# If using Conda
conda create -n fastapi-app python=3.11
conda activate fastapi-app


3. Dependency Installation

Install the required Python packages:

pip install fastapi "uvicorn[standard]" motor pydantic-settings


4. Configuration

My configuration leverages Pydantic settings. The base settings are defined in app/configuration_layer/settings.py and default to the local MongoDB instance.

To override connection parameters (e.g., using a remote database), create a .env file in the project root:

# .env file content
MONGO_DETAILS="mongodb://<host>:<port>" 
DATABASE_NAME="production_db"
COLLECTION_NAME="users_collection"


▶️ Execution Procedure

Step 1: Initialize MongoDB Service

The database must be actively listening on 127.0.0.1:27017 before proceeding.

Using Homebrew (macOS):

brew services start mongodb-community@6.0


Using Docker:

docker run --name mongo_fastapi -d -p 27017:27017 mongo


Step 2: Start the FastAPI Server

Execute the application using Uvicorn, targeting the application entry point:

# Syntax: uvicorn <module_path>:<app_variable>
uvicorn api_layer.mqproxy:app --host 0.0.0.0 --port 18005 --reload


The server will be available at http://0.0.0.0:18005.

📌 API Contract

The interactive OpenAPI documentation (Swagger UI) is available at: http://0.0.0.0:18005/docs

POST /save/user/data

This endpoint facilitates the insertion of a new user document through the layered architecture.

Method

Path

Summary

HTTP Status

POST

/save/user/data

Inserts a new user record.

201 Created

Request Body Schema (UserIn):

{
  "name": "Alex Johnson",
  "age": 32,
  "email": "alex.j@example.com"
}


Success Response Schema (UserOut):

{
  "id": "60c72b2f6c9d0f3c5b5a6c11",
  "name": "Alex Johnson",
  "age": 32,
  "email": "alex.j@example.com"
}
