import os
import platform
import shutil
import subprocess


def run_powershell(command):
    try:
        result = subprocess.run(
            ["powershell", "-Command", command],
            capture_output=True,
            text=True,
            timeout=5
        )
        return result.stdout.strip()
    except Exception:
        return "Unknown"


def get_system_info():
    print("=== SYSTEM ===")
    print(f"OS           : {platform.system()} {platform.release()}")
    print(f"Computer     : {platform.node()}")
    print(f"Architecture : {platform.machine()}")
    print(f"Python       : {platform.python_version()}")
    print()


def get_cpu_info():
    print("=== CPU ===")

    cpu = run_powershell(
        "(Get-CimInstance Win32_Processor).Name"
    )

    cores = os.cpu_count()

    print(f"Processor    : {cpu}")
    print(f"CPU cores    : {cores}")
    print()


def get_gpu_info():
    print("=== GPU ===")

    gpu = run_powershell(
        "(Get-CimInstance Win32_VideoController).Name"
    )

    print(f"Graphics     : {gpu}")
    print()


def get_memory_info():
    print("=== RAM ===")

    memory = run_powershell(
        "(Get-CimInstance Win32_ComputerSystem).TotalPhysicalMemory"
    )

    try:
        memory_gb = int(memory) / (1024 ** 3)
        print(f"Total RAM    : {memory_gb:.1f} GB")
    except (ValueError, TypeError):
        print("Total RAM    : Unknown")

    print()


def get_disk_info():
    print("=== STORAGE ===")

    total, used, free = shutil.disk_usage(os.path.abspath(os.sep))

    print(f"Total        : {total / (1024 ** 3):.1f} GB")
    print(f"Used         : {used / (1024 ** 3):.1f} GB")
    print(f"Free         : {free / (1024 ** 3):.1f} GB")
    print()


def main():
    print("=" * 40)
    print("           PC-TOOLKIT")
    print("=" * 40)
    print()

    get_system_info()
    get_cpu_info()
    get_gpu_info()
    get_memory_info()
    get_disk_info()

    print("Diagnostic complete.")


if __name__ == "__main__":
    main()
