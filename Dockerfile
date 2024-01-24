# Use the official Python image
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the .env file to the working directory
COPY .env .

# Copy the content of the local src directory to the working directory
COPY . .

# Expose port 8002 for the Flask app
EXPOSE 8002

# Start server
CMD ["python", "app.py"]
