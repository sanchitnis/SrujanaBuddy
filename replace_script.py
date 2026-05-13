import os
import re

replacements = [
    (re.compile(re.escape('Course Coach'), re.IGNORECASE), lambda m: 'Course Buddy' if m.group(0)[0].isupper() and m.group(0).split()[1][0].isupper() else 'Course Buddy'), # Default to Course Buddy for capitalized
    (re.compile(re.escape('course coach')), 'course buddy'),
    (re.compile(re.escape('COURSE COACH')), 'COURSE BUDDY'),
    (re.compile(re.escape('Course coach')), 'Course Buddy'),
    (re.compile(re.escape('course-coach')), 'course-buddy'),
    (re.compile(re.escape('Course-Coach')), 'Course-Buddy'),
    (re.compile(re.escape('Course-coach')), 'Course-Buddy'),
    (re.compile(re.escape('COURSE-COACH')), 'COURSE-BUDDY'),
]

# More robust replacement function
def replace_all(text):
    # Order matters: more specific/longer first if they overlap, but these don't much except for casing
    
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
    r'D:\Github\SrujanaBuddy\GEMINI.md',
    r'D:\Github\SrujanaBuddy\MANIFEST.md',
    r'D:\Github\SrujanaBuddy\REVA-METRICS-TRACKER.md',
    r'D:\Github\SrujanaBuddy\REVA-STUDENT-SYSTEM-SPEC.md',
    r'D:\Github\SrujanaBuddy\SKILL-legacy.md',
    r'D:\Github\SrujanaBuddy\SKILL.md',
    r'D:\Github\SrujanaBuddy\agents\course-coach-builder.md',
    r'D:\Github\SrujanaBuddy\agents\course-coach-template.md',
    r'D:\Github\SrujanaBuddy\agents\course-coaches\README.md',
    r'D:\Github\SrujanaBuddy\agents\course-coaches\_course-coach-instance-template.md',
    r'D:\Github\SrujanaBuddy\agents\course-coaches\instances\course-coach-02.md',
    r'D:\Github\SrujanaBuddy\agents\course-coaches\instances\course-coach-03.md',
    r'D:\Github\SrujanaBuddy\agents\course-coaches\instances\course-coach-04.md',
    r'D:\Github\SrujanaBuddy\agents\course-coaches\instances\course-coach-05.md',
    r'D:\Github\SrujanaBuddy\agents\course-coaches\instances\course-coach-06.md',
    r'D:\Github\SrujanaBuddy\agents\course-coaches\instances\course-coach-07.md',
    r'D:\Github\SrujanaBuddy\agents\course-coaches\instances\course-coach-08.md',
    r'D:\Github\SrujanaBuddy\agents\course-coaches\instances\course-coach-09.md',
    r'D:\Github\SrujanaBuddy\agents\course-coaches\instances\course-coach-10.md',
    r'D:\Github\SrujanaBuddy\agents\course-coaches\instances\course-coach-gcs.md',
    r'D:\Github\SrujanaBuddy\agents\course-coaches\instances\CSE GCS\skill.md',
    r'D:\Github\SrujanaBuddy\agents\course-coaches\streams\cse-template.md',
    r'D:\Github\SrujanaBuddy\agents\course-coaches\streams\ece-template.md',
    r'D:\Github\SrujanaBuddy\agents\course-coaches\streams\mba-template.md',
    r'D:\Github\SrujanaBuddy\knowledge\README.md',
    r'D:\Github\SrujanaBuddy\profiles\_mentee-profile-template.md',
    r'D:\Github\SrujanaBuddy\references\ai-tutor-philosophy.md',
    r'D:\Github\SrujanaBuddy\review\dr-anand\REVA-STUDENT-SYSTEM-SPEC.md',
    r'D:\Github\SrujanaBuddy\review\dr-anand\SKILL.md',
    r'D:\Github\SrujanaBuddy\tools\course-coach-builder\build.py',
    r'D:\Github\SrujanaBuddy\tools\course-coach-builder\eval_bridge.py',
    r'D:\Github\SrujanaBuddy\tools\course-coach-builder\README.md',
    r'D:\Github\SrujanaBuddy\tools\course-coach-builder\skill_generator.py',
    r'D:\Github\SrujanaBuddy\tools\course-coach-builder\wiki_generator.py',
    r'D:\Github\SrujanaBuddy\tools\course-coach-builder\workbook_generator.py',
    r'D:\Github\SrujanaBuddy\tools\course-coach-builder\templates\course-descriptor.md',
    r'D:\Github\SrujanaBuddy\CHANGELOG.md',
    r'D:\Github\SrujanaBuddy\REVA-ACCEPTANCE-EVIDENCE.md',
    r'D:\Github\SrujanaBuddy\agents\README.md',
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
