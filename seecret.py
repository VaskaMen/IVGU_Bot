import os

email = os.getenv("IVGU_EMAIL","example.mail.ru")
password = os.getenv("IVGU_PASSWORD","password")
token = os.getenv("TELEGRAM_TOKEN","token")
password_postgres = os.getenv("POSTGRES_PASSWORD","postgres")
server_ip = os.getenv("SERVER_IP", "localhost")
database = os.getenv("DATABASE_NAME","ivgu")
user_name = os.getenv("USER_NAME","postgres")
port = os.getenv("DATABASE_PORT",5432)