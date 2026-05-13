import os
import re

def replace_all(text):
    # Handle "Course Coach" variations
    text = re.sub(r'Course Coach', 'Course Buddy', text)
    text = re.sub(r'Course coach', 'Course Buddy', text)
    text = re.sub(r'course coach', 'course buddy', text)
    text = re.sub(r'COURSE COACH', 'COURSE BUDDY', text)
    
    # Handle "course-coach" variations
    text = re.sub(r'course-coach', 'course-buddy', text)
    text = re.sub(r'Course-Coach', 'Course-Buddy', text)
    text = re.sub(r'Course-coach', 'Course-Buddy', text)
    text = re.sub(r'COURSE-COACH', 'COURSE-BUDDY', text)

    # Handle "course_coach" variations
    text = re.sub(r'course_coach', 'course_buddy', text)
    text = re.sub(r'Course_Coach', 'Course_Buddy', text)
    
    return text

files_to_update = [
    r'D:\Github\SrujanaBuddy\REVA-STUDENT-SYSTEM-SPEC.md',
    r'D:\Github\SrujanaBuddy\eval\leaderboards\README.md',
]

for file_path in set(files_to_update):
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = replace_all(content)
        
        if content != new_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated: {file_path}")
        else:
            print(f"No changes in: {file_path}")
    else:
        print(f"File not found: {file_path}")
