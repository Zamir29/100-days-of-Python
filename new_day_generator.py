import os
# ---------------------------------------------------------
# CONFIGURATION - Update these once per day
# ---------------------------------------------------------

# --- CONFIGURATION ---
REPO_ROOT = os.path.dirname(os.path.abspath(__file__)) # Root is going to be the file's folder, no matter the folder
LOGS_DIR = os.path.join(REPO_ROOT, "daily_logs")
TEMPLATE_PATH = os.path.join(LOGS_DIR, "template.md")
README_PATH = os.path.join(REPO_ROOT, "README.md")

# Create the folder, main.py, config.py
def create_folder_structure(day_num):
    folder_name = f"day_{day_num}"
    folder_path = os.path.join(REPO_ROOT, folder_name)

    # Defensive Coding: Check if it exists before trying to create it
    if os.path.exists(folder_path):
        print(f"⚠️  Folder {folder_name} already exists.")
        return folder_path

    os.makedirs(folder_path)
    print(f"✅ Created folder: {folder_name}/")

    # Create main.py
    main_path = os.path.join(folder_path, "main.py")
    with open(main_path, "w") as f:
        f.write(
            f"# Day {day_num} - Created automatically\n\ndef main():\n    print('Hello Day {day_num}')\n\nif __name__ == '__main__':\n    main()\n")
    print(f"   └── Created main.py")

    # Create config.py
    config_path = os.path.join(folder_path, "config.py")
    with open(config_path, "w") as f:
        f.write(
            f"import os\nfrom dotenv import load_dotenv, find_dotenv\n\nload_dotenv(find_dotenv())\n"
        )
    print(f"   └── Created config.py")

    return folder_path

# Creates and edits the template for the specific day
def create_log_file(day_num, title, goal, steps, stack):
    filename = f"day_{day_num}.md"
    output_path = os.path.join(LOGS_DIR, filename)

    if os.path.exists(output_path):
        print(f"⚠️  Log file {filename} already exists. Skipping.")
        return

    # Read Template
    try:
        with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
            template = f.read()
    except FileNotFoundError:
        print("❌ Error: Template file not found in daily_logs/template.md")
        return

    # Fill Template
    prev_day = str(int(day_num) - 1)
    next_day = str(int(day_num) + 1)

    content = template.format(
        day=day_num,
        title=title,
        goal=goal,
        steps=steps,
        stack=stack,
        prev_day=prev_day,
        next_day=next_day
    )

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Created log: daily_logs/{filename}")

# Recreates line by line the README.md file
def update_readme(day_num, title, goal, stack):
    """
    Updates the README.md file:
    1. Updates the Progress Bar number.
    2. Inserts the new day entry under '## 📚 Daily Progress'.
    """
    if not os.path.exists(README_PATH):
        print("❌ README.md not found.")
        return

    with open(README_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()

    new_lines = []
    inserted = False
    updated_bar = False

    # The entry to insert
    new_entry = [
        f"- **Day {day_num} - {title}**   \n",
        f"  [![Open Project Folder](https://img.shields.io/badge/Open-📁%20Folder-blue)](/day_{day_num}/main.py)\n",
        f"  [![Open Log File](https://img.shields.io/badge/Open-📝%20Log-orange)](/daily_logs/day_{day_num}.md)  \n",
        f"{goal}  \n",
        f"**Stack used:** {stack}\n\n",
        "<details><summary>Show all logs</summary>  \n\n"
    ]

    for line in lines:
        # 1. Update Progress Bar URL
        if "progress-bar.xyz" in line and not updated_bar:
            # Simple string replace for the previous day number to current day number
            # Using regex would be safer, but this works if format is consistent
            prev_day_int = int(day_num) - 1
            if f"/{prev_day_int}/" in line:
                line = line.replace(f"/{prev_day_int}/", f"/{day_num}/")
                print(f"✅ Updated Progress Bar to {day_num}%")
                updated_bar = True

        # 2. Remove the OLD opening tag
        # Since we added a new one in 'new_entry', we must delete the old one
        # to avoid nesting <details> inside <details>
        if "<details>" in line or "<summary>Show all logs</summary>" in line:
            # We skip appending this line to new_lines
            continue

        new_lines.append(line)

        # 2. Insert New Day Entry
        # We look for the "Last Updated" badge line, and insert AFTER it.
        if "![Last Updated]" in line and not inserted:
            new_lines.extend(new_entry)
            inserted = True
            print(f"✅ Inserted Day {day_num} entry into README")

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.writelines(new_lines)


def main():
    print("--- 🚀 100 Days Automation ---")
    day_num = input("Day Number: ").strip()
    title = input("Project Title: ").strip()
    goal = input("Goal: ").strip()
    steps = input("Steps: ").strip()
    stack = input("Tech Stack: ").strip()

    create_folder_structure(day_num)
    create_log_file(day_num, title, goal, steps, stack)
    update_readme(day_num, title, goal, stack)

    print("\n✨ Done! Happy coding.")


if __name__ == "__main__":
    main()