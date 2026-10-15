from backend.ticket_utils import count_tickets

def test_count_open_and_closed_tickets():
    tickets = [
        {'id': 1, 'status': 'open'},
        {'id': 2, 'status': 'closed'},
        {'id': 3, 'status': 'open'},
        {'id': 4, 'status': 'closed'},
        {'id': 5, 'status': 'open'},
    ]

    result = count_tickets(tickets)

    assert result['open'] == 3
    #The assert statement compares the actual result with the expected result. If they differ, pytest reports a failure.
    assert result['closed'] == 2

def test_empty_ticket_list():
    tickets = []

    result = count_tickets(tickets)

    assert result['open'] == 0
    assert result['closed'] == 0