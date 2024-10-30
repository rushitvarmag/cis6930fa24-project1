import pytest
from redactor import Redactor
from io import StringIO
import sys

@pytest.fixture
def redactor():
    return Redactor()

def test_write_stats_to_stdout(capsys, redactor):
    redactor.stats = {'names': 3, 'dates': 2, 'phones': 1, 'addresses': 1, 'concepts': 2}
    redactor.write_stats("stdout")
    captured = capsys.readouterr()
    assert "Names: 3" in captured.out
    assert "Dates: 2" in captured.out
    assert "Phones: 1" in captured.out
    assert "Addresses: 1" in captured.out
    assert "Concepts: 2" in captured.out

def test_write_stats_to_stderr(capsys, redactor):
    redactor.stats = {'names': 4, 'dates': 1, 'phones': 0, 'addresses': 1, 'concepts': 3}
    redactor.write_stats("stderr")
    captured = capsys.readouterr()
    assert "Names: 4" in captured.err
    assert "Dates: 1" in captured.err
    assert "Phones: 0" in captured.err
    assert "Addresses: 1" in captured.err
    assert "Concepts: 3" in captured.err

def test_write_stats_to_file(tmp_path, redactor):
    redactor.stats = {'names': 2, 'dates': 3, 'phones': 1, 'addresses': 0, 'concepts': 1}
    output_file = tmp_path / "stats_output.txt"
    redactor.write_stats(str(output_file))

    with open(output_file, 'r') as f:
        content = f.read()
    
    assert "Names: 2" in content
    assert "Dates: 3" in content
    assert "Phones: 1" in content
    assert "Addresses: 0" in content
    assert "Concepts: 1" in content