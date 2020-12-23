FROM python:3.8
WORKDIR /code
COPY . .
CMD ["python","example2.py"]

