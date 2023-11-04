from utiles.utiles import read_requests_from_csv, get_file_path
from core.core import distribute_locates


def request_locates(requested_locates: dict[str, int]) -> dict[str, int]:
    # need to ask about this function, what the expected output is
    return {}


def main():
    requested_locates = read_requests_from_csv(get_file_path('../resources/locates_requests.csv'))
    approved_locates = request_locates(requested_locates)
    distribution = distribute_locates(requested_locates, approved_locates)
    print(distribution)


if __name__ == "__main__":
    main()
