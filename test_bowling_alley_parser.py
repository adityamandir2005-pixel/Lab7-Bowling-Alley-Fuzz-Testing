from hypothesis import given, example, strategies as st
from bowling_alley_parser import format_player_name, parse_frame, parse_scoreboard


def assert_does_not_crash(function, value):
    try:
        result = function(value)
    except Exception as exc:
        assert False, f"{function.__name__} crashed for {value!r}: {type(exc).__name__}: {exc}"
    return result


@given(st.text() | st.none())
@example(None)
@example("")
def test_format_player_name_handles_arbitrary_input(value):
    result = assert_does_not_crash(format_player_name, value)
    assert isinstance(result, str)
    assert len(result) <= 10


def test_format_player_name_normalizes_and_handles_invalid_input():
    assert format_player_name("  aSHA  ") == "Asha"
    assert format_player_name(None) == ""


@given(st.text() | st.none())
@example(None)
@example("")
@example("X?")
def test_parse_frame_handles_arbitrary_input(value):
    result = assert_does_not_crash(parse_frame, value)
    assert isinstance(result, tuple) and len(result) == 2
    first, second = result
    assert isinstance(first, int) and isinstance(second, int)
    assert 0 <= first <= 10 and 0 <= second <= 10
    assert first + second <= 10


def test_parse_frame_parses_notation_and_rejects_invalid_frames():
    assert parse_frame("X") == (10, 0)
    assert parse_frame("7/") == (7, 3)
    assert parse_frame("45") == (4, 5)
    assert parse_frame("") == (0, 0)
    assert parse_frame("X?") == (0, 0)
    assert parse_frame("99") == (0, 0)


@given(st.text() | st.none())
@example(None)
@example("")
@example("Asha:")
def test_parse_scoreboard_handles_arbitrary_input(value):
    result = assert_does_not_crash(parse_scoreboard, value)
    assert isinstance(result, dict)
    for name, score in result.items():
        assert isinstance(name, str) and name
        assert isinstance(score, int) and 0 <= score <= 300


def test_parse_scoreboard_skips_malformed_entries():
    assert parse_scoreboard("Asha:150,bad,Ravi:132,Cal:301,Jo:0") == {
        "Asha": 150,
        "Ravi": 132,
        "Jo": 0,
    }
    assert parse_scoreboard(None) == {}


def test_parse_scoreboard_parses_valid_entries():
    assert parse_scoreboard("Asha:150,Ravi:132") == {"Asha": 150, "Ravi": 132}
