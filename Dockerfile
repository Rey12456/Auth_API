FROM python:3.10.13-alpine3.18
WORKDIR /app
COPY . /app
COPY db.sqlite3 /app  
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 9000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9000"]  