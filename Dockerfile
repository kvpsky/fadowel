FROM python:3.13
WORKDIR /app
COPY ./src /app/src
RUN pip install --no-cache-dir --upgrade -r /app/src/requirements.txt
EXPOSE 8080
CMD ["fastapi", "run", "/app/src/main.py", "--port", "8080"]
