# Sungur: Threat Intelligence Extractor

# Sungur: Threat Intelligence Extractor

![Tests Passing](https://img.shields.io/badge/tests-passing-brightgreen)


**Sungur** is a lightweight, AI-powered tool for extracting cybersecurity threat intelligence from unstructured text sources. It uses natural language processing (NLP) techniques to detect potential threats, vulnerabilities, indicators of compromise (IOCs), and security-related keywords.

## Features
- Named Entity Recognition (NER) for cybersecurity-related entities.
- Extraction of key Indicators of Compromise (IOCs):
  - IP addresses
  - Domain names
  - Hash values (MD5, SHA-1, SHA-256)
  - Email addresses
  - URLs
- Pre-trained lightweight model for fast and efficient processing.
- Simple command-line interface (CLI) and modular Python code.

## Threats Extracted

| Threat Type | Description |
|:---|:---|
| IP Address | IPv4 addresses such as `192.168.1.1` |
| Domain | Domain names like `example.com` |
| Hash | Hash strings (32-64 hex characters) |
| Entity | Named entities like organizations and countries |
| Email | Email addresses like `user@example.com` |
| URL | Links starting with `http://` or `https://` |

## Installation

```bash
git clone https://github.com/yourusername/sungur.git
cd sungur
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

## Usage

```bash
python src/main.py --input examples/sample_text.txt --output extracted_threats.json
```

## Folder Structure

```
sungur/
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── extractor.py
│   └── utils.py
│
├── examples/
│   └── sample_text.txt
│
├── tests/
│   └── test_extractor.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

## Requirements

- Python 3.9+
- Huggingface Transformers
- spaCy
- scikit-learn

## License

This project is licensed under the MIT License.
