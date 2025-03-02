# End to End ML Project (student_performance)

## workflow
1. created setup.py, template.py and requirements.txt

2. Created custom exception in exception.py and logger.py and a function to read yaml

3. created EDA and Model trainer in research

4. Add new config.yaml file and done data_ingestion

5. Completed data transformation

6. Model Training

7. Created the prediction pipeline and the Flask app

8. Created .ebextensions for deployment

9. create .github actions

10. create ECR repo and save the repo uri 

11. create a ec2 instance 

12. Create a iam user and save a access key

13. In github, in settings under action/runner create a new runner.
        a. while running the cmds in order when asked for runner group keep it default but for runner name use self-hosted

14. Create Secret keys in github which are in workflow

## Docker Setup In EC2 commands to be Executed
#optinal
1. sudo apt-get update -y

2. sudo apt-get upgrade

#required

1. curl -fsSL https://get.docker.com -o get-docker.sh

2. sudo sh get-docker.sh

3. sudo usermod -aG docker ubuntu

4. newgrp docker 

## To run 
1. Create a virtual env and activate it
```bash
conda create -p env python y
conda activate /path/to/env
```

2. Install requirements.txt
```bash
pip install -r requirements.txt
```