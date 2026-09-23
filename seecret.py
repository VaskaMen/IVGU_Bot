import os

email = os.getenv("IVGU_EMAIL","miha2204n@gmail.com")
password = os.getenv("IVGU_PASSWORD","8azr25pb")
token = os.getenv("TELEGRAM_TOKEN","7665754490:AAH7ugdV42S3Vxlm6sUZjnY2GwKh800xRRM")
password_postgres = os.getenv("POSTGRES_PASSWORD","POSTGRES")
server_ip = os.getenv("SERVER_IP", "localhost")
database = os.getenv("DATABASE_NAME","ivgu")
user_name = os.getenv("USER_NAME","postgres")
port = os.getenv("DATABASE_PORT",4188)