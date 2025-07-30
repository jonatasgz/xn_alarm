FROM python:3.13-slim

WORKDIR /usr/src/app
COPY . .
RUN pip install --no-cache-dir gradio
EXPOSE 7865
ENV GRADIO_SERVER_NAME="0.0.0.0"

CMD ["python", "app.py"]