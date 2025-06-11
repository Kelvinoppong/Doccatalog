# Company Metadata Database

A Flask application for managing company metadata with SQLAlchemy integration.

## Quick Start

1. Clone and setup:
```bash
git clone <repository-url>
cd <repository-name>
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
```

2. Configure environment:
Create `.env` file with:
```
FLASK_APP=app.py
FLASK_ENV=development
DATABASE_URL=sqlite:///company_metadata.db
UPLOAD_FOLDER=uploads
SECRET_KEY=your-secret-key-here
```

3. Run the application:
```bash
flask run
```

## Features

- Flask with SQLAlchemy ORM
- Environment-based configuration
- File upload support
- SQLite database
- Secure configuration

## Project Structure

```
├── app.py              # Main application
├── config.py           # Configuration
├── requirements.txt    # Dependencies
├── .env               # Environment variables
└── uploads/           # Upload directory
```

## Security

- Keep `.env` out of version control
- Use a strong SECRET_KEY
- Update dependencies regularly

## License

[Add your license information here] 