# Basis Phoenix CTF Challenges

short version:

- challenges are already scaffolded and have starter files
- the placeholder website is https://ctf-7jvj5.ondigitalocean.app
- someone else will connect the website to this repo content

## What is already done

- 12 challenges are planned and scaffolded under [challenges](challenges)
- each challenge has `challenge.md` and a `files` folder with starter assets
- [challenges.txt](challenges.txt) has the full list and builder notes
- [platform/challenges.manifest.json](platform/challenges.manifest.json) has the machine-readable list

## What the next builder should do

1. Open one challenge folder at a time.
2. Replace placeholder flags in each `challenge.md` with the real flag for that challenge.
3. Test the challenge from scratch like a student would.
4. Tighten hints if they are too easy or too hard.

## How this should connect to the website

Whoever owns the website can either:

- read from [platform/challenges.manifest.json](platform/challenges.manifest.json) and pull each challenge file automatically, or
- copy the challenge text manually into the site.

Important:

- real answer checking should happen on backend/server side
- do not expose correct flags in frontend code

## Tone and difficulty target

- audience: middle school students
- target event time: around 45-90 minutes
- maybe most teams should solve 6-8 challenges
- advanced teams should solve more, especially with the bonus chain
