# PythonKatNotifier

PythonKatNotifier looks for you for the most downloaded movies on torrents sites and notify you about them

### pip & virtualenv

Dependecies are managed by pip

You can keep clean your local environment using virtualenv (https://pypi.python.org/pypi/virtualenv).

Install virtualenv via pip:
```
$ pip install virtualenv
```
Create a virtual environment for the project:
```
$ virtualenv venv
```
Activate it:
```
$ source venv/bin/activate
```
Install project dependencies into the new virtual environment:
```
$ pip install -r requirements.txt
```
You'll be able to deactivate the virtual environment using
```
$ deactivate
```

### Run it

Remember to prepare a ready compatible sqlite file before (*production.db* by default)
```
$ cp empty.db production.db
```
Now configure it managing dependecies injections into work.py and run it via
```
$ python work.py
```

### Docker way

Build the docker container with
```
$ docker build -t "pykat" .
```
and run it with
```
$ docker run --name pykat pykat 
```
or interative mode with
```
$ docker run -itv $(pwd):/app --name pykat pykat bash
```

### Tests

You can run all the tests via:
```
$ python -m unittest discover
```
or easier via the bash script:
```
$ ./runtest
```
Remember to install the dev dependecies with
```
$ pip install -r requirements.txt
$ pip install -r requirements.dev
```
The runtest script is compiliant with unittest test selectors:
```bash
$ ./runtest test_module               # run tests from test_module
$ ./runtest module.TestClass          # run tests from module.TestClass
$ ./runtest module.Class.test_method  # run specified test method
```
The test package structure allows selective test run for *unit* and *integration* tests:
```bash
$ ./runtest test.unit         # run unitary tests
$ ./runtest test.integration  # run integration tests
```
