# Linux System Monitor

A Python CLI tool for Linux that reports system uptime, CPU/memory/disk usage, active users, and top processes. Automatically flags high resource usage and saves audit-friendly reports.

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
