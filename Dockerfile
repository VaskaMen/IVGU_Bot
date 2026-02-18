from python:3.11-slim
label authors = "Mibsh"
copy requirements.txt .
run pip install --no-cache-dir -r requirements.txt
copy . .
ENV IVGU_EMAIL== example.mail.ru
ENV IVGU_PASSWORD== password
ENV TELEGRAM_TOKEN== token
ENV POSTGRES_PASSWORD== postgres
ENV SERVER_IP== localhost
ENV DATABASE_NAME== ivgu
ENV USER_NAME== postgres
ENV DATABASE_PORT== 5432
cmd ["python3","main.py"]