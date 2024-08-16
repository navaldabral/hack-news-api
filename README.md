---
## Installation

### Prerequisites

+ Python 3.11.1

+ MySQL database ver 8.0.32


## There are two types of installation: one is on a local system, and the other is using Docker.

### 1) Local System Setup
1. Clone the repository

    git clone https://github.com/navaldabral/hackernews-api.git

    cd hackernews-api-main
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

#### Hacker News 

<img width="1470" alt="Screenshot 2024-08-16 at 4 00 20 PM" src="https://github.com/user-attachments/assets/5865b04f-9c8e-423c-9f3f-7a3d6f8920be">

+ GET /top-news/

    Get a list of the top 10 default news items from Hacker News.

---

### Unit Tests

for the unit test, you run this command `pytest test_main.py`:

<img width="1470" alt="Screenshot 2024-08-15 at 3 15 50 PM" src="https://github.com/user-attachments/assets/4d2dd671-5e59-40cd-9be2-5b4fdb6d07c4">

---

### 2) Docker Setup

+ Pull the Docker Image

```bash
docker pull navaldabral/hackernews
```

+ Check the Pulled Image
  
```bash
docker images
```

+ Run the Docker Image

```bash
docker run -d -p 8000:8000 navaldabral/hackernews
```

+ Test the Application
  
  Open your web browser and go to http://localhost:8080

