# Company Metadata Database

A Flask-based application for storing and managing company metadata. This application provides a robust backend system for storing company information with SQLAlchemy integration and environment-based configuration.

## Features

- Flask web framework with SQLAlchemy ORM
- Environment-based configuration using python-dotenv
- File upload support with configurable upload directory
- SQLite database (configurable to other databases)
- Secure configuration management

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Create and activate a virtual environment:
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python -m venv venv
source venv/bin/activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root directory with the following variables:
```
FLASK_APP=app.py
FLASK_ENV=development
DATABASE_URL=sqlite:///company_metadata.db
UPLOAD_FOLDER=uploads
SECRET_KEY=your-secret-key-here
```

## Project Structure

```
├── app.py              # Main application file
├── config.py           # Configuration settings
├── requirements.txt    # Project dependencies
├── .env               # Environment variables (create from .env.example)
├── .gitignore         # Git ignore file
└── uploads/           # Upload directory (created automatically)
```

## Running the Application

1. Ensure your virtual environment is activated
2. Run the Flask application:
```bash
flask run
```

The application will be available at `http://localhost:5000`

## Development

- The application uses Flask's application factory pattern
- SQLAlchemy is configured for database operations
- Environment variables are managed through python-dotenv
- File uploads are handled with configurable size limits

## Security Notes

- Never commit the `.env` file to version control
- Keep your `SECRET_KEY` secure and unique
- Regularly update dependencies for security patches

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

[Add your license information here] 