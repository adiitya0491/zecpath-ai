def adjust_difficulty(current_level, answer_quality):

    levels = [
        "basic",
        "intermediate",
        "advanced"
    ]

    index = levels.index(current_level)

    if answer_quality == "good" and index < 2:
        return levels[index + 1]

    if answer_quality == "poor" and index > 0:
        return levels[index - 1]

    return current_level


if __name__ == "__main__":

    print(
        adjust_difficulty(
            "basic",
            "good"
        )
    )

    print(
        adjust_difficulty(
            "advanced",
            "poor"
        )
    )