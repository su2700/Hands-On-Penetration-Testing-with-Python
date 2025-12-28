#!/usr/bin/env python
"""
🗺️ Nmap XML Parser
Parses Nmap XML reports to show Hosts, Ports, and Services nicely.
Requires `libnmap` module. 🔍
"""

import sys
try:
    from libnmap.parser import NmapParser
except ImportError:
    print "❌ Error: 'libnmap' module not found."
    sys.exit(1)

class NmapReportViewer:
    def __init__(self, report_file):
        self.report_file = report_file

    def parse(self):
        print "\n📂 Parsing Nmap XML: " + self.report_file
        try:
            report = NmapParser.parse_fromfile(self.report_file)
        except Exception as e:
            print "❌ Parsing Error: " + str(e)
            return

        print "🚀 Scan Summary: " + report.summary
        print "\n--- HOSTS ---\n"

        for host in report.hosts:
            if host.is_up():
                print "✅ Host Up: " + str(host.address) + " (" + str(len(host.hostnames)) + " hostnames)"
                
                open_ports = host.get_open_ports()
                if open_ports:
                    print "   🔓 Open Services:"
                    for port, proto in open_ports:
                        service = host.get_service(port, proto)
                        print "      🔹 Port:    " + str(port) + "/" + proto
                        print "         Service: " + str(service.service)
                        print "         State:   " + str(service.state)
                        if service.banner:
                            print "         Banner:  " + str(service.banner)
                        print ""
            else:
                print "❌ Host Down: " + str(host.address)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Usage: python nmap_parser.py <nmap_output.xml>"
    else:
        viewer = NmapReportViewer(sys.argv[1])
        viewer.parse()
