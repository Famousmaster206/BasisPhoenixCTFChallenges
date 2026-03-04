import os
import json
import re

output = {}
challenge_number = 4  # since you already did 1-3

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

        if not (name_match and points_match and flag_match and desc_match):
            continue

        name = name_match.group(1).strip()
        description = desc_match.group(1).strip().replace("\n\n", "\n")
        points = int(points_match.group(1))
        flag = flag_match.group(1).strip()

        output[f"Challenge{challenge_number}"] = {
            "name": name,
            "description": description,
            "points": points,
            "flag": flag
        }

        challenge_number += 1

with open("challenges.json", "w", encoding="utf-8") as f:
    json.dump(output, f, indent=4)

print("challenges.json created")