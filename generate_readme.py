#!/usr/bin/env python3
# README.md Generator Script

README_CONTENT = "# My Project\n\nA brief description of your project.\n\n## Modules:\n"

for module in ['user', 'product']:
    with open(f"my_project/models/{module}.py", 'r') as f:
        for line in f:
            if '# README:' in line:
                comment = line.split('README:')[1].strip()
                README_CONTENT += f"- {comment}\n"

with open("README.md", 'w') as f:
    f.write(README_CONTENT)
