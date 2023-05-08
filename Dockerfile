FROM python:3.10

WORKDIR /test-app

COPY . .

RUN pip install pylint

ARG RUN_TIME
ARG TEST_TYPE
ARG TEST_SUITE_NAME
ARG NUM_USERS

RUN cat << 'EOF' > run-ui.sh \
&& pylint . \
--$TEST_TYPE=$TEST_SUITE_NAME \
--output-format=$NUM_USERS \
$RUN_TIME

CMD ./run-ui.sh
