# PlayHub 

A web application built with Django for browsing video games. The system features a database connecting Games, Developers, and Genres.

## Live Demo
The project is deployed on Render:
**[https://playhub-v10w.onrender.com](https://playhub-v10w.onrender.com)**

---

##  Access Credentials
You can register a new account or use the test credentials below to explore the features immediately:

Username: testplayhub

Password: test12345

---

## Key Features
* **User Authentication:** Complete Sign up, Login, and Logout functionality.
* **Dynamic Content:** Browse games by genres, developers, and view detailed information.
* **Database Structure:** Implements complex relationships:
    * *One-to-Many* for Developers.
    * *Many-to-Many* for Genres and User Libraries.
* **Responsive UI:** Interface built with Bootstrap, fully responsive for different devices.

---

## Database Structure
The application handles connections between Games, Genres, and Developers using the following topology:

![Database Schema](https://github.com/user-attachments/assets/61121222-0888-494f-a05e-a99c3da104d0)

---

## Screenshots

### 1. Main Page & Game List
![Main Page](https://github.com/user-attachments/assets/7b58ebab-aaaf-46b4-ac1a-8f026d4d1bf7)
![Game List](https://github.com/user-attachments/assets/edd4030b-08db-4f86-b949-1479e2802644)

### 2. Game Details
![Game Detail](https://github.com/user-attachments/assets/bc3feebe-9767-4faf-91bd-c31a2d0d044c)

### 3. Developers
![Developer List](https://github.com/user-attachments/assets/0add5fac-4147-4005-b095-6162377359a4)
![Developer Detail](https://github.com/user-attachments/assets/6947e019-01c6-4815-ae73-c1314597fa05)

### 4. Authentication (Login / Register / Logout)
![Login](https://github.com/user-attachments/assets/77c8964e-e25a-4722-9928-2e6322b750e1)
![Registration](https://github.com/user-attachments/assets/37995326-0610-4524-887f-75c70abf8a98)
![Logout](https://github.com/user-attachments/assets/0a9f515a-7f30-49cd-a2b7-9c2def6a9c2e)

---

## Tech Stack
* **Backend:** Python, Django
* **Database:** PostgreSQL (Neon), SQLite (Dev)
* **Frontend:** HTML5, CSS3, Bootstrap
* **Deployment:** Render

---

## Local Installation

If you want to run this project locally:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/nastyagst/playhub.git](https://github.com/nastyagst/playhub.git)
    cd playhub
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv .venv
    # Windows
    .venv\Scripts\activate
    # macOS/Linux
    source .venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up environment variables:**
    Create a `.env` file in the root directory and add your `SECRET_KEY`.

5.  **Run migrations:**
    ```bash
    python manage.py migrate
    ```

6.  **Run the server:**
    ```bash
    python manage.py runserver
    ```