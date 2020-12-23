FROM python:3.8
WORKDIR /code
COPY . .
CMD ["python","-u","example2.py"]

