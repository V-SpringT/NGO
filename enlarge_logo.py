import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

def enlarge_logo(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Replace height 55px with 85px
        new_content = content.replace(
            'style="height:55px;width:auto;object-fit:contain;"',
            'style="height:85px;width:auto;object-fit:contain;"'
        )

        if content != new_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Enlarged logo in {filepath}")
    except Exception as e:
        print(f"Error processing {filepath}: {e}")

directory = r"d:\Ke hoạch bạc tỷ\NGO"
for filename in os.listdir(directory):
    if filename.endswith(".html"):
        enlarge_logo(os.path.join(directory, filename))
