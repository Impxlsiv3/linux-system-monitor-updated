# Linux System Monitor

A lightweight Python CLI utility to monitor and report key Linux system metrics like uptime, CPU load, memory usage, disk space, and user sessions.

## Features
- Uptime and system load info
- Memory and disk usage
- Logged-in user list
- Top processes by CPU usage
- Optional report saving

## Requirements
- Python 3.x
- Linux system with `/proc` and `psutil`

## Usage
```bash
python system_monitor.py
```

To save a report:
```bash
python system_monitor.py --save
```
