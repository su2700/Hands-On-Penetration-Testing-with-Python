#!/usr/bin/env python
"""
🕵️ Base64 Decoder/Encoder
Just a tiny helper script to encode/decode secrets. 🔐
"""

import base64
import sys

def encode(password):
    """Encodes a string to Base64 🤐"""
    return base64.b64encode(password)

def decode(text):
    """Decodes a Base64 string 🔓"""
    return base64.b64decode(text)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Example: python Obs.py "SecretPhrase"
        print "Encoded: " + encode(sys.argv[1])
    else:
        # Test Case
        print "Decoded Test: " + decode('JCh0IUBNaXNwQER1MDE=')
