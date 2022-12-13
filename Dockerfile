
FROM python:3-slim

WORKDIR /usr/src/app

COPY source/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt -i https://mirror.baidu.com/pypi/simple 

COPY source/ .

EXPOSE 5000
CMD [ "python", "./app.py" ]
