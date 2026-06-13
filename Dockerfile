# 1. Base Python image
FROM python:3.12

# 2. Set working directory inside container
WORKDIR /app

# 3. Copy project files into container
COPY . .

# 4. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Run FastAPI app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]