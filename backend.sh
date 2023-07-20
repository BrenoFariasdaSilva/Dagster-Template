#!/bin/bash -i

pyenv install 3.7.17

echo "Python 3.7.17 instalado com sucesso"

pyenv virtualenv 3.7.17 dagster

eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

pyenv activate dagster

brew install yarn

make dev_install

echo "Make instalado com sucesso!"

dagster dev -h 0.0.0.0 -p 3000

echo "Servidor backend ativo ...."
