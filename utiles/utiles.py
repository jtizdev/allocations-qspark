import csv
import os


def get_file_path(file_name: str):
    """
    Args:
        file_name(str): name of file

    Returns:
        path to file

    """
    return os.path.join(os.path.dirname(__file__), file_name)


def read_requests_from_csv(file_path: str, requests=None):
    """

    Args:
        file_path: path to csv file
        requests: dictionary of requests

    Returns:
        requests dictionary
    """
    if requests is None:
        requests = {}
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            client_name, symbol, locates_requested = row
            locates_requested = int(locates_requested)  # casting to integer
            requests.setdefault(symbol, []).append((client_name, locates_requested))
    return requests
