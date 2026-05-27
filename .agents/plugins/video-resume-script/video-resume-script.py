# Video Resume Script Generator — Implementation (Python T0/T2)

"""
Tier: T0/T2 (Deterministic, no LLM required)
This script generates a 2-minute video resume script for any applicant based on user input.
"""

import textwrap

def generate_video_resume_script(name, experience, achievements, target_role, skills=None, motivation=None, reflection=None):
    script = f"""# 2-Minute Video Resume Script\n\nHello, my name is {name or '[Your Name]'}.\n\nI am applying for the role of {target_role or '[Target Role]'}. With {experience or '[Experience Level]'} experience, I have developed strong skills in {skills or '[Top Skills or Domain]'}.\n\nSome of my key achievements include:\n"""
    for ach in achievements:
        script += f"- {ach}\n"
    script += f"\nI am passionate about {motivation or '[your motivation or value statement]'}. My experience has taught me to {reflection or '[your growth or learning]'}\n\nThank you for considering my application. I look forward to the opportunity to contribute to your team.\n"
    return textwrap.dedent(script)

if __name__ == "__main__":
    print("Video Resume Script Generator\n")
    name = input("Applicant Name: ")
    experience = input("Experience Level (e.g., Fresher, 2 years): ")
    target_role = input("Target Role: ")
    skills = input("Top Skills (comma separated): ")
    print("Enter up to 3 key achievements (press Enter to skip):")
    achievements = []
    for i in range(3):
        ach = input(f"Achievement {i+1}: ")
        if ach:
            achievements.append(ach)
    motivation = input("Motivation/Value Statement: ")
    reflection = input("Growth/Learning Reflection: ")
    print("\n---\n")
    print(generate_video_resume_script(name, experience, achievements, target_role, skills, motivation, reflection))
    print("\n---\n")
    print("Recording Tips:\n- Find a quiet, well-lit space.\n- Practice the script a few times.\n- Keep your video under 2 minutes.\n- Speak clearly and confidently.\n- Dress professionally.\n")
