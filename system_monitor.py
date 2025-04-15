import os
import platform
import psutil
import datetime
import argparse
from getpass import getuser

def get_uptime():
    with open('/proc/uptime', 'r') as f:
        uptime_seconds = float(f.readline().split()[0])
    uptime_str = str(datetime.timedelta(seconds=int(uptime_seconds)))
    return uptime_str

def get_load_average():
    return os.getloadavg()

def get_memory_usage():
    mem = psutil.virtual_memory()
    return mem.used / (1024 ** 3), mem.total / (1024 ** 3)

def get_disk_usage():
    usage = psutil.disk_usage('/')
    return usage.percent

def get_logged_in_users():
    return sorted(set(u.name for u in psutil.users()))

def get_top_processes(limit=5):
    procs = [(p.info['cpu_percent'], p.info['name']) for p in psutil.process_iter(['name', 'cpu_percent'])]
    return sorted(procs, reverse=True)[:limit]

def generate_report():
    uptime = get_uptime()
    load_avg = get_load_average()
    mem_used, mem_total = get_memory_usage()
    disk = get_disk_usage()
    users = get_logged_in_users()
    top_procs = get_top_processes()

    suspicious = []
    if load_avg[0] > 2.0:
        suspicious.append("⚠️ High CPU load average detected")
    if (mem_used / mem_total) > 0.85:
        suspicious.append("⚠️ High memory usage detected")
    if disk > 90:
        suspicious.append("⚠️ Disk space critically low")

    report = f"""===== Linux System Monitor =====
User: {getuser()}
Uptime: {uptime}
Load Average: {load_avg[0]:.2f}, {load_avg[1]:.2f}, {load_avg[2]:.2f}
Memory Usage: {mem_used:.1f} GB / {mem_total:.1f} GB
Disk Usage: {disk}%
Logged In Users: {', '.join(users)}
Top Processes by CPU:
"""
    for cpu, name in top_procs:
        report += f"- {name}: {cpu:.1f}% CPU\n"

    if suspicious:
        report += "\n--- ⚠️ Suspicious Activity Detected ---\n"
        for flag in suspicious:
            report += f"{flag}\n"

    report += "================================\n"
    return report

def save_report(report):
    filename = f"sysreport_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
    with open(filename, 'w') as f:
        f.write(report)
    print(f"Report saved as {filename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Linux System Monitor CLI")
    parser.add_argument("--save", action="store_true", help="Save report to file")
    args = parser.parse_args()

    report = generate_report()
    print(report)
    if args.save:
        save_report(report)
