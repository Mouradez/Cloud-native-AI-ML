FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 8080

CMD ["uvicorn", "main:app", "--host", "localhost", "--port", "8080", "--reload"]
