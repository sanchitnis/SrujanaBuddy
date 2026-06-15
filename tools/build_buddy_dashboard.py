import os
import sys
import re
import json
import yaml
from pathlib import Path

# Resolve repo root
REPO_ROOT = Path(__file__).parent.parent.resolve()

def locate_srujana_memory():
    # 1. Env Var
    env_path = os.environ.get("SRUJANA_MEMORY_DIR")
    if env_path and Path(env_path).exists():
        return Path(env_path).resolve()
        
    # 2. Sibling Path (one level up from repo root)
    sibling_path = REPO_ROOT.parent / "srujana-memory"
    if sibling_path.exists():
        return sibling_path.resolve()
        
    # 3. Desktop
    desktop = Path(os.path.expanduser("~/Desktop/srujana-memory"))
    if desktop.exists():
        return desktop.resolve()
        
    # 4. OneDrive Desktop
    onedrive_desktop = Path(os.path.expanduser("~/OneDrive/Desktop/srujana-memory"))
    if onedrive_desktop.exists():
        return onedrive_desktop.resolve()
        
    return None

def parse_readme_commands():
    readme_path = REPO_ROOT / "README.md"
    commands = []
    if not readme_path.exists():
        return commands
        
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Find "Running a session" section
    match = re.search(r"##+ Running a session(.*?)(##+|$)", content, re.DOTALL | re.IGNORECASE)
    if match:
        section_text = match.group(1)
        # Find all bulleted/numbered items with commands
        for line in section_text.splitlines():
            line = line.strip()
            if line.startswith("-") or line.startswith("*") or re.match(r"^\d+\.", line):
                # Clean up bullet markers
                cleaned = re.sub(r"^[-*\d\.\s]+", "", line).strip()
                if cleaned:
                    # Check if it has a sub-bullet or nested code block
                    commands.append(cleaned)
    return commands

def check_profile_completeness(memory_dir):
    soul_path = memory_dir / "my-memory" / "soul.md"
    completeness = {
        "score": 0,
        "nudges": [],
        "fields": {
            "name": False,
            "student_id": False,
            "program": False,
            "website": False,
            "aspirations": False,
            "habits": False
        }
    }
    
    if not soul_path.exists():
        completeness["nudges"].append("Create your private profile: 'my-memory/soul.md' is missing.")
        return completeness
        
    with open(soul_path, "r", encoding="utf-8") as f:
        soul_content = f.read()
        
    # Read name
    name_match = re.search(r"Name:\s*(.+)", soul_content, re.IGNORECASE)
    if name_match and name_match.group(1).strip() and "your name" not in name_match.group(1).lower():
        completeness["fields"]["name"] = True
        completeness["score"] += 15
    else:
        completeness["nudges"].append("Identity: Please set your Name in your soul.md profile.")
        
    # Student ID
    id_match = re.search(r"Student ID:\s*(.+)", soul_content, re.IGNORECASE)
    if id_match and id_match.group(1).strip() and "your id" not in id_match.group(1).lower():
        completeness["fields"]["student_id"] = True
        completeness["score"] += 15
    else:
        completeness["nudges"].append("Identity: Please add your Student ID in your soul.md profile.")
        
    # Program / stream
    stream_match = re.search(r"Program and stream:\s*(.+)", soul_content, re.IGNORECASE)
    if stream_match and stream_match.group(1).strip():
        completeness["fields"]["program"] = True
        completeness["score"] += 15
    else:
        completeness["nudges"].append("Academics: Set your Program and stream in your soul.md profile.")
        
    # Website (Presence)
    website_match = re.search(r"(Personal Website|website|presence):\s*(.+)", soul_content, re.IGNORECASE)
    if website_match and website_match.group(2).strip() and "http" in website_match.group(2):
        completeness["fields"]["website"] = True
        completeness["score"] += 15
    else:
        completeness["nudges"].append("Srujana Presence: Add a link to your Personal website / portfolio in your soul.md profile.")

    # Aspirations
    aspirations_path = memory_dir / "my-memory" / "semantic" / "aspirations.yaml"
    if aspirations_path.exists():
        completeness["fields"]["aspirations"] = True
        completeness["score"] += 20
    else:
        completeness["nudges"].append("Aspirations: Define your goals under 'my-memory/semantic/aspirations.yaml'.")
        
    # Habits
    habits_path = memory_dir / "my-memory" / "habits" / "habits.md"
    if habits_path.exists():
        completeness["fields"]["habits"] = True
        completeness["score"] += 20
    else:
        completeness["nudges"].append("Habits: Tracking file 'my-memory/habits/habits.md' not found. Start tracking habits.")

    return completeness

def load_extra_personal_data(memory_dir):
    data = {
        "gps_map": "No active Goal Plan Sankalpa map found. Run daily planning to generate.",
        "habits": [],
        "collaborations": []
    }
    
    # 1. GPS map
    gps_path = memory_dir / "my-memory" / "semantic" / "gps-map.md"
    if gps_path.exists():
        with open(gps_path, "r", encoding="utf-8") as f:
            data["gps_map"] = f.read()
            
    # 2. Habits
    habits_path = memory_dir / "my-memory" / "habits" / "habits.md"
    if habits_path.exists():
        with open(habits_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line.startswith("- [") or line.startswith("* ["):
                    data["habits"].append(line)
                    
    # 3. Scan mentor-mentee folder
    mm_dir = memory_dir / "mentor-mentee"
    if mm_dir.exists():
        for item in mm_dir.iterdir():
            if item.is_dir():
                latest_mtime = 0
                latest_file = ""
                for subitem in item.glob("*.md"):
                    mtime = subitem.stat().st_mtime
                    if mtime > latest_mtime:
                        latest_mtime = mtime
                        latest_file = subitem.name
                if latest_file:
                    import datetime
                    dt = datetime.datetime.fromtimestamp(latest_mtime).isoformat()
                    data["collaborations"].append({
                        "folder": f"mentor-mentee/{item.name}",
                        "latest_file": latest_file,
                        "last_update": dt
                    })
                    
    return data

def build_dashboard():
    print("Building SrujanaBuddy Dashboard...")
    memory_dir = locate_srujana_memory()
    if not memory_dir:
        print("[WARNING] srujana-memory directory could not be located. Dashboard will show empty profile placeholders.")
        # Create empty template placeholder
        output_data = {
            "generic": {
                "system": "SrujanaBuddy",
                "commands": parse_readme_commands()
            },
            "personal": {
                "score": 0,
                "nudges": ["Create the 'srujana-memory' folder on your Desktop or parent directory to initialize profile tracking."],
                "fields": {},
                "gps_map": "Please set up srujana-memory to see your active GPS Map.",
                "habits": [],
                "collaborations": []
            }
        }
    else:
        completeness = check_profile_completeness(memory_dir)
        personal_data = load_extra_personal_data(memory_dir)
        
        output_data = {
            "generic": {
                "system": "SrujanaBuddy",
                "commands": parse_readme_commands()
            },
            "personal": {
                "score": completeness["score"],
                "nudges": completeness["nudges"],
                "fields": completeness["fields"],
                "gps_map": personal_data["gps_map"],
                "habits": personal_data["habits"],
                "collaborations": personal_data["collaborations"]
            }
        }
        
    web_dir = REPO_ROOT / "web"
    web_dir.mkdir(exist_ok=True)
    
    with open(web_dir / "buddy-data.json", "w", encoding="utf-8") as f:
        json.dump(output_data, f, indent=2)
        
    print(f"SrujanaBuddy dashboard data successfully written to {web_dir / 'buddy-data.json'}")

if __name__ == "__main__":
    build_dashboard()
