
# Python support can be specified down to the minor or micro version
# (e.g. 3.6 or 3.6.3).
# OS Support also exists for jessie & stretch (slim and full).
# See https://hub.docker.com/r/library/python/ for all supported Python
# tags from Docker Hub.
FROM python:3.6-slim

# If you prefer miniconda:
#FROM continuumio/miniconda3

# LABEL Name=dsjose Version=0.0.1
EXPOSE 3000 5050

ENV INSTALL_PATH /app
ENV FLASK_APP ./app/app.py
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY requirements.txt requirements.txt

# Using pip:
RUN pip install -r requirements.txt
# CMD ["python3", "-m", "app/app"]
COPY . .

# Using pipenv:
#RUN python3 -m pip install pipenv
#RUN pipenv install --ignore-pipfile
#CMD ["pipenv", "run", "python3", "-m", "dsjose"]

# Using miniconda (make sure to replace 'myenv' w/ your environment name):
#RUN conda env create -f environment.yml
#CMD /bin/bash -c "source activate myenv && python3 -m dsjose"
