# Nested Text File

## Metadata
- ID: 30
- Difficulty: Boss
- Points: 500
- Estimated Solve Time: 5-10 minutes
- Primary Skill: File Extraction / Persistence
- Status: READY_FOR_TEST
- Placeholder Flag: BASIS{Z1P_1NS1D3_A_Z1P}

## Player Prompt
We found a suspicious ZIP file. Inside was another ZIP file. And inside that? You guessed it. How deep does the rabbit hole go?

## Hints
- Hint 1 (5 min): You'll need to extract the files repeatedly.
- Hint 2 (10 min): There are 10 layers in total. Keep going!
- Hint 3 (15 min): You can do this manually, but a true hacker might write a simple script to unzip everything at once.

## Organizer Solution
- Unzip `layer1.zip`.
- Unzip the resulting `layer2.zip` inside it.
- Repeat until `flag.txt` is revealed in the final layer.