# Use the official Python 3.9 image as the base image
FROM python:3.9-buster

# Set the working directory inside the container
WORKDIR /app

# Copy the Python package requirements file to the working directory
COPY requirements.txt .

# Install Python dependencies using pip (without caching)
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the application code to the working directory
COPY . .

# Set an environment variable to configure Flask to listen on all interfaces
ENV FLASK_RUN_HOST=0.0.0.0

# Expose port 5000 for incoming connections (documentary, does not publish the port)
EXPOSE 5000

# Define the command to run when the container starts (start the Flask application)
CMD ["flask", "run"]
