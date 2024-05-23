# Subscription
# TheGaius
My Django Project 
## Table of Contents 
This Project contains the code  
# Features
- User Authentication
- Staff and Admin Priviledges 
- Pay for a subscription
-To be continued

## Setup Instructions

To get started with this project, follow these steps:

1. **Clone the repository:**

    ```sh
    git clone https://github.com/oseni99/TheGaius.git
    cd feedback
    ```

2. **Create and activate a virtual environment:**

    ```sh
    # On Windows
    python -m venv venv
    .\venv\Scripts\activate

    # On macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Apply the migrations:**

    ```sh
    python manage.py migrate
    ```

5. **Create a superuser:**

    ```sh
    python manage.py createsuperuser
    ```

6. **Run the development server:**

    ```sh
    python manage.py runserver
    ```

7. **Access the application:**

    Open your web browser and go to `http://127.0.0.1:8000/`.
