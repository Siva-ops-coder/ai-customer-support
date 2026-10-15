def count_tickets(tickets):
    counts = {
        'open': 0,
        'closed': 0,
    }

    for ticket in tickets:
        if ticket['status'] == 'open':
            counts['open'] += 1
        elif ticket['status'] == 'closed':
            counts['closed'] += 1

    return counts
