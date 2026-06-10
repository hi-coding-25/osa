import re

html_path = '/Users/MRecupero/Desktop/osa/index.html'
css_path = '/Users/MRecupero/Desktop/osa/style.css'

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Usa re.DOTALL per fare match su newline
pattern = re.compile(r'\s*<style>(.*?)</style>\s*', re.DOTALL)
match = pattern.search(content)

if match:
    css_content = match.group(1).strip()
    # Salva il CSS in style.css
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css_content)
    
    # Sostituisci il blocco nel file html con il tag <link>
    replacement = '\n  <link rel="stylesheet" href="style.css">\n'
    new_content = content[:match.start()] + replacement + content[match.end():]
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Estrazione completata con successo!")
else:
    print("Non ho trovato il tag <style>.")
