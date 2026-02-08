# JobScout AI

An intelligent LinkedIn job scraper with AI-powered CV matching that automatically finds and ranks job opportunities based on your resume.

## 🎯 Overview

JobScout AI is a comprehensive job discovery platform that:
- **Automatically scrapes** LinkedIn job listings based on your search criteria
- **Matches jobs** to your CV using AI-powered analysis
- **Ranks opportunities** by relevance score
- **Provides a REST API** for easy integration and job querying

The system runs on a scheduled basis, continuously discovering new opportunities and updating match scores as your CV evolves.

## ✨ Features

- 🤖 **AI-Powered Matching**: Uses Hugging Face inference models to calculate job-CV compatibility scores
- 🔄 **Automated Scraping**: Scheduled LinkedIn job scraping (configurable via Celery Beat)
- 📊 **Smart Filtering**: Query jobs by title, location, and match score
- 🔐 **Session Management**: Persistent LinkedIn authentication with automatic session renewal
- 🐳 **Dockerized**: Complete containerized setup with Docker Compose
- 📝 **File Upload**: Upload your CV (PDF) and custom matching prompt (TXT) via API
- 🔍 **Rich Job Data**: Captures job title, company, location, description, posting date, and more

## 🏗️ Architecture

```
┌─────────────┐
│   FastAPI   │  ← REST API (Job queries, file uploads)
└──────┬──────┘
       │
┌──────▼──────────────────┐
│   Celery Workers        │  ← Background task processing
│  ┌────────────────────┐ │
│  │ Scrape LinkedIn    │ │
│  │ Process Jobs (AI)  │ │
│  └────────────────────┘ │
└──────┬──────────────────┘
       │
┌──────▼──────┐  ┌──────────────┐  ┌─────────────┐
│ PostgreSQL  │  │    Redis     │  │  Playwright │
│  (Jobs DB)  │  │ (Celery MQ)  │  │  (Scraper)  │
└─────────────┘  └──────────────┘  └─────────────┘
```

## 🛠️ Tech Stack

- **API Framework**: FastAPI
- **Task Queue**: Celery with Redis broker
- **Database**: PostgreSQL with SQLAlchemy ORM
- **Web Scraping**: Playwright (Chromium)
- **AI/ML**: Hugging Face Inference API
- **Containerization**: Docker & Docker Compose
- **Process Management**: Supervisor
- **HTML Parsing**: BeautifulSoup4

## 📋 Prerequisites

- Docker and Docker Compose
- Hugging Face account with API token
- LinkedIn account credentials
- (Optional) Python 3.12+ for local development

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone <repository-url>
cd jobscout_ai
```

### 2. Environment Configuration

Create a `.env` file in the project root:

```env
# LinkedIn Credentials
LINKEDIN_USERNAME=your_linkedin_email@example.com
LINKEDIN_PASSWORD=your_linkedin_password

# Hugging Face AI
HF_TOKEN=your_huggingface_token
HF_MODEL=your_model_name  # e.g., meta-llama/Llama-3.1-8B-Instruct

# Database Configuration
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=postgres
POSTGRES_PORT=5432
POSTGRES_DB=jobscout_ai

# Redis Configuration
REDIS_URL=redis://redis:6379/0

# LinkedIn URLs (optional - defaults provided)
BASE_URL=https://www.linkedin.com
LOGIN_URL=/uas/login
FEED_URL=/feed
JOB_SEARCH_URL=/jobs/search/?
JOB_SEARCH_PARAMS=geoId=102974008&keywords=junior software engineer&refresh=true

# File Paths (optional - defaults provided)
SESSION_FILE_PATH=/data/session.json
CV_FILE_PATH=/data/resume.pdf
PROMPT_FILE_PATH=/data/prompt.txt
```

### 3. Build and Run

```bash
docker compose up -d
```

This will start:
- PostgreSQL database
- Redis broker
- Application container (API + Celery workers)

### 4. Upload Your CV and Prompt

Once the services are running, upload your CV and matching prompt:

```bash
# Upload CV (PDF)
curl -X POST "http://localhost:8000/upload-cv" \
  -F "file=@/path/to/your/resume.pdf"

# Upload matching prompt (TXT)
curl -X POST "http://localhost:8000/upload-prompt" \
  -F "file=@/path/to/your/prompt.txt"
```

**Prompt Template Example** (`prompt.txt`):
```
You are a job matching expert. Analyze the following CV and job description, then provide a match score from 0-100.

CV:
{{cv_text}}

Job Description:
{{job_description}}

Provide only a single integer score (0-100) representing how well the CV matches the job requirements.
```

### 5. Access the API

The API will be available at `http://localhost:8000`

- **API Docs**: `http://localhost:8000/docs` (Swagger UI)
- **Health Check**: `http://localhost:8000/health`

## 📡 API Endpoints

### Health Check
```http
GET /health
```

### Upload CV
```http
POST /upload-cv
Content-Type: multipart/form-data

file: <PDF file>
```

### Upload Prompt
```http
POST /upload-prompt
Content-Type: multipart/form-data

file: <TXT file>
```

### Get Jobs
```http
GET /jobs?limit=25&skip=0&match_score=true&title=engineer&location=remote
```

