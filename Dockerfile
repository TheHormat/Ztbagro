FROM python:3.10

ENV PYTHONUNBUFFERED 1
ENV APP_ROOT /code

ADD requirements.txt /requirements.txt

RUN pip3 install virtualenvwrapper
RUN python3 -m venv /venv
RUN /venv/bin/pip3 install -U pip
RUN /venv/bin/pip3 install --no-cache-dir -r /requirements.txt

RUN mkdir ${APP_ROOT}
WORKDIR ${APP_ROOT}
ADD . ${APP_ROOT}

EXPOSE 8000

ENTRYPOINT ["bash", "/code/entrypoint.sh"]
