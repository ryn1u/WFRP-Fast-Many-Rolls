import os
from os import listdir, path

if __name__ == '__main__':
    for file in [f for f in listdir('.') if path.isfile(f) and '.ui' in f]:
        name = file.split('.')[0]
        command = f"pyuic5 {name}.ui -o {name}.py"
        print(f"> {command}")
        os.system(command)
