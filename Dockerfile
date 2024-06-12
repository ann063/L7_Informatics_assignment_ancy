# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run setup script to initialize the database
RUN python setup_db.py

# Make port 80 available to the world outside this container
EXPOSE 80

# Run ice_cream_shop.py when the container launches
CMD ["python", "ice_cream_shop.py"]
