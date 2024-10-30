
from redactor import Redactor

def test_redact_names():
    redactor = Redactor()
    doc = redactor.nlp("John Doe went to the store.")
    redacted_doc = redactor.redact_names(doc)
    assert "John" not in redacted_doc.text
    assert "Doe" not in redacted_doc.text
    assert "went to the store" in redacted_doc.text