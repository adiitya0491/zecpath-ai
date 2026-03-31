from parsers.resume_reader import extract_resume_text
from parsers.text_cleaner import clean_text


def test_resume_extraction():
    """
    Test whether resume text is extracted properly.
    """

    sample_file = "data/resumes/sample.pdf"

    text = extract_resume_text(sample_file)

    # Check text is not empty
    assert text is not None
    assert len(text) > 50


def test_resume_cleaning():
    """
    Test whether extracted text is cleaned correctly.
    """

    dirty_text = "• SKILLS Python @@@ SQL"

    cleaned = clean_text(dirty_text)

    # Ensure unwanted symbols removed
    assert "@" not in cleaned
    assert "Python" in cleaned
