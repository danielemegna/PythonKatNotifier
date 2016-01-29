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

Now you can run tests via
```
$ python test/*.py
```
or easier with the bash script
```
$ ./runtest
```


