import os
import subprocess
from getPSSH import return_pssh
import re

print("\n===================================================")
print("           MPD KID Extractor - By Aiman")
print("           Added GET PSSH - By MoiZz")
print("===================================================\n")

url = input("Enter the URL: ")

subprocess.run(['yt-dlp', '--allow-u', '--no-progress', '--console-title', url],
           stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

for file in os.listdir():
if file.endswith('.mp4'):
    os.rename(file, 'test.mp4')
    break

kid = None
dump_output = subprocess.run(['mp4dump.exe', 'test.mp4'], capture_output=True, text=True).stdout
for line in dump_output.split('\n'):
    if 'KID' in line:
        kid = re.search(r'\[(.*?)\]', line)
        if kid:
            kid = kid.group(1)
        break

if kid:
    print(f"KID = {kid}")
else:
    print("MPD doesn't have a KID.")

for file in os.listdir():
    if file.endswith('.m4a') or file == 'test.mp4':
        os.remove(file)

print(return_pssh(kid))

input("Press any key to continue . . .")