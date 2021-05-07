FROM python:3.9.5

ENV DATA_MODEL
ENV REPOSITORY_NAME
ENV ROOT_MODEL_URL
ENV REPO_FOLDER
ENV MODEL_FOLDER=${REPO_FOLDER}/${DATA_MODEL}
ENV OUTPUT_FILENAME

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["build-yaml.py"]

ENTRYPOINT ["python3"]