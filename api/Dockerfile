FROM python:3.8
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
RUN python manage.py migrate
# RUN python manage.py loaddata short_url/fixtures/default.json
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]