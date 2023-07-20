#!/bin/bash -i

# prequisitos
# 1) pyenv
# 2) homebrew
# 3) node v14

# dependencias
sudo apt install git file procps make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev curl -y

### 1) pyenv
if [ ! -r ~/.pyenv/ ]
then
    git clone https://github.com/pyenv/pyenv.git ~/.pyenv
    git clone https://github.com/pyenv/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv
    echo '
# pyenv
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
if command -v pyenv 1>/dev/null 2>&1; then
    eval "$(pyenv init -)"
    eval "$(pyenv virtualenv-init -)" # Enable auto-activation of virtualenvs
fi' >> ~/.bashrc
    source ~/.bashrc
fi

## 2) homebrew
/bin/bash -c "$(sudo curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" </dev/null

(echo; echo 'eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"') >> ~/.bashrc
source ~/.bashrc

# 3) node
curl -sL https://deb.nodesource.com/setup_14.x | sudo bash -
sudo apt -y install nodejs
npm install  jest

source ~/.bashrc
exec "$SHELL"
