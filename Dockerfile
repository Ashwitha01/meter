FROM python:3.8-alpine3.10
COPY . /app
COPY requirements.txt /requirements.txt 
RUN pip install --no-cache-dir -r requirements.txt
WORKDIR /app
CMD ["python", "-/main.py"]