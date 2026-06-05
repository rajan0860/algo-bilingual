#!/usr/bin/env python3
import os
import sys
import re
import argparse

# Define valid categories and their pretty names
CATEGORIES = {
    "arrays": "Arrays",
    "linked-list": "Linked List",
    "stacks-queues": "Stacks & Queues",
    "trees": "Trees",
    "graphs": "Graphs",
    "binary-search": "Binary Search",
    "sliding-window": "Sliding Window",
    "two-pointers": "Two Pointers",
    "dynamic-programming": "Dynamic Programming",
    "backtracking": "Backtracking",
    "sorting": "Sorting"
}

DIFFICULTIES = ["Easy", "Medium", "Hard"]

def to_snake_case(name):
    # Convert "Two Sum", "Two-Sum", "TwoSum" to "two_sum"
    s = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', name)
    s = re.sub(r'[^a-zA-Z0-9]', '_', s)
    return re.sub(r'_+', '_', s).lower().strip('_')

def parse_args():
    parser = argparse.ArgumentParser(description="Scaffold a new DSA problem in Python and Go.")
    parser.add_argument("-c", "--category", choices=list(CATEGORIES.keys()), help="Problem category folder")
    parser.add_argument("-n", "--name", help="Problem name (e.g. 'Two Sum')")
    parser.add_argument("-d", "--difficulty", choices=DIFFICULTIES, help="Problem difficulty")
    return parser.parse_args()

def prompt_interactive():
    print("=== Algo-Bilingual Problem Scaffolder ===")
    
    # 1. Select Category
    categories_list = list(CATEGORIES.keys())
    print("\nSelect a category:")
    for idx, (cat, pretty) in enumerate(CATEGORIES.items(), 1):
        print(f"  {idx}. {pretty} ({cat})")
    
    while True:
        try:
            choice = input(f"Select category (1-{len(categories_list)}): ").strip()
            choice_idx = int(choice) - 1
            if 0 <= choice_idx < len(categories_list):
                category = categories_list[choice_idx]
                break
        except ValueError:
            pass
        print("Invalid choice. Please select a valid number.")

    # 2. Problem Name
    while True:
        name = input("\nEnter problem name (e.g., 'Two Sum'): ").strip()
        if name:
            break
        print("Problem name cannot be empty.")

    # 3. Difficulty
    print("\nSelect difficulty:")
    for idx, diff in enumerate(DIFFICULTIES, 1):
        print(f"  {idx}. {diff}")
    
    while True:
        try:
            choice = input(f"Select difficulty (1-3): ").strip()
            choice_idx = int(choice) - 1
            if 0 <= choice_idx < len(DIFFICULTIES):
                difficulty = DIFFICULTIES[choice_idx]
                break
        except ValueError:
            pass
        print("Invalid choice. Please select 1, 2, or 3.")

    return category, name, difficulty

def create_boilerplate_files(category, problem_name, snake_name, difficulty):
    target_dir = os.path.join(category, snake_name)
    os.makedirs(target_dir, exist_ok=True)

    # 1. Create solution.py
    py_path = os.path.join(target_dir, "solution.py")
    py_content = f'''def solve() -> None:
    """
    Problem: {problem_name}
    Difficulty: {difficulty}
    Category: {CATEGORIES[category]}
    """
    # TODO: Implement solution
    pass

if __name__ == "__main__":
    # Add your test cases or run validation here
    solve()
    print("Python solution ran successfully!")
'''
    if not os.path.exists(py_path):
        with open(py_path, "w") as f:
            f.write(py_content)
        print(f"Created: {py_path}")
    else:
        print(f"File already exists (skipped): {py_path}")

    # 2. Create solution.go
    go_path = os.path.join(target_dir, "solution.go")
    go_content = f'''package main

import "fmt"

// solve runs the solution logic
func solve() {{
	// TODO: Implement solution
	fmt.Println("Solution not implemented yet.")
}}

func main() {{
	solve()
	fmt.Println("Go solution ran successfully!")
}}
'''
    if not os.path.exists(go_path):
        with open(go_path, "w") as f:
            f.write(go_content)
        print(f"Created: {go_path}")
    else:
        print(f"File already exists (skipped): {go_path}")

    # 3. Create notes.md
    notes_path = os.path.join(target_dir, "notes.md")
    notes_content = f'''# {problem_name}

| Pattern | Time Complexity | Space Complexity | Difficulty |
|---|---|---|---|
| TODO | O(N) | O(1) | {difficulty} |

---

## Approach
*Provide a step-by-step breakdown of the logic before coding.*

1. 
2. 

## Key Differences

| Python 🐍 | Go ⚡ |
|---|---|
| *dynamic / simple* | *strongly typed / explicit* |

## Gotchas & Edge Cases
- 

---

## Resources
- **Problem Link:** [LeetCode]()
- **Status:** ⏳ In Progress
'''
    if not os.path.exists(notes_path):
        with open(notes_path, "w") as f:
            f.write(notes_content)
        print(f"Created: {notes_path}")
    else:
        print(f"File already exists (skipped): {notes_path}")

