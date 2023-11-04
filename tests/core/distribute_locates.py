import pytest

from core.core import distribute_locates


@pytest.mark.parametrize('requested_locates, approved_locates, expected_distribution', [
    ({'QQQ': [('client1', 100), ('client2', 200)]}, {'QQQ': 300}, {'QQQ': {'client1': 100, 'client2': 200}}),
    ({'QQQ': [('client1', 500), ('client2', 200)]}, {'QQQ': 700}, {'QQQ': {'client1': 500, 'client2': 200}}),
    ({'QQQ': [('client1', 150), ('client2', 250)]}, {'QQQ': 400}, {'QQQ': {'client1': 150, 'client2': 250}}),
    ({'QQQ': [('client1', 135), ('client2', 100)]}, {'QQQ': 235}, {'QQQ': {'client1': 135, 'client2': 100}}),
])
def test_distribute_locates_all_approved(requested_locates, approved_locates, expected_distribution):
    """Test case for all locates approved for a single symbol"""
    assert distribute_locates(requested_locates, approved_locates) == expected_distribution


@pytest.mark.parametrize('requested_locates, approved_locates, expected_distribution', [
    ({'QQQ': [('client1', 100), ('client2', 200)]}, {'QQQ': 300}, {'QQQ': {'client1': 100, 'client2': 200}}),
    ({'QQQ': [('client1', 500), ('client2', 200)]}, {'QQQ': 600}, {'QQQ': {'client1': 500, 'client2': 100}}),
    ({'QQQ': [('client1', 500), ('client2', 200)]}, {'QQQ': 0}, {}),
    ({}, {'QQQ': 100}, {}),
    ({'QQQ': [('client1', 100), ('client2', 200)]}, {'QQQ': 150}, {'QQQ': {'client1': 100, 'client2': 50}})
])
def test_distribute_locates_partial_approval(requested_locates, approved_locates, expected_distribution):
    """Test case for partial approval of locates for a single symbol"""
    assert distribute_locates(requested_locates, approved_locates) == expected_distribution


@pytest.mark.parametrize('requested_locates, approved_locates, expected_distribution', [
    ({}, {'QQQ': 0}, {})])
def test_distribute_locates_unapproved(requested_locates, approved_locates, expected_distribution):
    """Test case for no approved locates for a single symbol"""
    assert distribute_locates(requested_locates, approved_locates) == expected_distribution


@pytest.mark.parametrize('requested_locates, approved_locates, expected_distribution', [
    ({'QQQ': [('client1', 100), ('client2', 200)]}, {}, {})])
def test_distribute_locates_no_requests(requested_locates, approved_locates, expected_distribution):
    """Test case for no requested locates for a single symbol"""
    assert distribute_locates(requested_locates, approved_locates) == expected_distribution


def test_distribute_with_two_symbols():
    """Test case for distribution with two symbols"""
    requested_locates = {'QQQ': [('client1', 100), ('client2', 200)], 'ABC': [('client1', 100), ('client5', 200)]}
    approved_locates = {'QQQ': 300, 'ABC': 300}
    expected_distribution = {'QQQ': {'client1': 100, 'client2': 200}, 'ABC': {'client1': 100, 'client5': 200}}
    assert distribute_locates(requested_locates,
                              approved_locates) == expected_distribution, ("there was an error in the distribution "
                                                                           "with 2 symbols")


def test_distribute_with_two_symbols_partial_approval():
    """Test case for distribution with two symbols and partial approval"""
    requested_locates = {'QQQ': [('client1', 100), ('client2', 200)], 'ABC': [('client1', 100), ('client5', 200)]}
    approved_locates = {'QQQ': 300, 'ABC': 200}
    expected_distribution = {'QQQ': {'client1': 100, 'client2': 200}, 'ABC': {'client1': 100, 'client5': 100}}
    assert distribute_locates(requested_locates, approved_locates) == expected_distribution


# Run the tests
if __name__ == '__main__':
    pytest.main()
