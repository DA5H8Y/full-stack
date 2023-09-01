# full-stack
A full-stack example

## Environment Setup
Follow the following steps too setup the environment

```bash
mkdir project_name
cd project_name
python -m venv env
source ./env/bin/activate
pip install Django mysqlclient
```

If you get an error it probable that you don't have the prerequisites for mysqlclient installed in this case run the following first

```bash
sudo apt-get install python3-dev default-libmysqlclient-dev build-essential
```

To exit the virtual environment use the command

```bash
deactivate
```