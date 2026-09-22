"""Smoke test for entertainment-ticket-booking-system-high-load: booking logic."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.booking_engine import TicketEngine


def main():
    engine = TicketEngine(total_seats=5)
    results = [engine.book_ticket(f"user-{i}") for i in range(5)]
    assert all("booked" in r for r in results), results

    overflow = engine.book_ticket("user-late")
    assert "failed" in overflow, overflow

    stats = engine.get_stats()
    assert stats["Total Seats"] == 5
    assert stats["Available"] == 0
    assert stats["Booked"] == 5
    assert stats["Failed"] == 1

    print("smoke OK: booking, sold-out handling, stats")


if __name__ == "__main__":
    main()
