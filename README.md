# Seat Booking Management System Backend

## Overview

This project is a backend system designed to manage seat bookings for various venues. It allows for CRUD operations on venues, seats, and bookings, with robust validation to prevent double bookings. Built using Django and Django REST framework, this API serves as a reliable backend solution for seat management applications.

## Features

- **Venue Management**: Create, read, update, and delete venues.
- **Seat Management**: Assign seats to venues and manage them with CRUD operations.
- **Booking Management**: Handle bookings with built-in validation to prevent double bookings.
- **RESTful API**: Provides easy-to-use endpoints for integration with front-end applications or other services.

## Technologies Used

- **Django**: High-level Python web framework.
- **Django REST Framework**: Toolkit for building Web APIs.
- **SQLite**: Default database for Django projects, used for development purposes.

## Setup and Installation

### Prerequisites

- Python 3.8 or higher
- Pip (Python package installer)
- Git (for cloning the repository)

### Installation Steps

1. **Clone the Repository**:
    ```bash
    git clone <repository-url>
    cd seat_booking
    ```

2. **Create a Virtual Environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply Migrations**:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Run the Development Server**:
    ```bash
    python manage.py runserver
    ```
    The server will start on `http://127.0.0.1:8000/`.

## API Endpoints

### Venue Endpoints
- **GET /api/venues/**: List all venues.
- **POST /api/venues/**: Create a new venue.
- **GET /api/venues/{id}/**: Retrieve a specific venue by ID.
- **PUT /api/venues/{id}/**: Update a specific venue by ID.
- **DELETE /api/venues/{id}/**: Delete a specific venue by ID.

### Seat Endpoints
- **GET /api/seats/**: List all seats.
- **POST /api/seats/**: Create a new seat.
- **GET /api/seats/{id}/**: Retrieve a specific seat by ID.
- **PUT /api/seats/{id}/**: Update a specific seat by ID.
- **DELETE /api/seats/{id}/**: Delete a specific seat by ID.

### Booking Endpoints
- **GET /api/bookings/**: List all bookings.
- **POST /api/bookings/**: Create a new booking.
- **GET /api/bookings/{id}/**: Retrieve a specific booking by ID.
- **PUT /api/bookings/{id}/**: Update a specific booking by ID.
- **DELETE /api/bookings/{id}/**: Delete a specific booking by ID.

### Validation
- Bookings are validated to ensure that no seat can be double-booked. Attempting to book an already booked seat will result in a `400 Bad Request` response.

## Running Tests

To run the tests for this project, use the following command:

```bash
python manage.py test bookings
```

This will execute all tests defined in the `bookings/tests.py` file.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For any questions or feedback, please contact:

- **Jaman**: [zamaan.md19@gmail.com](mailto:zamaan.md19@gmail.com)
- **WhatsApp**: [+8801673850025](https://wa.me/8801673850025)

## Acknowledgements

- Thanks to the Django and Django REST Framework communities for their excellent tools and documentation.
- Special thanks to Interactive Cares for the opportunity to work on this task.

---
