from python:3.11-slim
label authors = "Mibsh"
copy requirements.txt .
run pip install --no-cache-dir -r requirements.txt
copy . .
cmd ["python3","main.py"]