# Developer Landing API

Backend API for developer landing page.

## Overview

Developer Landing API is a FastAPI backend service for processing contact form requests.

The API provides:

- Contact form endpoint
- Input validation with Pydantic
- Sentiment analysis of messages
- Request logging
- Rate limiting protection
- Health check endpoint
- Automatic Swagger documentation

## Tech Stack

- Python 3.10+
- FastAPI
- Uvicorn
- Pydantic
- SlowAPI
- Google Generative AI
- python-dotenv

## Project Structure

```text
developer-landing/
│
├── app/
│   ├── main.py
│   ├── schemas.py
│   ├── services.py
│   └── logger.py
│
├── logs/
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

## Installation

### 1. Clone repository

```bash
git clone https://github.com/SwaggyBaron/developer-landing.git
```

Go to project directory:

```bash
cd developer-landing
```

---

### 2. Create virtual environment

MacOS / Linux:

```bash
python3 -m venv venv

source venv/bin/activate
```

Windows:

```bash
python -m venv venv

venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment variables

Create `.env` file in the project root:

```env
AI_API_KEY=your_google_ai_api_key
```

This key is used for message sentiment analysis.

---

## Run application

Start the development server:

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

---

## API Documentation

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

# Endpoints

## GET /

Basic API status check.

Response:

```json
{
  "status": "ok"
}
```

---

## GET /api/health

Health check endpoint.

Response:

```json
{
  "status": "ok"
}
```

---

## POST /api/contact

Creates a new contact request.

Request example:

```json
{
  "name": "Ryan Gosling",
  "email": "ryan@example.com",
  "phone": "+79999999999",
  "comment": "Спасибо большое!"
}
```

Response example:

```json
{
  "message": "Contact request received",
  "sentiment": "positive",
  "data": {
    "name": "Ryan Gosling",
    "email": "ryan@example.com",
    "phone": "+79999999999",
    "comment": "Спасибо большое!"
  }
}
```

---

## Security

Implemented:

- Rate limiting: `5 requests/minute`
- CORS middleware
- Global exception handler
- Request logging

---

## Development

Run server with auto reload:

```bash
uvicorn app.main:app --reload
```
