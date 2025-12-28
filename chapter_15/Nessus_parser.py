#!/usr/bin/env python
"""
🔍 Nessus Report Parser
Parses `.nessus` XML files to extract and display vulnerability findings.
Requires `libnessus` module. 📊
"""

import sys
# Try/Except block for the external library to avoid immediate crashes if missing
try:
    from libnessus.parser import NessusParser
except ImportError:
    print "❌ Error: 'libnessus' module not found. Please install it."
    sys.exit(1)

class NessusReportViewer:
    def __init__(self, file_name):
        self.nessus_file = file_name
        # 🎨 Colors for Output
        self.colors = {
            'HEADER': '\033[95m',
            'BLUE': '\033[94m',
            'GREEN': '\033[92m',
            'WARNING': '\033[93m',
            'FAIL': '\033[91m',
            'END': '\033[0m',
            'BOLD': '\033[1m'
        }

    def print_report(self, nessus_obj):
        """Iterates through hosts and findings"""
        print "\n📊 === Nessus Report Summary === 📊\n"
        
        for host in nessus_obj.hosts:
            print self.colors['FAIL'] + "🖥️  Host: " + host.ip 
            print "    Hostname: " + host.name
            print "    OS: " + str(host.get_host_property('operating-system')) + self.colors['END']
            print "-" * 50

            for item in host.get_report_items:
                # Severity Color Coding could be added here
                print self.colors['GREEN'] + "   🧩 Plugin ID: " + self.colors['BLUE'] + str(item.plugin_id)
                print self.colors['GREEN'] + "   📛 Name:      " + self.colors['BLUE'] + str(item.plugin_name)
                print self.colors['GREEN'] + "   🔥 Severity:  " + self.colors['BLUE'] + str(item.severity)
                print self.colors['GREEN'] + "   🔌 Port:      " + self.colors['BLUE'] + str(item.port) + "/" + str(item.protocol)
                print self.colors['GREEN'] + "   📝 Synopsis:  " + self.colors['BLUE'] + str(item.synopsis)
                print self.colors['END']
                print "   -----------------------------"

    def parse(self):
        print "📂 Parsing file: " + self.nessus_file
        try:
            nessus_obj = NessusParser.parse_fromfile(self.nessus_file)
            self.print_report(nessus_obj)
        except Exception as e:
            print "❌ Failed to parse file: " + str(e)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Usage: python Nessus_parser.py <report.nessus>"
    else:
        viewer = NessusReportViewer(sys.argv[1])
        viewer.parse()
