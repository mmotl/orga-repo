import glob
import os

def process_file(file_path):
    """Reads the file, removes lines between the markers, and writes back to the file."""
    start_marker = "-- START_SOLUTION"
    end_marker = "-- END_SOLUTION"
    inside_exclude_block = False

    with open(file_path, 'r') as file:
        lines = file.readlines()

    updated_lines = []
    for line in lines:
        if start_marker in line:
            inside_exclude_block = True
        elif end_marker in line:
            inside_exclude_block = False
            continue  # Skip the end marker line
        if not inside_exclude_block:
            updated_lines.append(line)

    with open(file_path, 'w') as file:
        file.writelines(updated_lines)

def find_repository_root():
    """
    Finds the root of the repository by searching for a .git folder.
    """
    current_dir = os.getcwd()
    while current_dir != os.path.dirname(current_dir):  # Stop at filesystem root
        if os.path.isdir(os.path.join(current_dir, '.git')):
            return current_dir
        current_dir = os.path.dirname(current_dir)
    return os.getcwd()  # Default to current directory if no .git is found

def main():
    """Processes all .sql files in the current directory."""
    repository_root = find_repository_root()
    scripts = glob.glob(os.path.join(repository_root,
                                    '**/*.sql'), recursive=True)

    # Process each notebook found
    for script in scripts:
        process_file(script)


if __name__ == "__main__":
    main()
