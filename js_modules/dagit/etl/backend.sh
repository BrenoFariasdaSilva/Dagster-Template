#!/bin/bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

echo "Home brew configurado com sucesso!"

export PATH=/opt/homebrew/bin:$PATH

echo "Brew exportado com sucesso!"

brew install pyenv pyenv-virtualenv

echo "Brew instalou pyenv com sucesso!"

eval "$(pyenv init -)"

echo "Eval instalado com sucesso!"

eval "$(pyenv virtualenv-init -)"

echo "Eval instalado com sucesso!"

pyenv install 3.9.0

pip install jupyter

pip install notebook

pip install jupyterlab

pip install pandas

pip install seaborn

pip install boto3

pip install pdfkit

pip install ipykernel

pip install dagstermill==0.19.2

pip install dagster-graphql==1.3.2

pip install dagit==1.3.2

echo "Variavel de ambiente python instalado com sucesso!"

pyenv virtualenv 3.9.16 dagster39

echo "Variavel de ambiente virtual instalado com sucesso!"

pyenv activate dagster39

echo "Variavel de ambiente pyenv activate instalado com sucesso!"

brew install yarn

echo "Yarn instalado com sucesso!"

make dev_install

echo "Make instalado com sucesso!"

dagit -f hello-dagster.py

echo "Servidor backend ativo ...."
