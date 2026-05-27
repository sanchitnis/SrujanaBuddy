# Video Resume Script Generator — Plugin Skill

## Skill Name
`generate-video-resume-script`

## Description
Generates a concise, ready-to-record 2-minute video resume script for any applicant (student or experienced professional) based on their experience, achievements, and target role.

---

## Inputs Required
- Applicant name (optional)
- Experience level (e.g., Fresher, 2 years, Senior, etc.)
- Key achievements (bulleted or short phrases)
- Target role or job title
- Top skills (optional)

---

## Output
- Markdown-formatted script (approx. 250–300 words)
- Structure: Introduction, Experience Summary, Key Skills, Achievements, Closing
- Recording instructions for the applicant

---

## Usage Flow
1. Prompt user for required inputs (see above).
2. Generate a personalized script using the template below.
3. Output the script in Markdown, ready for the applicant to record.

---

## Script Template

```
# 2-Minute Video Resume Script

Hello, my name is [Applicant Name].

I am applying for the role of [Target Role]. With [Experience Level] experience, I have developed strong skills in [Top Skills or Domain].

Some of my key achievements include:
- [Achievement 1]
- [Achievement 2]
- [Achievement 3]

I am passionate about [brief motivation or value statement]. My experience has taught me to [short reflection on growth or learning].

Thank you for considering my application. I look forward to the opportunity to contribute to your team.
```

---

## Recording Instructions
- Find a quiet, well-lit space.
- Practice the script a few times for natural delivery.
- Keep your video under 2 minutes.
- Speak clearly and confidently.
- Dress professionally.

---

## Implementation Notes
- This skill can be invoked from the CV-for-Role workflow or as a standalone tool.
- All applicant-facing prompts and outputs must use inclusive language (not student-specific).
- The script should be concise, positive, and tailored to the applicant’s real experience.
- If any input is missing, prompt the user to provide it.

---

## Example Output

```
# 2-Minute Video Resume Script

Hello, my name is Priya Sharma.

I am applying for the role of Data Analyst. With 3 years of experience, I have developed strong skills in data visualization, SQL, and business analytics.

Some of my key achievements include:
- Led a project to automate reporting, reducing manual effort by 40%
- Presented insights to senior management, influencing key business decisions
- Achieved certification in Advanced Excel and Power BI

I am passionate about turning data into actionable insights. My experience has taught me to approach problems analytically and work collaboratively.

Thank you for considering my application. I look forward to the opportunity to contribute to your team.
```
