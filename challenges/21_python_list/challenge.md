# Python List

## Metadata

- ID: 21
- Difficulty: Stretch
- Points: 150
- Estimated Solve Time: 10-12 minutes
- Primary Skill: Python / Decoding Techniques
- Status: READY_FOR_TEST
- Placeholder Flag: BASIS{HELLO_PYTHON}

## Player Prompt

You found a Python Script called flaglist.py


Task:

Look at the flag_codes list.

Convert the numbers to ASCII characters using Python’s chr() function.

Join them to get the flag.

## Hints

- Hint 1 (5 min): Each number represents an ASCII code.
- Hint 2 (10 min): Use "".join([chr(c) for c in flag_codes]) to reveal the flag.
- Hint 3 (15 min): Running the script also prints the flag.

## Organizer Solution

- Look at the flag_codes list: [66, 65, 83, 73, 83, 123, 72, 69, 76, 76, 79, 95, 80, 89, 84, 72, 79, 78, 125]
- Convert each to ASCII: [chr(c) for c in flag_codes]  
 -> ['B','A','S','I','S','{','H','E','L','L','O','_','P','Y','T','H','O','N','}']
- Join them: flag = "BASIS{HELLO_PYTHON}"
