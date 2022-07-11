# flowui_example_project
A basic FlowUI project should be structured in the following way:
```
/dependencies
/operators
config.ini
```


# Operators
The `/operators` folder should contain your customized Operators. Each Operator should follow a standard organization and contain certain information to be able to be found and used by your deployed FlowUI instance. Example:
```
/operators
..../ExampleOperator
......../metadata.json
......../model.py
......../operator.py
```
<br>

### metadata.json
The simplest `metadata.json` file should contain basic metadata related to the Operator ans also optional style configurations for the UI node. Example:
```
{
    "name": "ExampleOperator"
    "version": "0.1.0"
    "dependency": {
        "docker_base_image": "default",
        "dockerfile": "default",
        "requirements_file": "requirements_1.txt"
    },
    "style": {**style_args},
    "form": {**form_schema}  # THIS WILL BE AUTO-GENERATED
}
```
<br>

### model.py
Contains the Pydantic model which defines the the input arguments types for the Operator. Example:
```
from pydantic import BaseModel, Field


class OperatorModel(BaseModel):
    """Bandpass filter"""

    argument_1: float = Field(
        default=1.,
        description="an argument of numeric type",
    )
    argument_2: str = Field(
        default="default",
        description="an argument of string type"
    )
    argument_3: bool = False

    class Config:
        title = "ExampleOperator"
```
<br>

### operator.py
Contains the logic to run your custom code. The Operator you're writing comes here, and it should inherit from FlowUI `BaseOperator`. Example:
```
from flowui.base_operator import BaseOperator
from .model import OperatorModel


class ExampleOperator(BaseOperator):

    def operator_function(self, operator_model: OperatorModel):
        # Your custom function code comes here
```
<br>


# Dependencies
The `/dependencies` folder should contain all `requirements.txt` and `Dockerfile` (optional) files that will be used to define the dependencies and to build the containers that will run your custom Operators. Example:

```
/containers
..../Dockerfile_1
..../Dockerfile_2
..../requirements_1.txt
..../requirements_1.txt
```

<br>

# config.ini
The `config.ini` file stores the configuration variables for the project.


# Files automatically generated by FlowUI
When using FlowUI convenience CLI functions to prepare your code repository to run, some files will be automatically created or modified for you:
- A `dependencies_map.json` file will be created at `/depedencies`
- The `metadata.json` files for each Operator will be updated with information about their data input schema
- A `docker-compose.yaml` file will be created at the root path (only for local deploy)