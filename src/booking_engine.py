import time
import random
import threading
from concurrent.futures import ThreadPoolExecutor

class TicketEngine:
    def __init__(self, total_seats=50):
        self.total_seats = total_seats
        self.available_seats = total_seats
        self.lock = threading.Lock()
        self.bookings = []
        self.failed_bookings = 0

    def book_ticket(self, user_id):
        """Attempts to book a ticket with locking."""
        # Simulating processing
        time.sleep(random.uniform(0.01, 0.05))

        # Critical Section
        with self.lock:
            if self.available_seats > 0:
                self.available_seats -= 1
                ticket_id = f"TICKET-{self.total_seats - self.available_seats}"
                self.bookings.append({"user": user_id, "ticket": ticket_id})
                return f"✅ User {user_id} booked {ticket_id}"
            else:
                self.failed_bookings += 1
                return f"❌ User {user_id} failed (Sold Out)"

    def get_stats(self):
        return {
            "Total Seats": self.total_seats,
            "Available": self.available_seats,
            "Booked": len(self.bookings),
            "Failed": self.failed_bookings
        }
