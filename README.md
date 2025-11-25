# AI Avatar Creator Project

This project is a full-stack application for AI avatar creation with Text-To-Speech (TTS), lip-sync animation, and media storage on AWS S3. It consists of a Python backend (Flask) and a React frontend dashboard.

## Features
- AI avatar creation API (simulated placeholder for Heygen, D-ID)
- TTS and lip-sync integration placeholder
- AWS S3 media storage upload and retrieval
- React frontend dashboard for input and avatar preview

## Prerequisites
- Python 3.8+
- Node.js 16+
- AWS account with S3 bucket and access keys

## Setup

### Backend

1. Navigate to the backend folder:

```bash
cd backend
```

2. Create and activate a Python virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install Python dependencies:

```bash
pip install flask flask-cors boto3
```

4. Create a `.env` file in the backend folder based on `.env.example` with your AWS credentials.

5. Run the Flask server:

```bash
flask run --host=0.0.0.0
# Or
python app.py
```

### Frontend

1. Navigate to the frontend folder:

```bash
cd frontend
```

2. Install dependencies:

```bash
npm install
```

3. Run the React app:

```bash
npm start
```

The frontend will run on `http://localhost:3000` and interact with the backend API on port 5000.

## Notes

- The avatar creation and TTS process is currently simulated.
- To integrate with real APIs like Heygen or D-ID, update the backend `/api/generate-avatar` endpoint.
- Ensure your AWS credentials have permissions for S3 operations.
- This setup is for development; review and enhance security and scaling for production use.

## License

MIT License
