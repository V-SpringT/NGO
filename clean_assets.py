import os
import re
import glob

# Gather all source files
html_files = glob.glob('*.html') + glob.glob('events/*.html')
css_files = glob.glob('assets/css/*.css')
js_files = glob.glob('assets/js/*.js')

all_files = html_files + css_files + js_files

referenced_assets = set()

# Scan for references
for fname in all_files:
    try:
        with open(fname, 'r', encoding='utf-8') as f:
            content = f.read()
            
            # Match assets/...
            matches = re.findall(r'(assets/[a-zA-Z0-9_./-]+)', content)
            for m in matches:
                referenced_assets.add(m)
            
            # Match ../images/... and ../fonts/... in CSS
            if fname.endswith('.css'):
                css_matches = re.findall(r'\.\./(images/[a-zA-Z0-9_./-]+)', content)
                for m in css_matches:
                    referenced_assets.add('assets/' + m)
                
                font_matches = re.findall(r'\.\./(fonts/[a-zA-Z0-9_./-]+)', content)
                for m in font_matches:
                    referenced_assets.add('assets/' + m)
            
            # Match ../assets/... in events HTML
            if fname.startswith('events/'):
                event_matches = re.findall(r'\.\./(assets/[a-zA-Z0-9_./-]+)', content)
                for m in event_matches:
                    referenced_assets.add(m)
                    
    except Exception as e:
        pass

# Clean references (remove quotes, query strings, hashes)
cleaned_refs = set()
for ref in referenced_assets:
    ref = ref.strip('\'"()')
    ref = ref.split('?')[0]
    ref = ref.split('#')[0]
    cleaned_refs.add(ref)

deleted_count = 0
for root, dirs, files in os.walk('assets'):
    for file in files:
        file_path = os.path.join(root, file)
        norm_path = file_path.replace(os.sep, '/')
        
        # Check if the file is used
        is_used = False
        for ref in cleaned_refs:
            if ref == norm_path:
                is_used = True
                break
        
        if not is_used:
            print(f"Deleting unused asset: {norm_path}")
            os.remove(file_path)
            deleted_count += 1

print(f"Total deleted unused assets: {deleted_count}")
