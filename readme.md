Application Setup and Execution
Prerequisites
Python 3.x installed on your system.
Django framework installed globally or in a virtual environment.
Installation
Clone the repository or download the project files.

Navigate to the project directory:

cd path/to/your/project

Install the required Python packages:
bash

pip install -r requirements.txt


Database Setup
Ensure that you have a compatible database server installed (e.g., PostgreSQL, MySQL, SQLite).

Open the settings.py file in your project's main directory.

Modify the database configuration section with your database details (e.g., username, password, host, etc.).

Apply database migrations:

bash

python manage.py migrate
Data Generation (Optional)
If you need to generate random data (10M Users, 1M Questions) to simulate the application's scale, you can run the data generation script.



python data_generation.py

Running the Development Server
To start the development server and run the application:



python manage.py runserver

The application will now be accessible at http://localhost:8000/ or http://127.0.0.1:8000/.

Unit Tests

The application includes comprehensive unit tests for API views and data generation to ensure functionality and performance.

Running the Tests

To execute the unit tests, run the following command:


python manage.py test

The test results will be displayed in the console.

API Documentation

The application provides the following API endpoints:

1. user-question-counts
This API provides a count of total favorite questions and read questions per user, paginated to 100 users per page.

Endpoint:

sql

GET /api/user-question-counts/
Response:

json

HTTP 200 OK
Content-Type: application/json

{
    "count": 100,
    "next": "http://example.com/api/user-question-counts/?page=2",
    "previous": null,
    "results": [
        {
            "user_id": 1,
            "display_name": "John Doe",
            "favorite_count": 10,
            "read_count": 20
        },
        ...
    ]
}
2. filter-questions
This API allows filtering questions by read, unread, favorite, and unfavorite status.

Endpoint:

sql

GET /api/filter-questions/
Query Parameters:

status (Optional): Filter questions by status (read, unread, favorite, unfavorite).
Response:

json

HTTP 200 OK
Content-Type: application/json

[
    {
        "id": 1,
        "question": "What is the capital of France?",
        "option1": "Berlin",
        "option2": "Paris",
        "option3": "London",
        "option4": "Madrid",
        "option5": "Rome",
        "answer": 2,
        "explain": "Paris is the capital of France."
    },
    ...
]
Additional Notes
The application uses caching and pagination to optimize API response times.
For data generation, the script data_generation.py generates random users and questions to simulate large-scale data.
Summary
This documentation provides the necessary steps to set up and run the application, execute unit tests, and understand the available API endpoints. Additionally, it outlines the data generation process and the application's optimizations for performance. If you encounter any issues or have any questions, please refer to the documentation or reach out to the development team for assistance. Happy coding!
