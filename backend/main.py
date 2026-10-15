from fastapi import FastAPI
from backend.ticket_utils import count_tickets
from backend.schemas import TicketPreviewRequest

app=FastAPI(title="AI Customer Support API")

tickets = [
    {"id": 101, "status": "open"},
    {"id": 102, "status": "closed"},
    {"id": 103, "status": "open"}
]

@app.get("/")
def home():
    return {"message": "API is working!"}

@app.get("/api/health")
def health_check():
    return {"status": "healthy"}

@app.get("/api/tickets/summary")
def ticket_summary():
    return count_tickets(tickets)

@app.post("/api/tickets/preview")
def preview_ticket(ticket: TicketPreviewRequest):
    return {
        "message": "Ticket preview created successfully",
        "ticket": ticket.model_dump()
    }
