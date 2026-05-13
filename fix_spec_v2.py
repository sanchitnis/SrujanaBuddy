import re
import os

file_path = 'REVA-STUDENT-SYSTEM-SPEC.md'

with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Case-insensitive replacement with preserving case of the first letters if possible,
# but usually mapping to "Course Buddy" or "Course Buddies" or "course buddy" etc.

def replace_course_coach(match):
    m = match.group(0)
    if 'coaches' in m.lower():
        if m.startswith('Course Coach') or m.startswith('Course coach'): return 'Course Buddies'
        if m.startswith('COURSE COACH'): return 'COURSE BUDDIES'
        return 'course buddies'
    else:
        if m.startswith('Course Coach') or m.startswith('Course coach'): return 'Course Buddy'
        if m.startswith('COURSE COACH'): return 'COURSE BUDDY'
        return 'course buddy'

text = re.sub(r'[Cc]ourse [Cc]oaches?', replace_course_coach, text)
text = re.sub(r'course-coach', 'course-buddy', text)
text = re.sub(r'Course-Coach', 'Course-Buddy', text)
text = re.sub(r'Course-coach', 'Course-Buddy', text)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Replacement (v2) done for REVA-STUDENT-SYSTEM-SPEC.md")
