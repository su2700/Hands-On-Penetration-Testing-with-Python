#!/usr/bin/env python
"""
🐦 Tweet Parser Sample
Simple script to parse JSON tweets line by line.
"""

import sys
import json
import fileinput
# Assuming this module exists in the local directory structure
try:
    from tweet_parser.tweet import Tweet
except ImportError:
    print "⚠️  'tweet_parser' module missing. This script might not run."
    # Mock class for demo if missing
    class Tweet:
        def __init__(self, data): self.all_text = str(data)

class TwitterDumpReader:
    def __init__(self, file_name):
        self.file = file_name

    def parse(self):
        print "📂 Reading Tweets from: " + self.file
        count = 0
        
        # Reads from file or stdin
        for line in fileinput.input(self.file):
            try:
                tweet_dict = json.loads(line)
                tweet = Tweet(tweet_dict)
                
                print "🐦 Tweet: " + tweet.all_text
                count += 1
            except Exception:
                continue
        
        print "\n✅ Processed " + str(count) + " tweets."

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Usage: python sample.py <tweets.json>"
    else:
        reader = TwitterDumpReader(sys.argv[1])
        reader.parse()
