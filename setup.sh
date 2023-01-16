wget https://www.python.org/ftp/python/3.9.9/Python-3.9.9.tgz
tar -zxvf Python-3.9.9.tgz
cd Python-3.9.9
sudo make altinstall
cd /usr/bin
sudo rm python
sudo ln -s /usr/local/bin/python3.9 python
python --version