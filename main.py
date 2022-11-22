import os
import sys

WIN_ROOT = 'C'
DIRNAME_PATTERN = 'Folders'


def mkdir(name):
    if not os.path.isdir(name):
        os.mkdir(name)


def move(old, new):
    os.rename(old, new)


def validate_path(path):
    if not path.startswith(WIN_ROOT): 
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
    mkdir(DIRNAME_PATTERN)

    try:
        print('Cleaning has been started !!')
        
        for file in os.listdir():
            if os.path.isdir(file):
                if not file.startswith('.') and file != DIRNAME_PATTERN: 
                    move(file, os.path.join(DIRNAME_PATTERN, file))
                
            else:
                _, ext = os.path.splitext(file)
                mkdir(ext)
                move(file, os.path.join(ext, file))
    
        print('Cleaning is done !!')
    except Exception as e:
        print('This error occured when trying to clean this folder ' + str(e))


if __name__ == "__main__":
    main()
