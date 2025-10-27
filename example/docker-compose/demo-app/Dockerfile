FROM python:3.10-slim

WORKDIR /app
RUN pip install flask prometheus-client
COPY app.py .

EXPOSE 8000
CMD ["python", "app.py"]
