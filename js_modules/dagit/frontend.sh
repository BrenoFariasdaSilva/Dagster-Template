#!/bin/bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

echo "Home brew configurado com sucesso!"

export PATH=/opt/homebrew/bin:$PATH

echo "Brew exportado com sucesso!"

brew install yarn

echo "Yarn instalado com sucesso!"

yarn install

make dev_webapp

echo "Servidor frontend ativo ...."
