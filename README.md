# PythonKatNotifier

.... (todo)

### virtualenv

Dependecies are managed by virtualenv (https://pypi.python.org/pypi/virtualenv).

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
$ pip install -r dependencies.txt
```

You'll be able to deactivate the virtual environment using
```
$ deactivate
```

### Test

Now you can run all the tests via:
```
$ python -m unittest discover
```
or easier via the bash script:
```
$ ./runtest
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
