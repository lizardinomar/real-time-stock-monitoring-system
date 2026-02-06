# Real Time Stock Monitoring System
A lightweight, non-stop running monitoring and alert system designed to run as a background service on Linux. It tracks real-time stock prices and triggers alerts based on predefined conditions.

## Overview
The system continuously monitors selected stocks and evaluates them against user-defined thresholds. It is designed to run unattended (via systemd) and act as a central hub for price-based alerts.
The system is built to be:
- Minimal and fast
- Service-oriented (runs on boot)
- Easy to extend with new alert mechanisms.

## Core Features
- Real-time stock price polling
- Configurable price thresholds
- Background execution using systemd
- Automatic restart on failure
- Modular design for future integrations (LEDs, sounds, notifications, APIs)

## How It Works
1. The service starts automatically at boot.
2. stock_tracker.py fetches live market data at regular intervals.
3. Prices are compared against configured alert conditions.
4. When conditions are met, alerts are triggered.
5. The loop continues until the service is stopped.

## Live Demo

![Watch Demo](media/smdemo1.gif)

## Hardware

![Hardware Section](hardware/README.md)

## Running as a Service
The system is designed to run via systemd:
- Starts automatically on boot
- Restarts if the script crashes
- Runs independently of user sessions
Service status can be checked with:
"systemctl status stock-tracker.service"

## Configuration
Stocks and alert conditions are defined in the configuration layer. This allows easy changes without modifying the core logic.
Typical configuration includes:
- Stock ticker symbols
- Target prices or ranges
- Polling interval

## Requirements 
- Linux system with systemd
- Python 3.x
- Internet connection for market data

## Future Expansion
- Integrate more stocks to monitor.
- 24/7 market monitoring.
- Alerts to be more descriptive of what is going on.

## Notes
- yfinance must be installed in the venv.
  source ~/stockenv/bin/activate
  pip install yfinance
- Internet connection required.
- Market must be open for live prices (otherwise last close is used).
