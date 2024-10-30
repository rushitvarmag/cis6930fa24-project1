
import pytest
from redactor import Redactor
import spacy
from io import StringIO
import os

@pytest.fixture
def redactor():
    return Redactor()

def test_redact_names(redactor):
    doc = redactor.nlp("John Doe went to the store.")
    redacted_doc = redactor.redact_names(doc)
    assert "John" not in redacted_doc.text
    assert "Doe" not in redacted_doc.text
    assert "went to the store" in redacted_doc.text

def test_redact_dates(redactor):
    doc = redactor.nlp("The meeting is on January 15, 2025.")
    redacted_doc = redactor.redact_dates(doc)
    assert "January 15, 2025" not in redacted_doc.text
    assert "The meeting is on" in redacted_doc.text

def test_redact_phones(redactor):
    doc = redactor.nlp("Call me at 123-456-7890 or (987) 654-3210.")
    redacted_doc = redactor.redact_phones(doc)
    assert "123-456-7890" not in redacted_doc.text
    assert "(987) 654-3210" not in redacted_doc.text
    assert "Call me at" in redacted_doc.text
    assert "or" in redacted_doc.text

def test_redact_address(redactor):
    doc = redactor.nlp("I live at 123 Main St, New York, NY 10001.")
    redacted_doc = redactor.redact_address(doc)
    assert "New York" not in redacted_doc.text
    assert "I live at" in redacted_doc.text

def test_redact_concepts(redactor):
    doc = redactor.nlp("The secret project is about AI. We must keep it confidential.")
    redacted_doc = redactor.redact_concepts(doc, ["secret", "confidential"])
    assert "The secret project is about AI." not in redacted_doc.text
    assert "We must keep it confidential." not in redacted_doc.text

def test_process_file(redactor, tmp_path):
    input_file = tmp_path / "input.txt"
    input_file.write_text("John Doe's phone is 123-456-7890.")
    output_dir = tmp_path / "output"
    output_dir.mkdir()

    class Args:
        names = True
        dates = False
        phones = True
        address = False
        concept = None

    redactor.process_file(str(input_file), str(output_dir), Args())

    output_file = output_dir / "input.txt.censored"
    assert output_file.exists()
    content = output_file.read_text()
    assert "John Doe" not in content
    assert "123-456-7890" not in content
    assert "phone is" in content

def test_error_handling_in_process_file(redactor, tmp_path):
    output_dir = tmp_path / "output"
    output_dir.mkdir()
    # Create a path that doesn't exist
    non_existent_file = tmp_path / "non_existent_file.txt"

    class Args:
        names = True
        dates = False
        phones = True
        address = False
        concept = None

    try:
        redactor.process_file(str(non_existent_file), str(output_dir), Args())
    except Exception as e:
        assert "Error processing file" in str(e)