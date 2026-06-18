# FIX: Refactored the four core game functions out of app.py into logic_utils.py
# using Claude Code (agent mode). The AI located each bug, proposed the fix, and
# I reviewed and approved the changes below.


def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty.

    Range widens as difficulty increases, so Normal is smaller than Hard.
    """
    # FIX: Normal used to be 1-100 and Hard 1-50, making Normal wider (harder)
    # than Hard. Swapped so difficulty scales correctly. (AI spotted, I confirmed.)
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 50
    if difficulty == "Hard":
        return 1, 100
    return 1, 50


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    # FIX: Refactored unchanged from app.py; collapsed the None/"" checks into one.
    if raw is None or raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    # FIX: Hints were reversed ("Too High" said "Go HIGHER"). Corrected the
    # messages and removed the broken string-comparison fallback branch.
    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number.

    A win earns more points the fewer attempts it took (minimum 10).
    Incorrect guesses do not change the score.
    """
    # FIX: Old logic awarded/penalized points erratically (e.g. "Too High" could
    # ADD points on even attempts). Now only a win scores, scaled by attempts.
    if outcome == "Win":
        points = 100 - 10 * (attempt_number - 1)
        if points < 10:
            points = 10
        return current_score + points

    return current_score
