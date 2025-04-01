FROM python:3.13

COPY main.py .
COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

CMD ["fastapi", "run", "main.py", "--port", "80"]