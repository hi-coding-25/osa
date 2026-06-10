with open('/Users/MRecupero/Desktop/osa/index.html', 'r') as f:
    content = f.read()

# We need to fix:
# <span class="osa-mark">:<span class="slash">//</span><div class="h2-text"></span>
# It should be:
# <span class="osa-mark">:<span class="slash">//</span></span><div class="h2-text">

content = content.replace('<span class="osa-mark">:<span class="slash">//</span><div class="h2-text"></span>', '<span class="osa-mark">:<span class="slash">//</span></span><div class="h2-text">')

with open('/Users/MRecupero/Desktop/osa/index.html', 'w') as f:
    f.write(content)

print("Fixed")
