FROM python:3.11

WORKDIR /app
COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install --upgrade aiohttp


COPY . .

CMD ["python", "-m", "Ashu"]