import re
import os

file_path = 'REVA-STUDENT-SYSTEM-SPEC.md'

with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Order matters for "Course coach" vs "Course Coach" if we want to be precise, 
# but usually "Course Buddy" is the replacement for both capitalized versions.

# "Course Coach" -> "Course Buddy"
text = re.sub(r'Course Coach', 'Course Buddy', text)
# "Course coach" -> "Course Buddy"
text = re.sub(r'Course coach', 'Course Buddy', text)
# "Course Coaches" -> "Course Buddies"
text = re.sub(r'Course Coaches', 'Course Buddies', text)
# "Course coaches" -> "Course Buddies"
text = re.sub(r'Course coaches', 'Course Buddies', text)
# "course-coach" -> "course-buddy"
text = re.sub(r'course-coach', 'course-buddy', text)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Replacement done for REVA-STUDENT-SYSTEM-SPEC.md")
