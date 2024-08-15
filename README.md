---
## Installation

### Prerequisites

+ Python 3.11.1

+ MySQL database ver 8.0.32

### Setup
1. Clone the repository

    git clone https://github.com/navaldabral/articles.git

    cd articles
2. Create a virtual environment and activate it
   
   virtualenv venv

   source venv/bin/activate

3. Install the dependencies

    pip install -r requirements.txt

6. Run the application

    uvicorn main:app --reload

7. To access the APIs visit this URL http://127.0.0.1:8000/docs

---

### Endpoints

#### Articles

<img width="1470" alt="Screenshot 2024-06-20 at 10 01 32 AM" src="https://github.com/navaldabral/articles/assets/29625991/04952e4e-b443-403a-9786-a82b3b3b10a0">

+ GET /api/articles/

    Retrieve a list of articles. Supports filtering by author and keyword, and sorting.

---

### Unit Tests

for the unit test, you run this command `pytest test_main.py`:

<img width="1470" alt="Screenshot 2024-06-20 at 10 06 17 AM" src="https://github.com/navaldabral/articles/assets/29625991/4b0a0d7d-999d-4100-a350-06bdb3ae6003">

---
