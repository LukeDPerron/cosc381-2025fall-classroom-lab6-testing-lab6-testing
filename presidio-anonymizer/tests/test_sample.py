import pytest
from presidio_anonymizer.sample import sample_run_anonymizer

def test_sample_run_anonymizer():
    # replace the following line with your test
    expected_outcome = {
    'text': 'My name is BIP.',
     'items':
     [
       {'start': 11, 'end': 14, 'entity_type': 'PERSON', 'text': 'BIP', 'operator': 'replace'}
     ]
    }
    
    result = sample_run_anonymizer("My name is Bond.", 11, 15)

    assert result.text == expected_outcome["text"]
    assert result.items[0].start == expected_outcome["items"][0]["start"]
    assert result.items[0].end == expected_outcome["items"][0]["end"]
    assert result.items[0].entity_type == expected_outcome["items"][0]["entity_type"]
    assert result.items[0].text == expected_outcome["items"][0]["text"] 
    assert result.items[0].operator == expected_outcome["items"][0]["operator"]

    pass