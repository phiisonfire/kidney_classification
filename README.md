# kidney_classification
# How to run?
### STEPS 0:

Clone the repository

```bash
$ git clone https://github.com/phiisonfire/kidney_classification.git
```

### STEP 1 - Create a conda environment after opening the repository

```bash
$ conda create -p kidney python=3.11 -y
$ conda activate kidney
```

### STEP 2 - Install the requirements
```bash
$ pip install -r requirements.txt
```

## Project workflows
1. Update config.yaml
2. Update secrets.yaml [Optional] (like database, user information, etc.)
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src/config
6. Update the components: data ingestion, model preparations, model trainer, model evaluation, ...
7. Update the pipeline: training pipeline, prediction pipeline
8. Update the main.py: endpoint
9. Update dvc.yaml
10. Update app.py (Flask app)

## Personal notes
1. `config/config.yaml` holds configuration variables of components, so I won't have to hard code them inside the component
2. `ConfigBox`
```python
from box import ConfigBox # helps accessing values of dictionary easier. Detailed in experiments.ipynb.
```
3. `@ensure_annotations`
```python
from ensure import ensure_annotations # decorator makes sure that the arguments and returned values are as my expected data type. Detailed in experiments.ipynb.
```