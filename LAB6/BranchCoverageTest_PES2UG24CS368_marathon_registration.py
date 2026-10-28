
import pytest

from marathon_registration import (
    entry_fee,
    start_wave,
    finisher_status,
)


@pytest.mark.parametrize(
    ("race", "age", "early_bird", "tshirt", "expected"),
    [
        ("5k", 30, False, False, 500),
        ("10k", 30, True, False, 600),
        ("half", 30, False, True, 1500),
        ("full", 70, True, True, 975),
        ("5k", 65, False, False, 250),
        ("10k", 65, True, False, 300),
    ],
)
def test_entry_fee_valid_paths(
    race, age, early_bird, tshirt, expected
):
    assert entry_fee(race, age, early_bird, tshirt) == expected


def test_entry_fee_unknown_race_branch():
    with pytest.raises(ValueError, match="unknown race"):
        entry_fee("ultra", 30, False, False)


def test_entry_fee_under_12_branch():
    with pytest.raises(ValueError, match="too young"):
        entry_fee("5k", 11, False, False)


def test_entry_fee_short_race_skips_long_distance_age_check():
    assert entry_fee("5k", 17, False, False) == 500


@pytest.mark.parametrize("race", ["half", "full"])
def test_entry_fee_long_race_under_18_branch(race):
    with pytest.raises(ValueError, match="too young for this distance"):
        entry_fee(race, 17, False, False)


def test_entry_fee_long_race_age_18_branch():
    assert entry_fee("half", 18, False, False) == 1200


@pytest.mark.parametrize(
    ("time", "race", "expected"),
    [
        (None, "full", "D"),
        (180, "full", "A"),
        (200, "full", "B"),
        (241, "full", "C"),
        (90, "10k", "A"),
        (100, "10k", "B"),
        (121, "10k", "C"),
    ],
)
def test_start_wave_branches(time, race, expected):
    assert start_wave(time, race) == expected


def test_finisher_disqualification_branch():
    assert finisher_status(400, "full", 1) == "DSQ"


@pytest.mark.parametrize(
    ("race", "elapsed", "expected"),
    [
        ("full", 360, "finisher"),
        ("full", 361, "DNF"),
        ("half", 180, "finisher"),
        ("half", 181, "DNF"),
        ("5k", 90, "finisher"),
        ("5k", 91, "DNF"),
        ("10k", 90, "finisher"),
        ("10k", 91, "DNF"),
    ],
)
def test_finisher_time_branches(race, elapsed, expected):
    assert finisher_status(elapsed, race, 0) == expected
