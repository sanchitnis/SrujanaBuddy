"""Strip MARP-specific markup and produce a plain Markdown file."""
import re

src = r'd:\Github\SrujanaBuddy\review\srujanabuddy-leadership-demo-v1.0.md'

with open(src, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Remove MARP frontmatter block (everything between the first --- and second ---)
text = re.sub(r'^---\n.*?^---\n', '', text, count=1, flags=re.DOTALL | re.MULTILINE)

# 2. Remove MARP slide class directives like <!-- _class: lead -->
text = re.sub(r'<!--\s*_class:[^>]*-->\n?', '', text)

# 3. Convert <div class="chat-student"> ... </div> to blockquote with label
def replace_chat_student(m):
    inner = m.group(1).strip()
    return f'> **[Student]** {inner}\n'

text = re.sub(
    r'<div class="chat-student">\s*(.*?)\s*</div>',
    replace_chat_student,
    text,
    flags=re.DOTALL
)

# 4. Convert <div class="chat-buddy"> ... </div> to blockquote with label
def replace_chat_buddy(m):
    inner = m.group(1).strip()
    return f'> **[SrujanaBuddy]** {inner}\n'

text = re.sub(
    r'<div class="chat-buddy">\s*(.*?)\s*</div>',
    replace_chat_buddy,
    text,
    flags=re.DOTALL
)

# 5. Convert <div class="placeholder"> ... </div> to a plain note blockquote
def replace_placeholder(m):
    inner = m.group(1).strip()
    return f'> 📌 *{inner}*\n'

text = re.sub(
    r'<div class="placeholder">\s*(.*?)\s*</div>',
    replace_placeholder,
    text,
    flags=re.DOTALL
)

# 6. Add a plain title at the very top
title = '# SrujanaBuddy — Leadership Demo\n**REVA University AI Coaching Companion**  \nMay 14, 2026 · First Floor Boardroom, Admin Block\n\n'
text = title + text.lstrip()

# 7. Collapse runs of 3+ blank lines down to 2
text = re.sub(r'\n{4,}', '\n\n\n', text)

with open(src, 'w', encoding='utf-8') as f:
    f.write(text)

print('Done. File updated.')
