

import pytest
from src.extractor import ThreatExtractor

@pytest.fixture
def sample_text():
    return """
    Attackers used IP addresses 192.168.0.1 and 10.0.0.8.
    They registered domains like malware-example.com and badsite.net.
    A suspicious file had the hash d41d8cd98f00b204e9800998ecf8427e.
    Reports mention Russia and Germany.
    Contact: security@cybermail.com
    More info: https://malicious.example.com/attack-info
    """

def test_extract_threats(sample_text):
    extractor = ThreatExtractor()
    threats = extractor.extract_threats(sample_text)

    assert "192.168.0.1" in threats["ip_addresses"]
    assert "10.0.0.8" in threats["ip_addresses"]

    assert "malware-example.com" in threats["domains"]
    assert "badsite.net" in threats["domains"]

    assert "d41d8cd98f00b204e9800998ecf8427e" in threats["hashes"]

    assert ("Russia", "GPE") in threats["entities"]
    assert ("Germany", "GPE") in threats["entities"]

    assert "security@cybermail.com" in threats["emails"]

    assert "https://malicious.example.com/attack-info" in threats["urls"]
