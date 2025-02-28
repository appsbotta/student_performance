import os

dirs = [
    "src",
    'research',
    'model',
    'templates',
    'artifacts',
    os.path.join('src','components'),
    os.path.join('src','pipeline'),
]

for dir in dirs:
    os.makedirs(dir,exist_ok=True)
    with open(os.path.join(dir,'.gitkeep'),'w') as f:
        pass

files = [
    os.path.join('src','__init__.py'),
    os.path.join('src','logger.py'),
    os.path.join('src','exception.py'),
    os.path.join('src','utils.py'),
    os.path.join('src/components','__init__.py'),
    os.path.join('src/components','data_ingestion.py'),
    os.path.join('src/components','data_transforamtion.py'),
    os.path.join('src/components','model_trainer.py'),
    os.path.join('src/pipeline','__init__.py'),
    os.path.join('src/pipeline','prediction_pipeline.py'),
    os.path.join('src/pipeline','train_pipeline.py'),
]

for file in files:
    if not os.path.exists(file):
        with open(file,'w') as f:
            pass