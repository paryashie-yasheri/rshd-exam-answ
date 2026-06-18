import re, subprocess

with open('README.md', 'r') as f:
    content = f.read()

bt = chr(96)
pattern = bt * 3 + 'mermaid\n(.*?)' + bt * 3

blocks = re.findall(pattern, content, re.DOTALL)

for i, block in enumerate(blocks):
    with open(f'/tmp/mmd_{i}.mmd', 'w') as f:
        f.write(block.strip())
    subprocess.run([
        'mmdc', '-i', f'/tmp/mmd_{i}.mmd',
        '-o', f'images/mermaid_{i}.png',
        '-p', 'puppeteer-config.json',
        '-w', '800'
    ], check=True)

def repl(m):
    idx = blocks.index(m.group(1))
    return f'![Mermaid diagram](images/mermaid_{idx}.png)'

content = re.sub(pattern, repl, content, flags=re.DOTALL)

with open('README-processed.md', 'w') as f:
    f.write(content)
