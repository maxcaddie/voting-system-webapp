FROM python:3.8
# Install dependencies:
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the application:
COPY time_test.py .
COPY key.json .
COPY secrets.py .

#Run
ARG FLASK_APP=time_test.py

EXPOSE 5000

ENV FLASK_APP=time_test.py

CMD ["flask","run","--no-debugger","--host=0.0.0.0"]
