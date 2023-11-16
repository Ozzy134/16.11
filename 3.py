import os

def print_reps(directory):
    for path, dirs, files in os.walk(directory):
        for dir in dirs:
            print(os.path.join(path, dir))
        for file in files:
            print(os.path.join(path, file))

os.chdir('../venv')
directory = os.getcwd()
print_reps(directory)