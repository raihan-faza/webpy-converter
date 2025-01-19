import sys

import httpx
from PIL import Image


def convert(inp, outp):
    webp_path = sys.argv[2]
    desired_path = sys.argv[3]
    print("[+] Trying to convert image")
    try:
        with Image.open(webp_path) as img:
            img.save(desired_path, format="PNG")
        print("[$] Image converted succesfully")
    except:
        print("[!] Failed to convert image")


def download(url):
    try:
        with httpx.Client() as h:
            res = h.get(url)
            res.raise_for_status()
            with open("temp.webp", "wb") as file:
                file.write(res.content)
    except:
        print("[!] Failed to download image")
        sys.exit()
    try:
        with Image.open("image.webp") as img:
            img.verify()
        print("[$] Image verified")
    except:
        print(f"[!] Failed to verify downloaded image")
        sys.exit()
