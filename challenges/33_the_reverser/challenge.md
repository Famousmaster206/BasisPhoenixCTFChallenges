# The Reverser

## Metadata
- ID: 36
- Difficulty: Easy
- Points: 50
- Estimated Solve Time: 2-3 minutes
- Primary Skill: Pattern Recognition / String Manipulation
- Status: READY_FOR_TEST
- Placeholder Flag: BASIS{this_is_backwards}

## Player Prompt
We found a string of text that looks like a flag, but the formatting is all wrong. It's almost as if someone looked at the flag in a mirror. Can you fix it?

`}sdrawkcab_si_siht{SISAB`

## Hints
- Hint 1 (5 min): Look closely at the "BASIS" part. Does it look familiar but flipped?
- Hint 2 (10 min): Try reading the string from right to left instead of left to right.
- Hint 3 (15 min): You can use an online "Text Reverser" or write a one-line Python script: `print("string"[::-1])`.

## Organizer Solution
- Recognize that the text is the flag written backwards.
- Reverse the string `}sdrawkcab_si_siht{SISAB` to get `BASIS{this_is_backwards}`.