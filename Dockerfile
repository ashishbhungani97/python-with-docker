FROM python:3

# set the working directory
WORKDIR /code

# install dependencies
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip install -r requirements.txt

# copy the src to the folder
COPY . .

# Expose the port the app   
# will listen on
EXPOSE 5000

# start the server
CMD ["python", "main.py"]