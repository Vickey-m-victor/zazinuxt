import os
import re

def process_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".vue"):
                filepath = os.path.join(root, file)
                process_file(filepath)

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    
    # We will just globally replace <a with <NuxtLink and </a> with </NuxtLink>
    # because NuxtLink correctly handles external links and anchor links.
    # But wait, what if there's an <a> tag with no href, or an anchor?
    # Let's be safer and only change <a> tags that have an href to a .html file.
    
    # A regex to match an <a> tag that contains href="something.html"
    # This is tricky due to nested tags.
    
    # Let's just do standard string replacements for the most common ones.
    # Actually, NuxtLink is completely fine for all <a> tags.
    # Let's change href="index.html" -> to="/"
    content = re.sub(r'href="index\.html(#.*?)?"', r'to="/\1"', content)
    
    # href="about.html" -> to="/about"
    content = re.sub(r'href="([a-zA-Z0-9_-]+)\.html(#.*?)?"', r'to="/\1\2"', content)
    
    # Now replace <a ... to=... > to <NuxtLink ... to=... >
    # Because we only changed href= to to= for the ones we want to convert.
    # So we can look for <a and > that contain 'to=' and change them?
    # No, we need to change the matching </a>.
    # Since it's too hard to balance tags with regex, we will just globally replace
    # ALL <a and </a> with <NuxtLink and </NuxtLink> globally. Nuxt handles it perfectly.
    
    # Let's verify NuxtLink handles href="https..." correctly. Yes, it does.
    content = content.replace('<a ', '<NuxtLink ')
    content = content.replace('</a>', '</NuxtLink>')
    content = content.replace('<a\n', '<NuxtLink\n')
    
    # Also fix to="/#" -> to="#"
    content = re.sub(r'to="/(#.*?)"', r'to="\1"', content)

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")

process_directory('/var/www/html/zazi/zazinuxt/app')
print("Done")
