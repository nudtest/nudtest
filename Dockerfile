FROM python:alpine3.7

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

EXPOSE 8080

ENTRYPOINT [ "python" ]

CMD [ "helloworld.py" ]
