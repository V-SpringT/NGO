import os
import glob
import re

events_dir = r"d:\Ke hoạch bạc tỷ\NGO\events"
files = glob.glob(os.path.join(events_dir, "event-*.html"))

for file_path in files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Title
    content = re.sub(r'<title>.*?</title>', '<title>Story — Anna Clerk Foundation</title>', content)
    
    # 2. H2 Event Detail -> Story
    content = content.replace('<h2>Event Detail</h2>', '<h2>Story</h2>')
    content = content.replace('<h2>Event Details</h2>', '<h2>Story</h2>')
    
    # 3. Breadcrumbs
    content = content.replace('<li><a href="../event.html">Events</a></li>', '<li><a href="../event.html">Stories & Learning</a></li>')
    content = content.replace('<li>Detail</li>', '<li>Story</li>')
    
    # 4. Back button
    content = content.replace('Back to all events', 'Back to all stories')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Updated {len(files)} event files.")
