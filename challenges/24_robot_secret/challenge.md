# Robots' Secret

## Metadata
- ID: 24
- Difficulty: Normal
- Points: 100
- Estimated Solve Time: 2-4 minutes
- Primary Skill: Web Enumeration / robots.txt
- Status: READY_FOR_TEST
- Placeholder Flag: BASIS{N0_B0TS_4LL0W3D}

## Player Prompt
Websites often use a special file to tell search engine "robots" which pages they aren't allowed to look at. If the robots aren't allowed there, that's exactly where we want to go.

## Hints
- Hint 1 (5 min): There is a standard file called `robots.txt` used by almost every website.
- Hint 2 (10 min): Try navigating to the URL of the site but add `/robots.txt` at the end.
- Hint 3 (15 min): Look for a "Disallow" entry in that file and visit that hidden path.

## Organizer Solution
- Visit `http://[challenge-url]/robots.txt`.
- Locate the disallowed path (e.g., `/hidden_flag_page.html`).
- Navigate to that path in the browser to see the flag.