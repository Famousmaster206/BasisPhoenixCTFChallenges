# Base Conversion

## Metadata

- ID: 16
- Difficulty: Medium
- Points: 200
- Estimated Solve Time: 6-10 minutes
- Primary Skill: Recognize decoding techniques
- Status: READY_FOR_TEST
- Placeholder Flag: BASIS{100101}

## Player Prompt

You found a secret message encoded in numbers:

1011 (base 2)
17 (base 8)
B (base 16)

All three numbers represent the same value in different bases.

Task:

Convert all three numbers to decimal.

Add them together.

Convert the sum to binary.

The resulting binary number is the flag.

Submit your answer in the format:

BASIS{binary_sum}

## Hints

- Hint 1 (5 min): What is Base 2 of 1011?
- Hint 2 (10 min): 17 (base 8) and B (base 16) have the same decimal value.
- Hint 3 (15 min): The final binary is just the sum of base 2 of 1011, base 8 of 17, and base 16 of B.

## Organizer Solution

- Convert all numbers to decimal: 
	Base 2 1011 → 11

	Base 8 17 → 15

	Base 16 B → 11
- Add the decimals (11+15+11) = 37
- To binary 37 -> 100101
- Final Flag: BASIS{100101}
