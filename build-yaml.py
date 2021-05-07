# Generates the swagger.yaml for the given data model

import yaml
import os
import json


def read_yaml(fileUrl):

    file = open(fileUrl, "r")
    return yaml.safe_load(file.read())

dataModel = os.environ['DATA_MODEL']
repoName = os.environ['REPOSITORY_NAME']
rootModelUrl = os.environ['ROOT_MODEL_URL']

modelFolder=os.environ['REPO_FOLDER'] + "/" + dataModel
modelYaml = modelFolder + "/model.yaml"
outputFile = modelFolder + "/" + os.environ['OUTPUT_FILENAME']



print(dataModel + " " + repoName + " " + rootModelUrl)
modelDict = read_yaml(modelYaml)
print(type(modelDict))

swaggerHeader = """---
# Copyleft (c) 2021 Contributors to Smart Data Models initiative
# """
swaggerBody = f"""paths: 
  /ngsi-ld/v1/entities: 
    get: 
      description: "Retrieve a set of entities which matches a specific query from an NGSI-LD system"
      parameters: 
        - in: query
          name: type
          required: true
          schema: 
            enum: 
              - {dataModel}
            type: string
      responses: 
        "200": 
          content: 
            application/ld+json: 
              examples: 
                keyvalues: 
                  summary: "Key-Values Pairs"
                  value: 
                    - $ref: "{rootModelUrl}/{repoName}/{dataModel}/examples/example.json"
                normalized: 
                  summary: "Normalized NGSI-LD"
                  value: 
                    - $ref: "{rootModelUrl}/{repoName}/{dataModel}/examples/example-normalized.jsonld"
          description: OK
      tags: 
        - ngsi-ld
        - {dataModel}
tags: 
  - description: "NGSI-LD Linked-data Format"
    name: ngsi-ld
  - description: "{modelDict[dataModel]["description"]}"
    name: {dataModel}"""

tab = "  "
nl = chr(10)
swaggerContent = swaggerHeader + nl
swaggerContent += nl
swaggerContent += nl
swaggerContent += "components:" + nl
swaggerContent += 1 * tab + "schemas: " + nl
swaggerContent += 2 * tab + dataModel + ": " + nl
swaggerContent += 3 * tab + "$ref: " + chr(34) + rootModelUrl + repoName + "/" + dataModel + "/" + modelYaml + "#/" + dataModel + chr(34) + nl
swaggerContent += "info:" + nl
swaggerContent += 1 * tab + "description:  |" + nl
if "description" in modelDict[dataModel]:
    swaggerContent += 2 * tab + modelDict[dataModel]["description"] + nl
swaggerContent += 1 * tab + "title: " + dataModel + nl
swaggerContent += 1 * tab + "version: " + chr(34) + "1.0.0" + chr(34) + nl
swaggerContent += "openapi: " + chr(34) + "3.0.0" + chr(34) + nl
swaggerContent += nl

for line in swaggerBody.splitlines():
    print(line)
    swaggerContent += line + nl
print(swaggerContent)
with open(outputFile, "w") as output:
    output.write(swaggerContent)