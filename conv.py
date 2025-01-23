import os
import sys

from pyfiglet import Figlet

from lahh.lahh import convert, download

f = Figlet(font="slant")

print(f.renderText("webpy.conv"))
if len(sys.argv) < 2:
    print("Error: missing argument, type python conv.py -h for references")
    sys.exit(1)
elif "-h" in sys.argv[1]:
    print("Usage: python conv.py image_file_path desired_bnw_image_file_path")
    print("Example: python conv.py -f /home/lahh/lahh.webp /home/lahh/lahh.png")
    print("Example: python conv.py -u https://lahh.com/lahh.webp /home/lahh/lahh.png")
    sys.exit(1)

command = sys.argv[1]
if command == "-f":
    webp_path = sys.argv[2]
    desired_path = sys.argv[3]
    convert(webp_path, desired_path)

elif command == "-u":
    url = sys.argv[2]
    desired_path = sys.argv[3]
    download(url)
    convert("temp.webp", desired_path)
    os.remove("temp.webp")
