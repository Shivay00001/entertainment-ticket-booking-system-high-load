# Entertainment Ticket Booking System (High Load)

[![Python 3.11](https://img.shields.io/badge/Python-3.11-3776AB.svg)](https://www.python.org/)
[![Concurrency](https://img.shields.io/badge/Architecture-Concurrent_Locking-red.svg)](https://docs.python.org/3/library/threading.html)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A **production-grade simulation of a high-load ticketing engine**. This repository demonstrates how to handle concurrent booking requests for a limited inventory (e.g., concert tickets) using thread-safe locking mechanisms to prevent overselling (Double Booking).

## 🚀 Features

- **Concurrent Booking Engine**: Handles multiple simultaneous user requests.
- **Optimistic Locking**: Simulates rapid seat reservation.
- **Inventory Management**: Real-time seat tracking.
- **Stress Testing**: Includes a simulation of 100+ concurrent users fighting for 50 seats.

## 📁 Project Structure

```
entertainment-ticket-booking-system-high-load/
├── src/
│   ├── booking_engine.py # Core Locking Logic
│   └── main.py           # Stress Test Simulation
├── requirements.txt
└── Dockerfile
```

## 🛠️ Quick Start

```bash
# Clone
git clone https://github.com/Shivay00001/entertainment-ticket-booking-system-high-load.git

# Run Stress Test (100 users, 50 seats)
python src/main.py
```

## 📄 License

MIT License
