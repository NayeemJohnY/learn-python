FROM python:3.10

WORKDIR /test-app

COPY . .

RUN pip install pylint

ARG RUN_TIME
ARG TEST_TYPE
ARG TEST_SUITE_NAME
ARG NUM_USERS

RUN cat << 'EOF' > run-ui.sh \
&& EXTRA_PARAMS="" \
&& if [[ "$RUN_TIME" != "" ]]; then EXTRA_PARAMS+=" --reports "$RUN_TIME""; else EXTRA_PARAMS+=" --reports n"; fi \
&& pylint . \
--"$TEST_TYPE" "$TEST_SUITE_NAME" \
--output-format:"$NUM_USERS" \
${EXTRA_PARAMS} \

CMD run-ui.sh
