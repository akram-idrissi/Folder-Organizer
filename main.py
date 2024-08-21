import os
import sys
import shutil
from colorama import Fore, Style, init


# Initialize Colorama
init()

# No need for a specific root on all OS
DIRNAME_PATTERN = 'Folders'


def mkdir(name):
    # Use os.makedirs to create directory and its parents if they don't exist
    if not os.path.exists(name):
        os.makedirs(name)


def move(old, new, filename="", folder=""):
    if os.path.exists(new):
        print(f"{Fore.RED}Error: The file '{filename}' already exists in '{folder}'. {Style.RESET_ALL}")
        return
    
    try:
        shutil.move(old, new)
        print(f"{Fore.GREEN}Success: Moved '{filename}' to '{folder}'. {Style.RESET_ALL}")
    except shutil.Error as e:
        print(f"{Fore.RED}Error: Unable to move '{filename}' to '{folder}': {e}. {Style.RESET_ALL}")


def validate_path(path):
    # Check if the path exists and is a directory
    if not os.path.isdir(path):
        print(f"{Fore.RED}Error: The provided path does not exist. Please provide a valid one. {Style.RESET_ALL}")
        return False

    return True


def main():
    if len(sys.argv) < 2:
        print(f"{Fore.RED}Error: Please provide a path. {Style.RESET_ALL}")
        return

    path = sys.argv[1]

    # Validate the provided path
    if not validate_path(path):
        return

    try:
        # creating Folders dir
        mkdir(os.path.join(path, DIRNAME_PATTERN))

        print(f"{Fore.BLUE}\nCleaning has been started !!\n{Style.RESET_ALL}")

        for file in os.listdir(path):
            file_path = os.path.join(path, file)

            if os.path.isdir(file_path):
                # Move subdirectories to the specified directory pattern
                if not file.startswith('.') and file != DIRNAME_PATTERN:
                    move(file_path, os.path.join(path, DIRNAME_PATTERN, file), file, DIRNAME_PATTERN)

            else:
                _, ext = os.path.splitext(file)
                # Create directories based on file extensions
                mkdir(os.path.join(path, ext))
                move(file_path, os.path.join(path, ext, file), file, ext)

        print(f"{Fore.BLUE}\nCleaning is done !!\n{Style.RESET_ALL}")

    # Handle FileNotFoundError specifically
    except FileNotFoundError as e:
        print(f"{Fore.RED}Error: {e.filename} not found{Style.RESET_ALL}")

    # Handle PermissionError specifically
    except PermissionError as e:
        print(f'Error: Permission issue. Unable to perform the operation on {e.filename}')
        print(f"{Fore.RED}Error: Permission issuen when moving {e.filename}{Style.RESET_ALL}")

    # Handle other unexpected exceptions
    except Exception as e:
        print(f"{Fore.RED}Error: An unexpected error occurred - {e}{Style.RESET_ALL}")


if __name__ == "__main__":
    main()
