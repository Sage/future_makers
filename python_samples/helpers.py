import os

def get_environment_variable(variable):
    if variable in os.environ:
        value = os.environ[variable]
        return value
    else:
        print('Environment variable for ' + variable + ' is not set.')
        exit()