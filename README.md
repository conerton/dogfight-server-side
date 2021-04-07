# dogfight-server-side
The Back-End Capstone for https://github.com/conerton/dogfight client.

Installations
Python on Windows Subsystem for Linux

sudo apt update sudo apt install -y gcc make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl python3 python3-pip

Homebrew /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

Python on Mac xcode-select --install

Pyenv and Python on Mac brew install pyenv pyenv install 3.9.1 pyenv global 3.9.1

Pipenv 3rd Party Tool pip3 install --user pipenv

If you get command not found: pipenv when trying to run pipenv:

Mac and Linux

Open ~/.zshrc and add: export PIPENV_DIR="$HOME/.local" export PATH="$PIPENV_DIR/bin:$PYENV_ROOT/bin:$PATH"
Windows

First run python -m site --user-site
Copy what that returns, replacing site-packages with Scripts
In the control panel add what was copied to the path
Virtual Environment pip3 install --user pipx pipx install pipenv

Start Virtual Project pipenv shell

Third-Party Packages pipenv install django autopep8 pylint djangorestframework django-cors-headers pylint-django

Migrate data ./seed.sh

Start the Server python manage.py runserver
