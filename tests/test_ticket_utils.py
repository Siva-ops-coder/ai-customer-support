from backend.ticket_utils import count_tickets

def test_count_open_and_closed_tickets():
    
    tickets = [
        {'id': 1, 'status': 'open'},
        {'id': 2, 'status': 'closed'},
        {'id': 3, 'status': 'open'},
        {'id': 4, 'status': 'closed'},
        {'id': 5, 'status': 'open'},
    ]

    assert count_tickets(tickets) == {'open': 3, 'closed': 2}

    

def test_empty_ticket_list():
    

    assert count_tickets([]) == {'open': 0, 'closed': 0}


    