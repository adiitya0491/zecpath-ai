from screening_ai.robust_flow import detect_edge_case


def test_missing():

    result = detect_edge_case(
        "",
        1.0
    )

    assert result == "missing"


def test_poor_audio():

    result = detect_edge_case(
        "hello",
        0.4
    )

    assert result == "poor_audio"


def test_language_mix():

    result = detect_edge_case(
        "hai chetta i have 2 years experience",
        1.0
    )

    assert result == "language_mix"


def test_incomplete():

    result = detect_edge_case(
        "yes",
        1.0
    )

    assert result == "incomplete"


def test_valid():

    result = detect_edge_case(
        "I have 3 years of experience in Python development",
        1.0
    )

    assert result == "valid"