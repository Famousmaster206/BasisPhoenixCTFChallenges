# Vigenere Vault

## Metadata
- ID: 32
- Difficulty: Boss
- Points: 500
- Estimated Solve Time: 5-8 minutes
- Primary Skill: Cryptography / Vigenère Cipher
- Status: READY_FOR_TEST
- Placeholder Flag: BASIS{TH3_V1G3N3R3_V4ULT}

## Player Prompt
The Caesar cipher was too easy, so we upgraded to something stronger. This ciphertext requires a "Key" to unlock. We heard a rumor that the key was written in "Invisible Ink" somewhere else in the lab...

**Ciphertext:** `QOEWA{XW3_M1Y3B3Z3_M4SML}`

## Hints
- Hint 1 (5 min): This is a Vigenère Cipher. Unlike Caesar, it uses a keyword to shift letters by different amounts.
- Hint 2 (10 min): You need the secret key from Challenge 45 (Invisible Ink). (The key is `PHOENIX`).
- Hint 3 (15 min): Use an online tool like CyberChef and search for the "Vigenère Decode" recipe. Plug in the ciphertext and the key.

## Organizer Solution
- Obtain the key `PHOENIX` from Challenge 45.
- Use a Vigenère decoder with the ciphertext `QOEWA{XW3_M1Y3B3Z3_M4SML}` and the key `PHOENIX`.
- The decoded result reveals the flag.