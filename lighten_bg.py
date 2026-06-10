import re
import sys

css_path = '/Users/MRecupero/Desktop/osa/style.css'

with open(css_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

in_panel_before = False
for i, line in enumerate(lines):
    if '::before {' in line and ('.panel' in line or '.chart-panel' in line):
        in_panel_before = True
    elif '}' in line and in_panel_before:
        in_panel_before = False
    
    if in_panel_before:
        # Riportiamo l'opacità al 100% per non far affondare la foto nel nero del div contenitore
        if 'opacity:' in line:
            lines[i] = re.sub(r'opacity:\s*(\.?[0-9]+);', 'opacity: 1;', line)
        
        # Schiariamo i gradienti rgba(5, 5, 5, X) del 50%
        if 'rgba(5, 5, 5,' in line:
            def halve_alpha(match):
                current_alpha = float(match.group(1))
                new_alpha = current_alpha / 2  # dimezza il nero!
                formatted = f"{new_alpha:.2f}".replace('0.', '.')
                return f"rgba(5, 5, 5, {formatted})"
            
            lines[i] = re.sub(r'rgba\(5,\s*5,\s*5,\s*(\.?[0-9]+)\)', halve_alpha, line)

with open(css_path, 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("Modifica applicata: opacity ripristinata a 1, e neri dimezzati!")
