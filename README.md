## Setup Instructions

1. Clone the repository:
    ```
    git clone <repository_url>
    ```

2. Navigate to the project directory:
    ```
    cd project_directory
    ```

3. Create a virtual environment:
    ```
    python -m venv venv
    ```

4. Activate the virtual environment:
    ```
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

5. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

6. Apply migrations:
    ```
    python manage.py migrate
    ```

7. Run the server:
    ```
    python manage.py runserver
    ```

8. Open your browser and navigate to `http://127.0.0.1:8000/`.

## Features

- Add authors
- Add books
- Add borrow records
- View paginated lists of authors, books, and borrow records
- Export data to an Excel file

## Technologies Used

- Django
- HTML, CSS
- SQLite

## Contact

For any inquiries or support, please contact [adhirajsingh3103@example.com].
