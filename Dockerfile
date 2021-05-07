FROM python:3.9.5

ENV DATA_MODEL="dataModel"
ENV REPOSITORY_NAME="dataModelRepository"
ENV ROOT_MODEL_URL="https://smart-data-models.github.io"
ENV REPO_FOLDER="/github/workspace"
ENV OUTPUT_FILENAME="openapi.yaml"

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["/usr/src/app/build-yaml.py"]

ENTRYPOINT ["python3"]