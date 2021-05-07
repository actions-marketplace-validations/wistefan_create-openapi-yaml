# Create openapi.yaml github action

This action creates an [OpenAPI](https://swagger.io/specification/)-representation of a given [Smart-Data-Model](https://smartdatamodels.org/). The rest-path is based on the [NGSI-LD Specification](https://www.etsi.org/deliver/etsi_gs/CIM/001_099/009/01.04.02_60/gs_cim009v010402p.pdf).

The action will create the yaml-file inside github-workspace folder for further usage.

## Inputs

### `model-name`

**Required** Name of the model to be generated. Should be the folder that holds the model.yaml.

### `repository-name`

**Required** Name of the repository containing the model.

### `root-model-url`

**Required** Url of the root model. Default `"https://smart-data-models.github.io"`.

### `output-file-name`

**Required** Name of the file to be generated. Default `"swagger.yaml"`.


## Example usage

```yaml
uses: actions/create-openapi-yaml@v1
with:
  model-name: 'ACMeasurement'
  repository-name: 'dataModel.Energy'
```