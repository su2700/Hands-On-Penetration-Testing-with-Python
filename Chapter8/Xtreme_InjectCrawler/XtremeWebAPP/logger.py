"""
📝 Xtreme Logger
Logs events with style and timestamps! 🕰️
"""

import time
import sys

class Logger(object):
    """
    Handles logging for the crawler. 
    Now with extra flair! ✨
    """

    def __init__(self, write_to_file=False):
        self.file_write = write_to_file

    def log(self, message, log_type='INFO', report_file=None):
        """
        Logs a message to stdout and optionally to a file.
        """
        if not log_type:
            log_type = 'INFO'
        
        # 🎨 Add icons based on log type
        icon = "ℹ️ "
        if 'error' in log_type.lower():
            icon = "❌ "
        elif 'warning' in log_type.lower():
            icon = "⚠️ "
        elif 'vuln' in log_type.lower():
            icon = "🔥 "
        elif 'crawler' in log_type.lower():
            icon = "🕷️ "

        # timestamp
        timestamp = time.ctime()
        
        # Format the log string
        # [Day Mon DD HH:MM:SS YYYY] - TYPE: Message
        formatted_msg = "[%s] %s%s: %s" % (timestamp, icon, log_type.upper(), message)
        
        # Print to console (handle unicode safely for Python 2)
        try:
            print formatted_msg
        except UnicodeEncodeError:
            print formatted_msg.encode('utf-8')

        # 📄 Write to Report File (if it's important)
        if report_file and "VULNERABILITY FOUND" in log_type.upper():
            try:
                with open(report_file, 'a') as f:
                    f.write("%s \n %s \n %s \n \n" % (timestamp, log_type, message))
            except IOError as e:
                print "   ❌ Error writing to report file: %s" % e

if __name__ == "__main__":
    # Test the logger
    logger = Logger()
    logger.log('System Check Initiated...', 'info')
    logger.log('Something looks fishy.', 'warning')
    logger.log('SQL Injection Found!', 'VULNERABILITY FOUND')
