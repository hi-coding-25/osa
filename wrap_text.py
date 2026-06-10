import re

with open('/Users/MRecupero/Desktop/osa/index.html', 'r') as f:
    content = f.read()

# We want to find all <h2> elements that start with <span class="osa-mark">...</span>
# and wrap the REST of the innerHTML in a <span class="h2-text"> ... </span>
# IF it's not already wrapped.

def replacer(match):
    prefix = match.group(1) # <h2...>
    mark = match.group(2)   # <span class="osa-mark">...</span>
    rest = match.group(3)   # The rest of the h2 content
    
    # Check if rest is just a single span
    if re.match(r'^\s*<span[^>]*>.*</span>\s*$', rest, re.DOTALL):
        # Already wrapped in a span (like typewriter-text)
        # We can still wrap it, or add a class, but we don't need to change much.
        # Actually, it's safer to just wrap EVERYTHING in a div or span that acts as the text container.
        # Wait, if we wrap it in a div, h2 flex item will work perfectly.
        return f"{prefix}{mark}<div class=\"h2-text\">{rest}</div></h2>"
    else:
        return f"{prefix}{mark}<div class=\"h2-text\">{rest}</div></h2>"

# Regex to match <h2> with osa-mark inside it.
# We use non-greedy matching to find the end of the h2.
new_content = re.sub(
    r'(<h2[^>]*>)\s*(<span class="osa-mark">.*?</span>)(.*?)</h2>',
    replacer,
    content,
    flags=re.DOTALL
)

with open('/Users/MRecupero/Desktop/osa/index.html', 'w') as f:
    f.write(new_content)

print("Done")