def update_readme(category, problem_name, snake_name, difficulty):
    readme_path = "README.md"
    if not os.path.exists(readme_path):
        print("Warning: README.md not found. Progress tracker was not updated.")
        return

    with open(readme_path, "r") as f:
        content = f.read()

    # Find the START and END comments of the tracker
    start_tag = "<!-- START_TRACKER -->"
    end_tag = "<!-- END_TRACKER -->"

    if start_tag not in content or end_tag not in content:
        print("Warning: Tracker markers not found in README.md. Progress tracker was not updated.")
        return

    # Locate indices of tags
    start_idx = content.find(start_tag)
    end_idx = content.find(end_tag)

    if start_idx == -1 or end_idx == -1 or start_idx >= end_idx:
        print("Warning: Tracker markers not found in README.md. Progress tracker was not updated.")
        return

    # Extract all rows currently in the tracker
    tracker_section = content[start_idx + len(start_tag):end_idx].strip()
    rows = [r.strip() for r in tracker_section.split("\n") if r.strip()]

    # Calculate index (e.g. 001, 002...)
    count = len(rows)
    index_str = f"{count + 1:03d}"

    # Build the link relative to root
    relative_link = f"./{category}/{snake_name}/"
    pretty_category = CATEGORIES[category]

    # Form the new markdown table row
    # Column format: | # | Problem | Category | Python 🐍 | Go ⚡ | Notes 📝 | Difficulty |
    new_row = f"| {index_str} | [{problem_name}]({relative_link}) | {pretty_category} | ⏳ In Progress | ❌ Todo | ❌ Todo | {difficulty} |"
    
    # Avoid duplicate registrations
    if any(problem_name in r for r in rows):
        print(f"Problem '{problem_name}' already registered in README.md. Skipped registration.")
        return

    # Add the new row to the list of rows
    rows.append(new_row)

    # Rebuild the tracker block
    new_tracker_content = f"\n" + "\n".join(rows) + "\n"
    new_content = content[:start_idx + len(start_tag)] + new_tracker_content + content[end_idx:]

    with open(readme_path, "w") as f:
        f.write(new_content)
    print(f"Updated README.md: Added problem '{problem_name}' to the Progress Tracker.")

def main():
    args = parse_args()
    
    # Use args if provided, otherwise fallback to interactive prompts
    if args.category and args.name and args.difficulty:
        category = args.category
        name = args.name
        difficulty = args.difficulty
    else:
        category, name, difficulty = prompt_interactive()

    snake_name = to_snake_case(name)
    
    print(f"\nScaffolding project:")
    print(f"  Category:   {category} ({CATEGORIES[category]})")
    print(f"  Name:       {name} (folder: {snake_name})")
    print(f"  Difficulty: {difficulty}")
    print("-" * 40)

    create_boilerplate_files(category, name, snake_name, difficulty)
    update_readme(category, name, snake_name, difficulty)
    
    print("\n🎉 Scaffolding completed successfully!")

if __name__ == "__main__":
    main()
