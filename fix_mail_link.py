import os
import glob
import re

html_files = glob.glob(r"d:\Ke hoạch bạc tỷ\NGO\*.html") + glob.glob(r"d:\Ke hoạch bạc tỷ\NGO\events\*.html")

old_href = 'href="mailto:annaclerk.charity@gmail.com"'
new_href = 'href="https://mail.google.com/mail/?view=cm&fs=1&to=annaclerk.charity@gmail.com" target="_blank"'

updated = 0
for fp in html_files:
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if old_href in content:
        content = content.replace(old_href, new_href)
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(content)
        updated += 1
        print(f"Updated {os.path.basename(fp)}")

print(f"\nSuccessfully updated mail link in {updated} files.")
