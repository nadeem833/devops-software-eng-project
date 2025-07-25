#!/bin/bash
echo "****************************************"
echo " Setting up Capstone Environment"
echo "****************************************"

<<<<<<< HEAD
echo "Updating package manager..."
sudo add-apt-repository -y ppa:deadsnakes/ppa

=======
>>>>>>> 1b50c88e08626c848688a42c96143d6b41d5eb1a
echo "Installing Python 3.9 and Virtual Environment"
sudo apt-get update
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y python3.9 python3.9-venv

<<<<<<< HEAD
echo "Making Python 3.9 the default..."
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 1
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.9 2

echo "Checking the Python version..."
python3 --version

echo "Creating a Python virtual environment"
python3 -m venv ~/venv
=======
echo "Checking the Python version..."
python3.9 --version

echo "Creating a Python virtual environment"
python3.9 -m venv ~/venv
>>>>>>> 1b50c88e08626c848688a42c96143d6b41d5eb1a

echo "Configuring the developer environment..."
echo "# DevOps Capstone Project additions" >> ~/.bashrc
echo "export GITHUB_ACCOUNT=$GITHUB_ACCOUNT" >> ~/.bashrc
echo 'export PS1="\[\e]0;\u:\W\a\]${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u\[\033[00m\]:\[\033[01;34m\]\W\[\033[00m\]\$ "' >> ~/.bashrc
echo "source ~/venv/bin/activate" >> ~/.bashrc

<<<<<<< HEAD
echo "Installing Python depenencies..."
source ~/venv/bin/activate && python3 -m pip install --upgrade pip wheel
=======
echo "Installing Python dependencies..."
source ~/venv/bin/activate && python3.9 -m pip install --upgrade pip wheel
>>>>>>> 1b50c88e08626c848688a42c96143d6b41d5eb1a
source ~/venv/bin/activate && pip install -r requirements.txt

echo "Starting the Postgres Docker container..."
make db

echo "Checking the Postgres Docker container..."
docker ps

echo "****************************************"
echo " Capstone Environment Setup Complete"
echo "****************************************"
echo ""
echo "Use 'exit' to close this terminal and open a new one to initialize the environment"
echo ""
