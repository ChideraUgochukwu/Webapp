# StudyBuddy - Student Chat Web Application

A Django-based chat application for students with topic-based chat rooms and real-time messaging.

## Features

- User authentication with email verification
- Topic-based chat rooms
- Real-time messaging using WebSockets
- User profiles with avatars and interests
- Responsive design with Bootstrap 5

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Virtual environment (recommended)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd StudyBuddy
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create .env file:
```bash
cp .env.example .env
# Edit .env with your settings
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Create a superuser:
```bash
python manage.py createsuperuser
```

7. Run the development server:
```bash
python manage.py runserver
```

## Usage

1. Access the application at http://localhost:8000
2. Register a new account or login
3. Create or join topic-based chat rooms
4. Start chatting in real-time!

## Development

- The project uses Django 4.2.7
- Real-time chat is implemented using Django Channels
- Frontend styling uses Bootstrap 5 and custom CSS
- Authentication handled by django-allauth

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
