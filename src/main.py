# src/main.py

import argparse
import json
from extractor import ThreatExtractor

def main():
    parser = argparse.ArgumentParser(description="Extract threats from text file.")
    parser.add_argument('--input', type=str, required=True, help="Path to input text file.")
    parser.add_argument('--output', type=str, required=True, help="Path to output JSON file.")
    args = parser.parse_args()

    with open(args.input, 'r', encoding='utf-8') as file:
        text = file.read()

    extractor = ThreatExtractor()
    threats = extractor.extract_threats(text)

    with open(args.output, 'w', encoding='utf-8') as out_file:
        json.dump(threats, out_file, indent=4)

    print(f"Threats extracted and saved to {args.output}")

if __name__ == "__main__":
    main()
