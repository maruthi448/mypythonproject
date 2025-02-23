#Python version
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy project files
COPY . /app

#Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
# Expose the FastAPI port

EXPOSE 8081

# Run the FastAPI app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8081", "--reload" ]