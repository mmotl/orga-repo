import nbformat
import os
import glob

def strip_solution_cells(nb_path):
    with open(nb_path, 'r') as f:
        nb = nbformat.read(f, as_version=4)

    # Filter out cells tagged with 'solution'
    nb.cells = [cell for cell in nb.cells if 'solution' not in cell.metadata.get('tags', [])]

    with open(nb_path, 'w') as f:
        nbformat.write(nb, f)
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

repository_root = find_repository_root()

# Find all notebooks in the "notebooks/" directory (you can customize the folder path)
#notebooks_directory = 'notebooks/'  # Replace with the directory where teachers save their notebooks
notebooks = glob.glob(os.path.join(repository_root,
                                    '**/*.ipynb'), recursive=True)

# Process each notebook found
for notebook in notebooks:
    strip_solution_cells(notebook)
