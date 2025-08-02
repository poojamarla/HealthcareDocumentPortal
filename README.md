# Healthcare Document Portal

## Project Overview
The Healthcare Document Portal is a web application that allows users to upload, view, download, and delete PDF documents. It is built using React for the frontend and Flask for the backend, with SQLite for database management.

## Features
- Upload PDF files
- List all uploaded documents
- Download documents
- Delete documents

## Tech Stack
- **Frontend**: React
- **Backend**: Flask
- **Database**: SQLite

## Architecture
The application utilizes a client-server architecture:
- **React App**: Manages the user interface and sends requests to the server.
- **Flask API**: Handles file operations and database interactions.
- **File Storage**: Stores uploaded PDF files.
- **SQLite DB**: Stores file metadata.

## How to Run Locally

### Prerequisites
- Node.js
- Python 3.x

### Setup Instructions

1. **Clone the repository**
   ```bash
   
   git clone https://github.com/poojamarla/HealthcareDocumentPortal.git
   cd HealthcareDocumentPortal

2. **Backend Setup**
   Navigate to the backend directory
   
   `cd backend`
   
   Create a virtual environment and activate it

   `python -m venv venv`
   
   `source venv/bin/activate`   #On Windows use `venv\Scripts\activate` 
   
   Install dependencies
   
   `pip install -r requirements.txt`
   
   Run the Flask server
   
   `flask run`

4. **Frontend Setup**
   Navigate to the frontend directory
   
   `cd my-healthcare-portal`
   
   Install dependencies
   
   `npm install`
   
   Run the React app
   
   `npm start`
### Assumptions
- Max file size is 10MB.
- No user authentication.
- Suitable for development/testing environments.
