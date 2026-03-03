# Welcome Flag

## Metadata

- ID: 13
- Difficulty: Medium
- Points: 100
- Estimated Solve Time: 4-6 minutes
- Primary Skill: Decode Base64
- Status: READY_FOR_TEST
- Placeholder Flag: BASIS{REPLACE_ME_13}

## Player Prompt

You are given a string that has been encoded multiple times using Base64. Decode it as many times as needed until you get the flag.

## Hints

- Hint 1 (5 min): Try decoding the string from Base64. Does the output still look encoded?
- Hint 2 (10 min): Keep decoding until the output looks readable.
- Hint 3 (15 min): If your decoded text still ends in = or looks like random letters and numbers, it’s probably another Base64 layer.

## Organizer Solution

- Student opens `secretencodedstring.txt`.
- Student decodes the string using Base64
- Student observes that the string is still encoded
- Student continues decoding until the result is readable text.
