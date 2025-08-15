import pickle
from pathlib import Path

def save_pickle(data, file_name):
    """Saves data to a pickle file."""
    directory = Path.cwd().joinpath("data", "stage", file_name)
    with open(directory, 'wb') as file:
        pickle.dump(data, file)


def load_pickle(file_name):
    """Loads data from a pickle file."""
    directory = Path.cwd().joinpath("data", "stage", file_name)
    with open(directory, 'rb') as file:
        return pickle.load(file)