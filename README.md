
#  Installation Steps

1. Download the git repo via command :

	```bash
	git clone https://github.com/kartikjoshi267/myGNN.git
	```

	Later go to the folder myGNN by command:
	```bash
	cd myGNN
	```

2. Create a python 3 virtual environment to run. Command:
	```bash
	virtualenv major_project_env
	```

	If virtual environment is not installed in the system follow the following steps first:
	```bash
	pip install virtualenv
	```

3. Activate the environement using the command:

	```bash
	source ./major_project_env/bin/activate
	```
  

4. Once the virtual environement is setup, install the dependencies.
Command: 	
	```bash
	pip3 install -r requirements.txt
	```

5. To run the training program use command:

	```bash
	python ./src/main.py
	```

6. The output wil be stored in the outputFiles folder.