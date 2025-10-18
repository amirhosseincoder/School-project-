import os
import re

TEMPLATES_DIR = "templates"

def process_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()


    if "{% load static %}" not in content:
        content = "{% load static %}\n" + content


    content = re.sub(r'src="([^"]+)"', lambda m: f'src="{{% static \'{m.group(1)}\' %}}"', content)


    content = re.sub(r'href="([^"]+)"', lambda m: f'href="{{% static \'{m.group(1)}\' %}}"', content)


    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✅ Updated: {filepath}")


for root, dirs, files in os.walk(TEMPLATES_DIR):
    for file in files:
        if file.endswith(".html"):
            filepath = os.path.join(root, file)
            process_file(filepath)