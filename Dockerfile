FROM python:3.10

WORKDIR /test-app

COPY . .

RUN pip install pylint

CMD ["pylint" , " ." ," --reports=y" , "--recursive=y" ,"--output-format=text", "--fail-under", "2"]
