FROM python:3

WORKDIR /scripts

RUN pip install pipenv

COPY ./Pipfile ./Pipfile.lock /
RUN pipenv install --system

COPY ./main.py /scripts/main.py

CMD [ "python", "/scripts/main.py" ]
