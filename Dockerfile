FROM python:3.13

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt


COPY wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh


COPY . /app/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
