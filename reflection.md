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

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
