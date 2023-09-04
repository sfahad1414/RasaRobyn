FROM python:3.10-slim-bookworm

WORKDIR /app
RUN python -m pip install --upgrade pip
COPY requirements.txt .
RUN python -m pip install -r requirements.txt
COPY models models
RUN app.py .
RUN ls

CMD python app.py