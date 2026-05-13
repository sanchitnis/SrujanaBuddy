import os

renames = [
    (r'D:\Github\SrujanaBuddy\agents\course-coach-builder.md', r'D:\Github\SrujanaBuddy\agents\course-buddy-builder.md'),
    (r'D:\Github\SrujanaBuddy\agents\course-coach-template.md', r'D:\Github\SrujanaBuddy\agents\course-buddy-template.md'),
    (r'D:\Github\SrujanaBuddy\agents\course-coaches\_course-coach-instance-template.md', r'D:\Github\SrujanaBuddy\agents\course-coaches\_course-buddy-instance-template.md'),
]

# Add course-coach-XX.md files
instances_dir = r'D:\Github\SrujanaBuddy\agents\course-coaches\instances'
if os.path.exists(instances_dir):
    for f in os.listdir(instances_dir):
        if 'course-coach' in f:
            old_path = os.path.join(instances_dir, f)
            new_path = os.path.join(instances_dir, f.replace('course-coach', 'course-buddy'))
            renames.append((old_path, new_path))

# Finally rename directories
renames.append((r'D:\Github\SrujanaBuddy\agents\course-coaches', r'D:\Github\SrujanaBuddy\agents\course-buddies'))
renames.append((r'D:\Github\SrujanaBuddy\tools\course-coach-builder', r'D:\Github\SrujanaBuddy\tools\course-buddy-builder'))

for old, new in renames:
    if os.path.exists(old):
        # Ensure parent directory of new exists if it's not the same
        new_dir = os.path.dirname(new)
        if not os.path.exists(new_dir):
            os.makedirs(new_dir)
        
        os.rename(old, new)
        print(f"Renamed: {old} -> {new}")
    else:
        print(f"Not found: {old}")
