with open('/Users/MRecupero/Desktop/osa/index.html', 'r') as f:
    content = f.read()

# We want to add CSS rules for h2 with osa-mark.
css_to_add = """
    h2:has(> .osa-mark) {
      display: flex;
      align-items: flex-start;
      gap: 0;
    }
    
    h2:has(> .osa-mark) .osa-mark {
      flex-shrink: 0;
      /* margin-right is already .28em on .osa-mark, which gives the gap */
    }
    
    .h2-text {
      flex: 1;
      /* If text is center-aligned globally, but we want it to flow normally inside the flex container, flex: 1 works perfectly */
    }
"""

# Let's insert it after .osa-mark definition
content = content.replace('    .osa-mark {', css_to_add + '\n    .osa-mark {')

with open('/Users/MRecupero/Desktop/osa/index.html', 'w') as f:
    f.write(content)

print("Done")
