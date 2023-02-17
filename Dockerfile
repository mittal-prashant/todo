FROM python:3.8-slim-buster
COPY . /todo
WORKDIR /todo
RUN pip install -r requirements.txt 
EXPOSE 5001
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]