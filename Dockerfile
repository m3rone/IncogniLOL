FROM alpine:latest

RUN apk update
RUN apk upgrade
RUN apk add python3

COPY requirements.txt .

ENV VENV_PATH=/root
RUN python3 -m venv ${VENV_PATH}
ENV PATH="$VENV_PATH/bin:$PATH"
RUN python3 -m ensurepip
RUN python3 -m pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD [ "python3", "start.py" ]
