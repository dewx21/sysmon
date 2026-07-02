with open("/proc/meminfo") as f:
    print(f.read())