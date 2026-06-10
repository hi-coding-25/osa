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
    
    if in_panel_before and 'opacity:' in line:
        # Estrai l'opacità attuale
        match = re.search(r'opacity:\s*(\.?[0-9]+);', line)
        if match:
            current_opacity = float(match.group(1))
            # Se è maggiore di 0.20, la abbassiamo di 0.20
            if current_opacity > 0.20:
                new_opacity = current_opacity - 0.20
                # Arrotonda a due cifre e togli lo zero se inizia con 0.
                formatted_opacity = f"{new_opacity:.2f}".replace('0.', '.')
                lines[i] = re.sub(r'opacity:\s*(\.?[0-9]+);', f'opacity: {formatted_opacity};', line)

# Inoltre, abbasso la riga 433 (il .panel::before principale)
# Trovo l'opacity: .68; sotto .panel::before
for i, line in enumerate(lines):
    if '.panel::before {' in line:
        for j in range(i, i+15):
            if 'opacity:' in lines[j]:
                match = re.search(r'opacity:\s*(\.?[0-9]+);', lines[j])
                if match:
                    current = float(match.group(1))
                    if current == 0.68:
                        lines[j] = re.sub(r'opacity:\s*(\.?[0-9]+);', f'opacity: .48;', lines[j])
                break

with open(css_path, 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("Opacità ridotta del 20%!")
