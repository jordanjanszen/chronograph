# Cronograph 2.0

Cronograph is a time-tracking web application built with Django. It allows you to track time spent on various activities throughout your day, ranging from sleep, workouts, meals, and more. With Cronograph, journaling becomes a new experience — helping you visualize and analyze how you spend your time through detailed statistics and logs. Whether you're aiming for productivity or just curious about your habits, Cronograph gives you a comprehensive overview of your life in a sleek, intuitive interface.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies](#technologies)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Track Daily Activities**: Log sleep, workouts, meals, and any other activities you perform throughout the day.
- **Customizable Categories**: Add your own activity categories to match your personal habits and lifestyle.
- **Data Visualization**: View your tracked activities in easy-to-read charts and graphs to monitor trends and patterns.
- **Statistics**: Analyze detailed statistics of how you spend your time over days, weeks, and months.
- **Journaling Integration**: Add notes and reflections to each activity, making it a journal as much as a tracker.
- **Mobile-First Design**: Optimized for mobile and desktop use, ensuring a smooth experience across devices.

## Installation

To get Cronograph up and running locally, follow these steps:

### Prerequisites

- Python 3.8+
- Django 4.x
- PostgreSQL or SQLite (for local development)
- Node.js and npm (optional, for front-end assets)

### Setup

Step 1: Clone the repository

   ```bash
   git clone https://github.com/yourusername/cronograph.git
   cd cronograph
   ```

Step 2: Create and Activate a Virtual Environment

```bash
  python -m venv venv
  source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

Step 4: Configure Environment Variables

Create a `.env` file in the project root with the necessary environment variables for your database and Django settings. For example:

```bash
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=postgres://user:password@localhost:5432/cronograph
```

Step 5: Apply Migrations

```bash
python manage.py migrate
```

Step 6: Create a Superuser

```bash
python manage.py createsuperuser
```

Step 7: Run the Development Server

```bash
python manage.py runserver
```

Step 8: Access the App

Open your browser and go to `http://127.0.0.1:8000/` to access Cronograph.

## Usage

1. **Register an account** and log in to start tracking your daily activities.
2. **Add categories** based on the activities you wish to log, such as sleep, exercise, or meals.
3. **Start logging** your activities by clicking "Add Activity" and inputting the time spent.
4. **View Statistics**: Navigate to the statistics page to view detailed analytics and graphical representations of how you spend your time.
5. **Journal Entries**: Optionally add notes to each activity log to reflect on your day.

## Technologies

- **Backend**: [Django](https://www.djangoproject.com/)
- **Database**: PostgreSQL (for production) / SQLite (for development)
- **Frontend**: HTML5, CSS3, JavaScript (using Django templates)
- **Authentication**: Django's built-in authentication system (optional OAuth2 support)
- **Visualizations**: Chart.js for graphs and time analysis

## Screenshots

*(You can include screenshots here to show off your app’s UI and main features.)*

## Contributing

We welcome contributions! If you would like to contribute to Cronograph, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request, and be sure to describe the changes you’ve made.

Please make sure all new features and changes are covered by tests.

## License

Cronograph is released under the MIT License. See [LICENSE](LICENSE) for more details.
