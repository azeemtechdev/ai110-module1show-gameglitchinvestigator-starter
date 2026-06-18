from logic_utils import check_guess, get_range_for_difficulty, update_score


# check_guess returns a tuple: (outcome, message)

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    # If secret is 50 and guess is 60, outcome should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    # If secret is 50 and guess is 40, outcome should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"


# --- Targeted regression tests for the bugs we fixed ---

def test_too_high_hint_tells_user_to_go_lower():
    """Bug: hints were reversed. A guess that is too high must tell the
    user to go LOWER, not HIGHER."""
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message.upper()
    assert "HIGHER" not in message.upper()


def test_too_low_hint_tells_user_to_go_higher():
    """Bug: hints were reversed. A guess that is too low must tell the
    user to go HIGHER, not LOWER."""
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message.upper()
    assert "LOWER" not in message.upper()


def test_normal_range_is_smaller_than_hard_range():
    """Bug: Normal's range (1-100) was wider than Hard's (1-50), which
    inverted difficulty scaling. Normal must be strictly smaller than Hard."""
    _, normal_high = get_range_for_difficulty("Normal")
    _, hard_high = get_range_for_difficulty("Hard")
    assert normal_high < hard_high


def test_wrong_guess_does_not_change_score():
    """Bug: update_score could ADD points on a wrong ('Too High') guess.
    Only a win should change the score."""
    assert update_score(0, "Too High", 2) == 0
    assert update_score(0, "Too Low", 3) == 0


def test_win_awards_more_points_for_fewer_attempts():
    """A win on an earlier attempt should score at least as high as a
    later one (never negative or zero growth for the first win)."""
    early = update_score(0, "Win", 1)
    late = update_score(0, "Win", 5)
    assert early > 0
    assert early >= late
