def distribute_locates(requested_locates:dict, approved_locates:dict):
    """
    Args:
        requested_locates: dictionary of requested locates by symbol and client
        approved_locates: dictionary of approved locates by symbol

    Returns:
        dictionary of distributed locates by symbol and client
    """
    distribution = {}
    for symbol, requests in requested_locates.items():
        approved = approved_locates.get(symbol, 0)
        if approved > 0:
            distribution[symbol] = distribute_partial_approval(requests, approved)
    return distribution


def distribute_partial_approval(requested_locates: dict, approved_locates: int):
    """

    Args:
        requested_locates (list): list of tuples of client and requested locates
        approved_locates (int): number of approved locates

    Returns:
        dictionary of distributed locates by client

    """
    distribution = {}
    for client, requested in requested_locates:
        if approved_locates >= requested:
            distribution[client] = requested
            approved_locates -= requested
        else:
            distribution[client] = approved_locates
            approved_locates = 0
    return distribution
