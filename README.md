<div align="center">
  
# [Dagster - Template Model.](https://github.com/BrenoFariasdaSilva/Dagster-Template) <img src="https://github.com/BrenoFariasdaSilva/Dagster-Template/blob/main/.assets/Dagster.svg"  width="11%" height="11%">

</div>

<div align="center">
  
---
  
This repository is a translation of a Jupyter notebook model_name model to Dagster, in which uses Dagster 1.3.11 and Python 3.7.17.

---
  
</div>

<div align="center">
  
---
  
Dagster is a data orchestrator for machine learning, analytics, and ETL. It lets you define pipelines in terms of the data flow between reusable, logical components, then test locally and run anywhere. With a unified view of pipelines and the assets they produce, Dagster can schedule and orchestrate Pandas, Spark, SQL, or anything else that Python can invoke. It abstracts away the infrastructure details and job execution, so that you can focus on what matters: building data applications. For more information, please visit the [Dagster website](https://dagster.io/).

---
  
</div>

<div align="center">

![GitHub Code Size in Bytes](https://img.shields.io/github/languages/code-size/BrenoFariasdaSilva/Dagster-Template)
![GitHub Last Commit](https://img.shields.io/github/last-commit/BrenoFariasdaSilva/Dagster-Template)
![GitHub](https://img.shields.io/github/license/BrenoFariasdaSilva/Dagster-Template)
![wakatime](https://wakatime.com/badge/github/BrenoFariasdaSilva/Dagster-Template.svg)

</div>

<div align="center">
  
![RepoBeats Statistics](https://repobeats.axiom.co/api/embed/a681afdffa4460fc93f814d6a0cd3349fb79634f.svg "Repobeats analytics image")

</div>

## Table of Contents:
- [Dagster - Template Model. ](#dagster---template-model-)
  - [Table of Contents:](#table-of-contents)
  - [Project Files Structure:](#project-files-structure)
  - [Install Dependencies:](#install-dependencies)
    - [Pre-requisites:](#pre-requisites)
    - [Backend:](#backend)
    - [Model Dependencies:](#model-dependencies)
  - [How to Run:](#how-to-run)
  - [Contributing](#contributing)
  - [License](#license)



## Project Files Structure:
There are two levels of folders in this project. The first level is the project folder (root), and the second level is the Dagster folder (translated model). The project folder contains the files that are related setting up the python to a specific version (3.7.17) and dagster depencies. The Dagster folder contains the files that are related to Dagster project. Each folder level have a README.md file and a Makefile file.

## Install Dependencies:
### Pre-requisites:
First you need to run the `prerequisites.sh` file to install the project dependencies, such as `python`, `homebrew` and `node`. This file will install the `pyenv` and `pyenv-virtualenv` to manage the Python versions and virtual environments. The `homebrew` will be installed as package manager for the dagster packages. Lastly, the `node` is installed for the use of the website, in which we will have the dagster UI.

```shell
chmod +x ./prerequisites.sh # Gives execution permission to the file
./prerequisites.sh # Installs project pre requisites, such as pyenv, homebrew and node.
```

### Backend:
Now you need to run the `backend.sh` file (also located in the root directory of the project), which will create the python virtual environment and install the dagster packages, install `yarn`, the python modules and `dagit` (dagster UI).
```shell
chmod +x ./backend.sh # Gives execution permission to the file
./backend.sh # Installs project dependencies, such as python 3.7.17, dagster packages, yarn, python modules and dagit.
```
Great, the dagster dependencies are installed. Now we need to install the project/model dependencies, located in `Model/` folder.

### Model Dependencies:
Now that you have Python 3.7.17 installed, the Dagster dependencies and the pyenv virtual environment created, open a new terminal in the `Model/` folder and execute the following makefile rule:

```shell
cd Model # Enters the project folder
make dependecies # Install the project dependencies, such as:
# Install Python dependencies of the model -> pandas, matplotlib, seaborn and scikit-learn.
# Install the database module dependencies -> psycopg2-binary and sqlalchemy, etc.
# Install Docker and Docker-Compose.
# Build the docker-compose.
```
Now you have the project dependencies installed. Let's run the model.
## How to Run:
At this point, you can simply run the following command to run the model:
```shell
make dagster # Run the dagster model
```
This will run the dagster dev command, which will be executed on port 3000 and receive requests from any host. You can access the dagster UI by accessing the following link: http://localhost:3000.

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**. If you have suggestions for improving the code, your insights will be highly welcome.
In order to contribute to this project, please follow the guidelines below or read the [CONTRIBUTING.md](CONTRIBUTING.md) file for more details on how to contribute to this project, as it contains information about the commit standards and the entire pull request process.
Please follow these guidelines to make your contributions smooth and effective:

1. **Set Up Your Environment**: Ensure you've followed the setup instructions in the [Setup](#setup) section to prepare your development environment.

2. **Make Your Changes**:
   - **Create a Branch**: `git checkout -b feature/YourFeatureName`
   - **Implement Your Changes**: Make sure to test your changes thoroughly.
   - **Commit Your Changes**: Use clear commit messages, for example:
     - For new features: `git commit -m "FEAT: Add some AmazingFeature"`
     - For bug fixes: `git commit -m "FIX: Resolve Issue #123"`
     - For documentation: `git commit -m "DOCS: Update README with new instructions"`
     - For refactorings: `git commit -m "REFACTOR: Enhance component for better aspect"`
     - For snapshots: `git commit -m "SNAPSHOT: Temporary commit to save the current state for later reference"`
   - See more about crafting commit messages in the [CONTRIBUTING.md](CONTRIBUTING.md) file.

3. **Submit Your Contribution**:
   - **Push Your Changes**: `git push origin feature/YourFeatureName`
   - **Open a Pull Request (PR)**: Navigate to the repository on GitHub and open a PR with a detailed description of your changes.

4. **Stay Engaged**: Respond to any feedback from the project maintainers and make necessary adjustments to your PR.

5. **Celebrate**: Once your PR is merged, celebrate your contribution to the project!

## License
This project is licensed under the [Creative Commons Zero v1.0 Universal](LICENSE), which means you are free to use, modify, and distribute the code. See the [LICENSE](LICENSE) file for more details.
