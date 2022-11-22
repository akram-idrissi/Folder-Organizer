import os
import sys


def validate_path(path):
    if not path.startswith('C'): 
        print('Path not found..Please provide the absolute path to the folder you want to organize')
        return False

    if not os.path.isdir(path):
        print('The provided folder is not found..Please provide an existing folder.')
        return False

    return True

def main() :
    path = sys.argv[1]
    if not validate_path(path) : return
    os.chdir(path)
    
    for file in os.listdir():
        print(file) 


if __name__ == "__main__":
    main()