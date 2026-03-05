import os
import json
import re

output = [] #json list instead of a json dictionary
challenge_number = 0

for root, dirs, files in os.walk("."):
    if "challenge.md" in files:
        path = os.path.join(root, "challenge.md")

        with open(path, encoding="utf-8") as f:
            text = f.read()

        # challenge name (first markdown title)
        name_match = re.search(r"# (.*)", text)

        # points
        points_match = re.search(r"Points:\s*(\d+)", text)

        # placeholder flag
        flag_match = re.search(r"Placeholder Flag:\s*(.*)", text)

        # player prompt section
        desc_match = re.search(
            r"## Player Prompt\s*([\s\S]*?)\n##",
            text
        )

        Hints = re.search(
            r"## Hints\s*([\s\S]*?)\n##",
            text
        )

        if not (Hints):
            continue

        Hints = Hints.group(1).strip().replace("\n\n", "\n")
        HintList = Hints.split("\n")

        if not (name_match and points_match and flag_match and desc_match):
            continue

        name = name_match.group(1).strip()
        description = desc_match.group(1).strip().replace("\n\n", "\n")
        points = int(points_match.group(1))
        flag = flag_match.group(1).strip()

        output.append({
            "name": name,
            "description": description,
            "points": points,
            "flag": flag,
            "hints": {
                "hint1": HintList[0][18:].strip() if len(HintList) > 0 else "",
                "hint2": HintList[1][18:].strip() if len(HintList) > 1 else "",
                "hint3": HintList[2][18:].strip() if len(HintList) > 2 else ""
            }
        })

with open("challenges&hints.json", "w", encoding="utf-8") as f:
    json.dump(output, f, indent=4)

print("challenges&hints.json created")





