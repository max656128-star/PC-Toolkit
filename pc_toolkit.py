import os
import platform
import shutil
import subprocess


def get_windows_info():
    print("=== SYSTEM INFORMATION ===")
    print(f"Operating system : {platform.system()} {platform.release()}")
    print(f"Computer         : {platform.node()}")
    print(f"Architecture     : {platform.machine()}")
    print(f"Python version   : {platform.python_version()}")
    print()


def get_cpu_info():
    print("=== CPU ===")

    try:
        result = subprocess.run(
            [
                "powershell",
                "-Command",
                "(Get-CimInstance Win32_Processor).Name"
            ],
            capture_output=True,
            text=True,
            timeout=5
        )

        cpu = result.stdout.strip()

        if cpu:
            print(f"Processor : {cpu}")
        else:
            print("Processor : Unable to detect")
    except Exception:
        print("Processor : Unable to detect")

    print(f"CPU cores : {os.cpu_count()}")
    print()


def get_memory_info():
    print("=== MEMORY ===")

    try:
        result = subprocess.run(
            [
                "powershell",
                "-Command",
                "(Get-CimInstance Win32_ComputerSystem).TotalPhysicalMemory"
            ],
            capture_output=True,
            text=True,
            timeout=5
        )

        memory = int(result.stdout.strip())
        memory_gb = memory / (1024 ** 3)

        print(f"Total RAM : {memory_gb:.1f} GB")
    except Exception:
        print("RAM      : Unable to detect")

    print()


def get_disk_info():
    print("=== STORAGE ===")

    total, used, free = shutil.disk_usage(os.path.abspath(os.sep))

    total_gb = total / (1024 ** 3)
    used_gb = used / (1024 ** 3)
    free_gb = free / (1024 ** 3)

    print(f"Total : {total_gb:.1f} GB")
    print(f"Used  : {used_gb:.1f} GB")
    print(f"Free  : {free_gb:.1f} GB")
    print()


def main():
    print("================================")
    print("          PC-TOOLKIT")
    print("================================")
    print()

    get_windows_info()
    get_cpu_info()
    get_memory_info()
    get_disk_info()

    print("Diagnostic complete.")


if __name__ == "__main__":
    main()
