# Person API

This is a simple REST API for managing person records.

## Setup Instructions

1. Clone this repository.

```bash
git clone https://github.com/JoelInyang/HNG-StageTwo.git
cd StageTwo

python -m venv venv
source venv/bin/activate for linux/mac OS, or use venv\Scripts\activate for Windows
pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate


python manage.py runserver

The API will be available at http://localhost:8000/api/persons/.
he API will be available at http://localhost:8000/api/persons/.he API will be available at http://localhost:8000/api/persons/.
