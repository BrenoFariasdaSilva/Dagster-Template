# Author: Breno Farias da Silva
# Last update: 20/07/2023

# Set the pyenv environment where the commands will be executed:
export PYENV_VERSION=dagster

# Run all of the makefile rules:
all:
	dependencies dagster

# Install the external project dependencies (Not related to dagster, but to the model):
dependencies:
	clear;
	echo "Installing the external project dependencies...";
	python_dependencies database_module_dependencies 
	echo "External project dependencies installed!";

# Install the python dependencies:
python_dependencies:
	echo "Installing the python dependencies...";
	pip install pandas matplotlib seaborn scikit-learn
	echo "Python dependencies installed!";

# Install the dagster dependencies:
database_module_dependencies:
	echo "Installing the database module dependencies...";
	cd DataBaseModule;
	pip install -r requirements.txt;
	echo "Database dependencies installed!";

# Run the dagster project:
dagster:
	clear;
	echo "Running the dagster project...";
	dagster dev -h 0.0.0.0 -p 3000
