FROM python:3.9.5

ENV DATA_MODEL="dataModel"
ENV REPOSITORY_NAME="dataModelRepository"
ENV ROOT_MODEL_URL="https://smart-data-models.github.io"
ENV REPO_FOLDER="/github/workspace"
ENV MODEL_FOLDER=${REPO_FOLDER}/${DATA_MODEL}
ENV OUTPUT_FILENAME="openapi.yaml"

WORKDIR ${REPO_FOLDER}

COPY . .

RUN pip install --no-cache-dir -r requirements.txt
RUN chmod +rwx build-yaml.py

RUN ls -l

CMD ["build-yaml.py"]

ENTRYPOINT ["python3"]