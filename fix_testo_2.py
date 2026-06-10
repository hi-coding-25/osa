with open('/Users/MRecupero/Desktop/osa/index.html', 'r') as f:
    c = f.read()

# Vecchio codice HTML (quello che ho messo io nell'ultimo turno in cui l'ho inserito dentro lo span)
vecchio = """        <div class="hero-copy">
          <h2>
            <div class="h2-text"><span class="typewriter-text"
                data-typewriter-html="<span class=&quot;osa-mark&quot;>:<span class=&quot;slash&quot;>//</span></span> Il&nbsp;linguaggio<br>è l'abbigliamento<br>col quale i vostri prodotti<br>si presentano in pubblico."><span class="osa-mark">:<span class="slash">//</span></span> Il&nbsp;linguaggio<br>è l'abbigliamento<br>col quale i vostri prodotti<br>si presentano in pubblico.</span></div>
          </h2>
        </div>"""

# Nuovo codice HTML: il simbolo osa-mark FUORI, come figlio diretto di h2, e il testo spezzato con br nel typewriter
nuovo = """        <div class="hero-copy">
          <h2><span class="osa-mark">:<span class="slash">//</span></span>
            <div class="h2-text"><span class="typewriter-text"
                data-typewriter-html="Il&nbsp;linguaggio<br>è l'abbigliamento<br>col quale i vostri prodotti<br>si presentano in pubblico.">Il&nbsp;linguaggio<br>è l'abbigliamento<br>col quale i vostri prodotti<br>si presentano in pubblico.</span></div>
          </h2>
        </div>"""

# Ripristiniamo
if vecchio in c:
    c = c.replace(vecchio, nuovo)
else:
    print("Non trovato, provo a cercare pezzi.")
    import re
    # Proviamo una regex più flessibile
    c = re.sub(
        r'<div class="hero-copy">\s*<h2>\s*<div class="h2-text"><span class="typewriter-text"[^>]+>.*?</span></div>\s*</h2>\s*</div>',
        nuovo,
        c,
        flags=re.DOTALL
    )

with open('/Users/MRecupero/Desktop/osa/index.html', 'w') as f:
    f.write(c)
print("Fatto")
