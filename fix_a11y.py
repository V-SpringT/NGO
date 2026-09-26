import os
import glob
import re

html_files = glob.glob(r"d:\Ke hoạch bạc tỷ\NGO\*.html") + glob.glob(r"d:\Ke hoạch bạc tỷ\NGO\events\*.html")

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Add id="main" if not exists
    if 'id="main"' not in content:
        # Find the first section or div after header
        # </header> usually followed by some <!-- comments --> and then <section ...>
        # We can just add id="main" to the first section.
        match = re.search(r'</header>.*?<section', content, flags=re.DOTALL)
        if match:
            # Add id="main" to that section
            content = content[:match.end()] + ' id="main" ' + content[match.end():]
        else:
            # If no section, try finding the first div after header
            match = re.search(r'</header>.*?<div', content, flags=re.DOTALL)
            if match:
                content = content[:match.end()] + ' id="main" ' + content[match.end():]

    # 2. Add loading="lazy" to imgs that don't have it and are not logo/preloader
    # Using a simple string replacement for now.
    # It's better to use regex to find <img ...> without loading="lazy"
    def repl_img(m):
        img_tag = m.group(0)
        if 'loading=' in img_tag or 'logo.png' in img_tag or 'preloader.png' in img_tag:
            return img_tag
        return img_tag.replace('<img ', '<img loading="lazy" ')
    
    content = re.sub(r'<img\s+[^>]*>', repl_img, content)

    # 3. Add lang="en" to html if missing
    if '<html' in content and 'lang=' not in content:
        content = content.replace('<html', '<html lang="en"')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Accessibility fixes applied to {len(html_files)} files.")
