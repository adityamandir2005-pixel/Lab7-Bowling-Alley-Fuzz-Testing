def format_player_name(name):
    """Return a trimmed, title-cased name limited to the scoreboard width.

    Unexpected non-string values produce an empty name instead of crashing.
    """
    if not isinstance(name, str):
        return ""
    return name.strip().title()[:10]


def parse_frame(text):
    """Parse a strike, spare, or open-frame notation.

    Invalid input safely produces (0, 0).
    """
    if not isinstance(text, str):
        return (0, 0)
    value = text.strip().upper()
    if value == "X":
        return (10, 0)
    if len(value) != 2:
        return (0, 0)
    first, second = value
    if first not in "0123456789":
        return (0, 0)
    first_pins = int(first)
    if second == "/":
        return (first_pins, 10 - first_pins)
    if second not in "0123456789":
        return (0, 0)
    second_pins = int(second)
    if first_pins + second_pins > 10:
        return (0, 0)
    return (first_pins, second_pins)


def parse_scoreboard(text):
    """Parse valid NAME:SCORE entries; ignore malformed or out-of-range entries.

    Bowling scores are limited to 0..300. Invalid input safely produces an
    empty dictionary, and malformed entries do not invalidate valid neighbors.
    """
    if not isinstance(text, str):
        return {}
    scores = {}
    for entry in text.split(","):
        name, separator, score_text = entry.partition(":")
        name = name.strip()
        score_text = score_text.strip()
        if not separator or not name or not score_text:
            continue
        if any(char not in "0123456789" for char in score_text):
            continue
        score = int(score_text)
        if score <= 300:
            scores[name] = score
    return scores


def main():
    print("==== Running format_player_name ====")
    value = input("Enter a player name for the scoreboard: ")
    print("Scoreboard name:", format_player_name(value))

    print("\n==== Running parse_frame ====")
    value = input("Enter a frame as X (strike), 7/ (spare) or two digits (e.g. 45): ")
    print("Pins (first roll, second roll):", parse_frame(value))

    print("\n==== Running parse_scoreboard ====")
    value = input("Enter scores as NAME:SCORE separated by commas (e.g. Asha:150,Ravi:132): ")
    print("Scoreboard:", parse_scoreboard(value))


if __name__ == "__main__":
    main()
