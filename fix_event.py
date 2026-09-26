import re

file_path = r"d:\Ke hoạch bạc tỷ\NGO\event.html"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update title
content = re.sub(r'<title>.*?</title>', '<title>Stories & Learning — Anna Clerk Foundation</title>', content)

# 2. Update page title section
content = content.replace('<h2>Events</h2>', '<h2>Stories & Learning</h2>')
content = content.replace('<li>Events</li>', '<li>Stories</li>')

# 3. Update section title
content = content.replace("<span>H'Hen Nie's Charitable Journey</span>", "<span>External stories & learning</span>")
content = content.replace("<h2>Featured Events & Community Projects</h2>", "<h2>Public Case Studies</h2>")

# 4. Remove top-date blocks
content = re.sub(r'<div class="top-date">.*?</div>\s*</div>\s*<div class="image">', '<div class="image">', content, flags=re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated event.html")