**Query Parameters:**
- `limit` (int, 1-100): Number of jobs to return (default: 25)
- `skip` (int): Pagination offset (default: 0)
- `match_score` (bool): Filter jobs with match scores only (default: true)
- `title` (string, optional): Filter by job title (case-insensitive)
- `location` (string, optional): Filter by location (case-insensitive)

**Response:**
```json
{
  "status": "success",
  "meta": {
    "page": 1,
    "page_size": 25,
    "total_results": 150,
    "total_pages": 6
  },
  "data": [
    {
      "id": "1234567890",
      "title": "junior software engineer",
      "company": "tech corp",
      "company_website": "https://linkedin.com/company/tech-corp",
      "location": "san francisco, ca",
      "location_type": "remote",
      "job_url": "https://linkedin.com/jobs/view/1234567890",
      "description": "Job description text...",
      "posted_date": "2 days ago",
      "match_score": 85,
      "scraped_at": "2024-01-15T10:30:00Z"
    }
  ]
}
```

## ⚙️ Configuration

### Scheduled Tasks

Jobs are automatically scraped and processed on a schedule defined in `app/celery.py`:

- **Scraping**: Runs at 8 AM, 2 PM, and 8 PM UTC (configurable)
- **Processing**: Runs every 30 minutes to process new unscored jobs

To modify the schedule, edit the `beat_schedule` in `app/celery.py`:

```python
app.conf.beat_schedule = {
    "scrape-linkedin-jobs-hourly": {
        "task": "app.tasks.scrape_linkedin_jobs_task",
        "schedule": crontab(minute="0", hour="8,14,20"),
    },
    "process-jobs-hourly": {
        "task": "app.tasks.process_jobs",
        "schedule": crontab(minute="*/30"),
    },
}
```

### Job Search Parameters

Customize your LinkedIn job search by modifying `JOB_SEARCH_PARAMS` in your `.env`:

```
JOB_SEARCH_PARAMS=geoId=102974008&keywords=python developer&locationId=us:0&refresh=true
```

- `geoId`: Geographic location ID (find via LinkedIn URL)
- `keywords`: Job title or skills to search for
- `locationId`: Location filter
- `refresh`: Force refresh of results

## 📁 Project Structure

```
jobscout_ai/
├── api/                 # FastAPI application
│   ├── __init__.py
│   └── main.py         # API routes and endpoints
├── app/                 # Application core
│   ├── __init__.py
│   ├── celery.py       # Celery configuration and schedules
│   ├── config.py       # Settings and environment variables
│   ├── service.py      # Service layer (singletons)
│   └── tasks.py        # Celery background tasks
├── database/           # Database layer
│   ├── __init__.py
│   ├── models.py       # SQLAlchemy models
│   └── session.py      # Database manager
├── linkedin/           # LinkedIn scraping module
│   ├── __init__.py
│   ├── auth.py         # LinkedIn authentication
│   ├── processor.py    # AI job processing
│   └── scraper.py      # Job scraping logic
├── tests/              # Test suite
│   └── test_scraper.py
├── compose.yml         # Docker Compose configuration
├── Dockerfile          # Application container definition
├── requirements.txt    # Python dependencies
├── supervisord.conf    # Process manager configuration
└── README.md          # This file
```

## 🔧 Development

### Local Development Setup

1. **Create Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. **Install Dependencies**
```bash
pip install -r requirements.txt
python -m playwright install chromium
```

3. **Run Services Locally**

Start PostgreSQL and Redis:
```bash
docker compose up -d postgres redis
```

Run the API:
```bash
uvicorn api.main:app --reload --host 0.0.0.0 --port 8000
```

Run Celery worker (in separate terminal):
```bash
celery -A app.celery worker --beat --loglevel=info
```

### Running Tests

```bash
pytest tests/
```

## 🐳 Docker Details

### Container Services

- **app**: Main application container running:
  - FastAPI server (port 8000)
  - Celery worker with beat scheduler
  - Managed by Supervisor

- **postgres**: PostgreSQL 18 database
- **redis**: Redis 8 cache/broker

### Volumes

- `postgres_data`: Persistent database storage
- `redis_data`: Persistent Redis data
- `app_data`: Application data (sessions, CV, prompts)

### Health Checks

All services include health checks to ensure proper startup order and reliability.

## 🔒 Security Considerations

- **Credentials**: Never commit `.env` files or credentials to version control
- **LinkedIn**: Be mindful of LinkedIn's Terms of Service regarding automated scraping
- **Rate Limiting**: The scraper includes delays and error handling to avoid aggressive requests
- **Session Storage**: LinkedIn sessions are stored locally and automatically renewed

## 📝 Notes

- **LinkedIn Authentication**: The system uses session-based authentication. If 2FA is enabled, you may need to handle it manually on first login.
- **Match Scores**: Jobs are processed in batches of 2 to manage API rate limits. Adjust in `app/tasks.py` if needed.
- **Error Handling**: Tasks include retry logic with exponential backoff for resilience.
- **Data Persistence**: All job data is stored in PostgreSQL and persists across container restarts.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

[Specify your license here]

## 🙏 Acknowledgments

- Built with [FastAPI](https://fastapi.tiangolo.com/)
- Web scraping powered by [Playwright](https://playwright.dev/)
- AI matching via [Hugging Face](https://huggingface.co/)

---

**Happy Job Hunting! 🎯**
