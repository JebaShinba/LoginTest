# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set environment variables to disable buffering of stdout and stderr
ENV PYTHONUNBUFFERED 1

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install system dependencies required for MongoDB, Selenium, and Chrome
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    unzip \
    gnupg \
    ca-certificates \
    libnss3 \
    libxss1 \
    libappindicator3-1 \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libx11-xcb1 \
    libgbm1 \
    libgdk-pixbuf2.0-0 \
    libx11-dev \
    && apt-get clean

# Install Chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome-stable_current_amd64.deb || apt-get install -f -y

# Install ChromeDriver (Required for Selenium)
RUN wget -q https://chromedriver.storage.googleapis.com/112.0.5615.49/chromedriver_linux64.zip
RUN unzip chromedriver_linux64.zip -d /usr/local/bin
RUN chmod +x /usr/local/bin/chromedriver

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Install MongoDB tools (Optional, required for MongoDB interactions)
RUN curl -fsSL https://www.mongodb.org/static/pgp/server-4.4.asc | tee /etc/apt/trusted.gpg.d/mongodb.asc
RUN echo "deb [ arch=amd64 ] https://repo.mongodb.org/apt/ubuntu $(lsb_release -cs)/mongodb-org/4.4 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-4.4.list
RUN apt-get update
RUN apt-get install -y mongodb-org-tools

# Command to run your test (adjust as necessary for your entry point)
CMD ["python", "-m", "unittest", "discover", "-s", "login_testcases", "-p", "valid.py"]
