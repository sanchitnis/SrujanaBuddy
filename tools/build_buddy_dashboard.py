import os
import sys
import re
import json
from pathlib import Path

# Resolve repo root
REPO_ROOT = Path(__file__).parent.parent.resolve()

def locate_srujana_memory():
    # 1. Env Var
    env_path = os.environ.get("SRUJANA_MEMORY_DIR")
    if env_path and Path(env_path).exists():
        return Path(env_path).resolve()
        
    # 2. Walk up parent directory tree from REPO_ROOT and current directory to find srujana-memory
    search_starts = [REPO_ROOT, Path.cwd()]
    for start in search_starts:
        curr = start.resolve()
        # Traverse up to the drive root
        while curr != curr.parent:
            # Check if it's a child here or a sibling
            sibling = curr / "srujana-memory"
            if sibling.exists() and sibling.is_dir():
                return sibling.resolve()
            sibling_sibling = curr.parent / "srujana-memory"
            if sibling_sibling.exists() and sibling_sibling.is_dir():
                return sibling_sibling.resolve()
            curr = curr.parent
            
    # 3. Fallbacks to Desktop/OneDrive Desktop
    fallbacks = [
        Path(os.path.expanduser("~/Desktop/srujana-memory")),
        Path(os.path.expanduser("~/OneDrive/Desktop/srujana-memory")),
        Path(os.path.expanduser("~/OneDrive - REVA University/Desktop/srujana-memory"))
    ]
    for path in fallbacks:
        if path.exists() and path.is_dir():
            return path.resolve()
            
    return None

def parse_skill_routing():
    skill_path = REPO_ROOT / "SKILL.md"
    plugins = [
        {"name": "Academics", "description": "Courses, concept mastery, and exam preparation", "commands": []},
        {"name": "Aspirations", "description": "Goal Plan Sankalpa (GPS) and career pathways", "commands": []},
        {"name": "Wellbeing", "description": "Stress management, energy checks, and Kaizen", "commands": []}
    ]
    if not skill_path.exists():
        return plugins
        
    with open(skill_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Find Session Type Routing table
    match = re.search(r"##+ Session Type Routing(.*?)(##+|$)", content, re.DOTALL | re.IGNORECASE)
    if not match:
        return plugins
        
    table_text = match.group(1)
    for line in table_text.splitlines():
        if "|" in line and not line.strip().startswith("|-") and "Primary Agent" not in line and "Session Type" not in line:
            parts = [p.strip() for p in line.split("|") if p.strip()]
            if len(parts) >= 2:
                session_type = parts[1]
                agent = parts[2] if len(parts) > 2 else ""
                
                # Dynamic grouping
                category = "Academics"
                agent_lower = agent.lower()
                if "gps" in agent_lower or "svadharma" in agent_lower or "career" in agent_lower or "presence" in agent_lower or "aspiration" in agent_lower or "portfolio" in agent_lower or "enterprising" in agent_lower:
                    category = "Aspirations"
                elif "wellbeing" in agent_lower or "mastery" in agent_lower or "life" in agent_lower or "escalation" in agent_lower or "triage" in agent_lower:
                    category = "Wellbeing"
                    
                for p in plugins:
                    if p["name"] == category:
                        p["commands"].append({
                            "command": session_type,
                            "description": f"Guided coaching using {agent}"
                        })
    return plugins

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

def parse_soul_metadata(soul_path):
    metadata = {
        "name": "Unknown Student",
        "role": "Student Member",
        "school": "School of Computer Science and Engineering",
        "orcid": "None",
        "user_type": "student"
    }
    if not soul_path.exists():
        return metadata
        
    with open(soul_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    name_match = re.search(r"Name:\s*(.+)", content, re.IGNORECASE)
    if name_match:
        metadata["name"] = name_match.group(1).strip()
        
    id_match = re.search(r"Student ID:\s*(.+)", content, re.IGNORECASE)
    if id_match:
        metadata["orcid"] = id_match.group(1).strip()
        
    stream_match = re.search(r"Program and stream:\s*(.+)", content, re.IGNORECASE)
    if stream_match:
        metadata["role"] = stream_match.group(1).strip()
        
    school_match = re.search(r"School:\s*(.+)", content, re.IGNORECASE)
    if school_match:
        metadata["school"] = school_match.group(1).strip()
        
    type_match = re.search(r"(User Type|type):\s*(.+)", content, re.IGNORECASE)
    if type_match:
        metadata["user_type"] = type_match.group(2).strip()
        
    return metadata

def read_markdown_file(path, fallback=""):
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    return fallback

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
                        "type": "mentor-mentee",
                        "folder": f"mentor-mentee/{item.name}",
                        "latest_file": latest_file,
                        "last_update": dt
                    })
                    
    return data

def build_dashboard():
    print("Building SrujanaBuddy Dashboard...")
    memory_dir = locate_srujana_memory()
    if not memory_dir:
        print("[WARNING] srujana-memory directory could not be located. Dashboard generation halted.")
        return
        
    completeness = check_profile_completeness(memory_dir)
    personal_data = load_extra_personal_data(memory_dir)
    soul_meta = parse_soul_metadata(memory_dir / "my-memory" / "soul.md")
    
    # Paths for other semantic logs
    recent_path = memory_dir / "my-memory" / "episodic" / "recent.md"
    aspirations_path = memory_dir / "my-memory" / "semantic" / "aspirations.yaml"
    
    output_data = {
        "generic": {
            "system": "SrujanaBuddy",
            "plugins": parse_skill_routing()
        },
        "personal": {
            "name": soul_meta["name"],
            "role": soul_meta["role"],
            "school": soul_meta["school"],
            "orcid": soul_meta["orcid"],
            "score": completeness["score"],
            "nudges": completeness["nudges"],
            "fields": completeness["fields"],
            "gps_map": personal_data["gps_map"],
            "habits": personal_data["habits"],
            "collaborations": personal_data["collaborations"],
            "recent": read_markdown_file(recent_path, "No recent sessions logged."),
            "aspirations": read_markdown_file(aspirations_path, "No aspirations defined.")
        }
    }
    
    # 1. Write the backup JSON
    dest_json = memory_dir / "my-memory" / "buddy-data.json"
    with open(dest_json, "w", encoding="utf-8") as f:
        json.dump(output_data, f, indent=2)
        
    # 2. Read HTML template from repository
    template_file = REPO_ROOT / "web" / "student_index.html"
    if template_file.exists():
        with open(template_file, "r", encoding="utf-8") as f:
            template_content = f.read()
            
        # Replace the json string placeholder in the template
        embedded_str = json.dumps(output_data, indent=2)
        replaced_content = template_content.replace("/*DASHBOARD_DATA_PLACEHOLDER*/", embedded_str)
        
        dest_html = memory_dir / "my-memory" / "student_index.html"
        with open(dest_html, "w", encoding="utf-8") as f:
            f.write(replaced_content)
        print(f"SrujanaBuddy Student HTML portal written to {dest_html}")
    else:
        print(f"[WARNING] Student HTML template not found at {template_file}")

if __name__ == "__main__":
    build_dashboard()
