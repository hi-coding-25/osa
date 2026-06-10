import re

css_path = '/Users/MRecupero/Desktop/osa/style.css'

with open(css_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

in_panel_before = False
for i, line in enumerate(lines):
    if '::before {' in line and ('.panel' in line or '.chart-panel' in line):
        in_panel_before = True
    elif '}' in line and in_panel_before:
        in_panel_before = False
    
    if in_panel_before and 'opacity:' in line:
        lines[i] = re.sub(r'opacity:\s*(\.?[0-9]+);', 'opacity: 1;', line)

with open(css_path, 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("Opacità ripristinate a 1 per risolvere la trasparenza delle foto sul fondo nero.")
