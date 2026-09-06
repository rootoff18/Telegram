import re, glob

files = glob.glob("TMessagesProj/src/main/res/values*/strings.xml")
pattern = re.compile(r'(<string\s+name="[^"]*"[^>]*>)(.*?)(</string>)', re.DOTALL)

def repl(m):
    open_tag, text, close_tag = m.groups()
    new_text = text.replace("Telegram", "VerdGram")
    return open_tag + new_text + close_tag

for path in files:
    with open(path, encoding="utf-8") as f:
        content = f.read()
    new_content = pattern.sub(repl, content)
    if new_content != content:
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print("patched:", path)
