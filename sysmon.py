try:
    with open("/proc/meminfo") as f:
        for line in f:
            if line.startswith("MemTotal"):
                print(line.strip())
except FileNotFoundError:
    print("/proc/meminfo not found — are you on Linux?")
except PermissionError:
    print("No permission to read /proc/meminfo")