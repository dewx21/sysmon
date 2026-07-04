try:
    with open("/proc/meminfo") as f:
        mem = {line.split(":")[0]: line.split()[1] for line in f}
        totalgb=int(mem['MemTotal']) / 1024 / 1024
        print(f'Total GB: {totalgb:.2f} GB')
except FileNotFoundError:
    print("/proc/meminfo not found — are you on Linux?")
except PermissionError:
    print("No permission to read /proc/meminfo")