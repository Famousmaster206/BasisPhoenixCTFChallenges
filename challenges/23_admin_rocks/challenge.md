# The Cookie Jar

## Metadata
- ID: 23
- Difficulty: Hard
- Points: 300
- Estimated Solve Time: 3-5 minutes
- Primary Skill: Web DevTools / Cookie Manipulation
- Status: READY_FOR_TEST
- Placeholder Flag: BASIS{C00KIE_M0NST3R_77}

## Player Prompt
The admin dashboard is restricted. Only users with administrative privileges can see the secret flag. Can you find a way to "convince" the browser you are the boss?

## Hints
- Hint 1 (5 min): Open DevTools (F12) and look at the "Application" or "Storage" tab.
- Hint 2 (10 min): Look for "Cookies" in the sidebar. Do you see anything interesting like `admin=false`?
- Hint 3 (15 min): Try changing the value of the admin cookie and refreshing the page.

## Organizer Solution
- Open the site in a browser.
- Open DevTools -> Application Tab -> Cookies.
- Edit the `admin` cookie value from `false` to `true`.
- Refresh the page to reveal the flag.