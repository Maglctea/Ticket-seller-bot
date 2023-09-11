FROM python:3-slim
WORKDIR /bot
COPY . .
RUN pip3 install -r requirements.txt
CMD python3 -m bot