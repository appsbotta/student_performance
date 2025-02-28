import os

dirs = [
    "src",
    'research',
    'model',
    'templates',
    'artifacts'
]

for dir in dirs:
    os.makedirs(dir,exist_ok=True)
    with open(os.path.join(dir,'.gitkeep'),'w') as f:
        pass