FROM osgeo/gdal:ubuntu-small-3.8.4

WORKDIR /app

RUN apt-get update && apt-get install -y python3-pip

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY main.py .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
