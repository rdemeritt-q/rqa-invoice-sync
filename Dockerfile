ARG BASE_IMAGE
FROM ${BASE_IMAGE}
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --require-hashes -r requirements.txt
COPY app ./app
CMD ["python", "-m", "app.main"]
