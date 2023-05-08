FROM python:3.10

WORKDIR /test-app

COPY . .

RUN pip install pylint

ARG RUN_TIME
ARG TEST_TYPE
ARG TEST_SUITE_NAME
ARG NUM_USERS

RUN echo $'#!/bin/bash \
pylint . \
--$TEST_TYPE=$TEST_SUITE_NAME \
--output-format=$NUM_USERS \
$RUN_TIME' > run-ui.sh

RUN ["chmod", "+x", "run-ui.sh"]

CMD ["sh", "./run-ui.sh"]
