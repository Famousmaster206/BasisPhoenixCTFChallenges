# ROT13 Classic

## Metadata
- ID: 35
- Difficulty: Easy
- Points: 50
- Estimated Solve Time: 3-5 minutes
- Primary Skill: Cryptography / ROT13
- Status: READY_FOR_TEST
- Placeholder Flag: BASIS{N0T_S0_S3CR3T_R0T}

## Player Prompt
We intercepted a message that looks like complete gibberish: `ONFVF{A0G_F0_F3PE3G_E0G}`. It looks like it might be a simple rotation cipher. Can you shift the letters back?

## Hints
- Hint 1 (5 min): This is a Caesar Cipher with a shift of 13.
- Hint 2 (10 min): In ROT13, 'A' becomes 'N' and 'N' becomes 'A'. 
- Hint 3 (15 min): Search for an "Online ROT13 Decoder" to solve this instantly.

## Organizer Solution
- Copy the encrypted string.
- Use a tool like CyberChef or a ROT13 website to decode it.
- The decoded text reveals the flag.