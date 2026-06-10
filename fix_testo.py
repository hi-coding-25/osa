with open('/Users/MRecupero/Desktop/osa/index.html', 'r') as f:
    c = f.read()

vecchio = """<span class="osa-mark">:<span class="slash">//</span></span> Il&nbsp;linguaggio<br>è
                l'abbigliamento col quale<br>i&nbsp;vostri prodotti<br>si presentano in pubblico.</span>"""

nuovo = """<span class="osa-mark">:<span class="slash">//</span></span> Il&nbsp;linguaggio<br>è l'abbigliamento<br>col quale i vostri prodotti<br>si presentano in pubblico.</span>"""

vecchio_data = """data-typewriter-html="<span class=&quot;osa-mark&quot;>:<span class=&quot;slash&quot;>//</span></span> Il&nbsp;linguaggio<br>è l'abbigliamento col quale<br>i&nbsp;vostri prodotti<br>si presentano in pubblico." """

nuovo_data = """data-typewriter-html="<span class=&quot;osa-mark&quot;>:<span class=&quot;slash&quot;>//</span></span> Il&nbsp;linguaggio<br>è l'abbigliamento<br>col quale i vostri prodotti<br>si presentano in pubblico." """

c = c.replace(vecchio, nuovo)
c = c.replace(vecchio_data.strip(), nuovo_data.strip())

with open('/Users/MRecupero/Desktop/osa/index.html', 'w') as f:
    f.write(c)
print("Fatto")
