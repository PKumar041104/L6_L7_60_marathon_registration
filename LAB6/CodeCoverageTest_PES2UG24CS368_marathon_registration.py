
import pytest

from marathon_registration import (
    entry_fee,
    start_wave,
    finisher_status,
)


@pytest.mark.parametrize(
    ("race", "expected"),
    [
        ("5k", 500),
        ("10k", 800),
        ("half", 1200),
        ("full", 1800),
    ],
)
def test_standard_entry_fees(race, expected):
    assert entry_fee(race, 30, False, False) == expected


def test_unknown_race():
    with pytest.raises(ValueError, match="unknown race"):
        entry_fee("ultra", 30, False, False)


def test_age_below_minimum():
    with pytest.raises(ValueError, match="too young"):
        entry_fee("5k", 11, False, False)


@pytest.mark.parametrize("race", ["half", "full"])
def test_underage_long_distance(race):
    with pytest.raises(ValueError, match="too young for this distance"):
        entry_fee(race, 17, False, False)


def test_age_12_is_accepted_for_5k():
    assert entry_fee("5k", 12, False, False) == 500


def test_age_18_is_accepted_for_half_marathon():
    assert entry_fee("half", 18, False, False) == 1200


def test_early_bird_discount():
    assert entry_fee("10k", 30, True, False) == 600


def test_senior_discount_at_65():
    assert entry_fee("10k", 65, False, False) == 400


def test_tshirt_surcharge():
    assert entry_fee("5k", 30, False, True) == 800


def test_combined_discounts_and_tshirt():
    assert entry_fee("10k", 65, True, True) == 600


def test_early_bird_discount_rounding():
    assert entry_fee("5k", 30, True, False) == 375


def test_no_discount_for_age_64():
    assert entry_fee("10k", 64, False, False) == 800


def test_start_wave_without_time():
    assert start_wave(None, "full") == "D"


@pytest.mark.parametrize(
    ("time", "race", "expected"),
    [
        (180, "full", "A"),
        (181, "full", "B"),
        (240, "full", "B"),
        (241, "full", "C"),
        (90, "10k", "A"),
        (91, "10k", "B"),
        (120, "10k", "B"),
        (121, "10k", "C"),
    ],
)
def test_start_wave_decisions(time, race, expected):
    assert start_wave(time, race) == expected


def test_missed_checkpoint_disqualifies_runner():
    assert finisher_status(60, "5k", 1) == "DSQ"


def test_multiple_missed_checkpoints_disqualify_runner():
    assert finisher_status(60, "full", 2) == "DSQ"


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
def test_finisher_status_time_limits(race, elapsed, expected):
    assert finisher_status(elapsed, race, 0) == expected
