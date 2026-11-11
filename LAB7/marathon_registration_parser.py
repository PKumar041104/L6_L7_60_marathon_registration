
def format_bib_name(name):
    """
    Formats a runner's name for the race bib.
    Returns an uppercase name limited to 12 characters.
    Returns None for invalid or empty input.
    """
    if not isinstance(name, str):
        return None

    name = name.strip()

    if not name:
        return None

    return name.upper()[:12]


def parse_finish_time(text):
    """
    Converts a finish time in H:MM:SS format into seconds.
    Returns None for invalid input.
    """
    if not isinstance(text, str):
        return None

    parts = text.strip().split(':')

    if len(parts) != 3:
        return None

    if not all(part.isascii() and part.isdigit() for part in parts):
        return None

    try:
        hours, minutes, seconds = map(int, parts)
    except (ValueError, OverflowError):
        return None

    if minutes >= 60 or seconds >= 60:
        return None

    return hours * 3600 + minutes * 60 + seconds


def average_split(text):
    """
    Calculates the average of space-separated split times.
    Returns None for invalid or empty input.
    """
    if not isinstance(text, str):
        return None

    values = text.split()

    if not values:
        return None

    if not all(value.isascii() and value.isdigit() for value in values):
        return None

    try:
        splits = [int(value) for value in values]
    except (ValueError, OverflowError):
        return None

    return sum(splits) / len(splits)


def main():
    print("==== Running format_bib_name ====")
    value = input("Enter the name to print on the bib: ")
    result = format_bib_name(value)
    print("Bib name:", result if result is not None else "Invalid name")

    print("\n==== Running parse_finish_time ====")
    value = input("Enter a finish time as H:MM:SS (e.g. 3:45:10): ")
    result = parse_finish_time(value)
    print("Finish time in seconds:", result if result is not None else "Invalid finish time")

    print("\n==== Running average_split ====")
    value = input("Enter your 5 km split times in minutes separated by spaces (e.g. 25 26 24): ")
    result = average_split(value)
    print("Average split (minutes):", result if result is not None else "Invalid split times")


if __name__ == "__main__":
    main()
