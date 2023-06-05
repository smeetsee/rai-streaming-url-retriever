FROM python:3.11-alpine

WORKDIR /opt/flask_app
RUN pip install flask requests
COPY flask_app.py get_video_url.py output_m3u.py /opt/flask_app/

ENTRYPOINT FLASK_APP=flask_app.py flask run --host=0.0.0.0