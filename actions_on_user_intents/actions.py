def presale_tickets():

    return {

        "presale_text": """Mean while friend I see you are interested in tickets? I have a couple for you!""",
        "tickets": [
            {"name": "Test ticket 1", 
             "description": "Raffle ticket for participation small collection", 
             "price": 10,
             "image": "https://www.lifebuilderstc.com/uploads/4/2/8/0/4280388/s615747952753621297_p62_i1_w612.jpeg"},
            {"name": "Test ticket 2", 
             "description": "Raffle ticket for participation small collection", 
             "price": 10,
             "image": "https://www.lifebuilderstc.com/uploads/4/2/8/0/4280388/s615747952753621297_p62_i1_w612.jpeg"},
            {"name": "Test ticket 3", 
             "description": "Raffle ticket for participation small collection", 
             "price": 10,
             "image": "https://www.lifebuilderstc.com/uploads/4/2/8/0/4280388/s615747952753621297_p62_i1_w612.jpeg"},
        ]
    }


ACTIONS = {
    "PurchaseTicketProcess": presale_tickets,
    "RequiredInformation": "RequiredInformation",
    "ParticipationSteps": "ParticipationSteps",
    "TicketPurchaseLimit": presale_tickets,
}