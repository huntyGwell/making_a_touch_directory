import subprocess

url = "https://public.byulaw.org/directory"

firefox_command = f"firefox --kiosk {url}"
subprocess.run(firefox_command, shell=True)
