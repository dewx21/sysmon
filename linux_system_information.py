import subprocess

def run_command(command):
    try:
        result=subprocess.run(command, shell=True, text=True, capture_output=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"Error: {e}"

def main():
    print("="*50)
    print("Linux system information")
    print("="*50)

    commands={"Hostname":"hostname", "Current User":"whoami", "Kernel Version":"uname -r", "Current directory":"pwd"}

    for title, command in commands.items():
        print(f"\n{title:}")

print(run_command(command))

print("\n Python successfully executed Linux Commands!")

if __name__ == "__main__":
    main()

