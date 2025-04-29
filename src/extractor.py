# src/extractor.py

import re
import spacy

class ThreatExtractor:
    def __init__(self):
        # Load small English NLP model
        self.nlp = spacy.load("en_core_web_sm")

    def extract_threats(self, text):
        threats = {
            "ip_addresses": self.extract_ip_addresses(text),
            "domains": self.extract_domains(text),
            "hashes": self.extract_hashes(text),
            "entities": self.extract_named_entities(text),
            "emails": self.extract_emails(text),
            "urls": self.extract_urls(text)
        }
        return threats

    def extract_ip_addresses(self, text):
        ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
        return re.findall(ip_pattern, text)

    def extract_domains(self, text):
        domain_pattern = r'\b(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}\b'
        return re.findall(domain_pattern, text)

    def extract_hashes(self, text):
        hash_pattern = r'\b[A-Fa-f0-9]{32,64}\b'
        return re.findall(hash_pattern, text)

    def extract_named_entities(self, text):
        doc = self.nlp(text)
        return [(ent.text, ent.label_) for ent in doc.ents if ent.label_ in {"ORG", "PRODUCT", "GPE"}]

    def extract_emails(self, text):
        email_pattern = r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'
        return re.findall(email_pattern, text)

    def extract_urls(self, text):
        url_pattern = r'https?://[^\s]+'
        return re.findall(url_pattern, text)
