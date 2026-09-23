import time
from booking_engine import TicketEngine
from concurrent.futures import ThreadPoolExecutor

def main():
    SEATS = 50
    USERS = 120 # Overbooking scenario
    
    print(f"--- High Load Ticket Event ({SEATS} Seats, {USERS} Users) ---")
    
    engine = TicketEngine(total_seats=SEATS)
    results = []

    print("🚀 Opening Sales! (Simulating 120 concurrent requests)...")
    start = time.time()
    
    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = {executor.submit(engine.book_ticket, f"User_{i+1}"): i for i in range(USERS)}
        
        for future in futures:
            results.append(future.result())
            
    end = time.time()
    
    print("\n--- Results ---")
    # Sample a few
    for r in results[:5]: print(r)
    print("...")
    for r in results[-5:]: print(r)

    stats = engine.get_stats()
    print("\n--- Final Stats ---")
    print(f"Sold: {stats['Booked']}/{stats['Total Seats']}")
    print(f"Failed Requests: {stats['Failed']}")
    print(f"Time Taken: {end - start:.2f}s")
    
    if stats['Booked'] > stats['Total Seats']:
        print("🚨 CRITICAL BUG: Oversold!")
    elif stats['Booked'] == stats['Total Seats'] and stats['Available'] == 0:
        print("✅ Perfect Sellout.")

if __name__ == "__main__":
    main()
