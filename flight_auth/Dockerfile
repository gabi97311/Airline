# Используем легкий образ Python
FROM python:3.14-slim

# Рабочая папка внутри контейнера
WORKDIR /app

# Копируем список зависимостей и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем всё остальное
COPY . .

# Запускаем сервер
# Исправлено: main.py находится в корне, поэтому вызываем main:app вместо src.main:app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]