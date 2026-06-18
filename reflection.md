# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

What did the game look like the first time you ran it?
- The difficulty was set to "Normal."
- The target number range was defined as 1 to 100.
- The total "Attempts allowed" was 8.

List at least two concrete bugs you noticed at the start  
- The game does not return to a fresh state after clicking "New Game." Even though the secret number changes, the user is forced to manually refresh the page.
- The hints operate in reverse.
- The number range for "Normal" difficulty should be smaller than the range for "Hard" difficulty.
- An attempt is recorded immediately upon starting a new game, before a guess is even submitted

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|     Submit Guess (Check Hint)  |  If the guess is lower than the secret, the hint should say "Too Low". If higher, it should say "Too High"                 | The hint logic operates in reverse, misdirecting the user.                | None                       |
|Click "New Game" (after playing)       | The game state fully resets: History clears, attempts return to 0, and a new secret is generated without requiring a page reload.                  |  The secret number changes in the background, but the UI state does not reset. A manual page refresh is forced.               |   None                     |
|"Normal" and "Hard" Difficulty      | The Guess number range for "Normal" should be strictly smaller than the range for "Hard".                 |The "Normal" range is larger than the "Hard" range, breaking difficulty scaling              |     None                   |
|Page Load / Click "New Game" |The game initializes a fresh state. Attempt count should be 0 with an empty history array |An attempt is recorded immediately (Attempts: 1), reducing available attempts before any guess is submitted.|None|

---

## 2. How did you use AI as a teammate?

I mainly used Claude Code in agent mode inside VS Code. Instead of asking it to "fix the game," I first had it read `app.py` and `reflection.md` together and point me to the exact line where each bug I had already noticed actually lived, which kept me in control of what changed. One suggestion that was correct: it found that on every other attempt the code ran `secret = str(st.session_state.secret)` and passed a string into `check_guess`, which silently broke the number comparison; I verified this by tracing the `attempts % 2 == 0` branch and seeing that comparing an int to a string is what triggered the reversed/erratic hints. One suggestion that was misleading at first: it initially proposed only swapping the "Go HIGHER"/"Go LOWER" text in `check_guess`, which would have fixed the wording but left the deeper string-cast bug in `app.py` untouched, so the hints would still go wrong on even attempts. I caught this by actually walking through a sample game in my head, which showed the text fix alone wasn't enough.

## 3. Debugging and testing your fixes

I decided a bug was really fixed only after I could reproduce the original broken behavior and then confirm the same input now behaved correctly, not just because the code "looked right." For example, after fixing the range bug I checked that "Normal" returned `1, 50` and "Hard" returned `1, 100`, so Normal is now strictly smaller than Hard. I also ran `python -m py_compile app.py logic_utils.py` to confirm both files still compiled after the refactor, which caught nothing this time but gave me confidence the imports were wired correctly. AI helped me by suggesting concrete inputs to test (like submitting a guess on the 2nd attempt to hit the even-attempt branch) and by reminding me to verify the "New Game" button by checking that history, score, and status all actually reset, not just the secret.

## 4. What did you learn about Streamlit and state?

I'd explain it like this: every time you click a button or type something, Streamlit re-runs the entire script from top to bottom, like refreshing a page. Because of that, any normal variable gets wiped and recreated on each run, so the game would forget the secret number and your score instantly. `st.session_state` is a special box that survives those re-runs, so that's where you store things you want to remember between clicks. The "New Game" bug made this click for me: changing `st.session_state.secret` worked, but I had to also reset `history`, `score`, and `status` in session state, because the re-run kept the old values and the leftover `status == "won"` froze the board.

## 5. Looking ahead: your developer habits

One habit I want to reuse is reproducing a bug and writing down its expected vs. actual behavior *before* I change any code, like I did in the Bug Reproduction Log, it stopped me from "fixing" things that weren't actually broken. One thing I'd do differently next time is write a quick test case before changing code, so I can confirm the fix addresses the actual bug and not just the symptoms. Overall this project taught me that AI-generated code can look polished and "production-ready" while quietly containing several real bugs, so I now treat AI output as a draft to verify rather than an answer to trust.
