#!/usr/bin/env python
"""
🎭 CSRF Automator
Crawls a site and looks for forms missing anti-CSRF tokens.
It's like checking if your front door has a lock! 🔓
"""

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class CSRFAutomator:
    def __init__(self, target, base_url):
        self.target = target
        self.base_url = base_url
        self.email = "admin"
        self.password = "password"
        
        # 🎯 Targets to scan within the site
        self.target_paths = ["vulnerabilities/csrf/"]
        
        # 🍪 Tokens we recognize as protection
        self.csrf_token_names = ["RequestVerificationToken", "token", "csrfToken", "csrftoken"]
        self.hidden_input_names = ["__RequestVerificationToken", "token", "_csrfToken", "_csrftoken"]
        
        print "\n🎭 CSRF Automator Initialized!"
        print "   🎯 Target: " + self.target

    def login(self, browser):
        """Performs the login action."""
        print "\n   🔑 Logging in..."
        browser.get(self.target)
        
        try:
            # 1️⃣ Fill Username
            user_field = browser.find_element_by_name("username")
            user_field.clear()
            user_field.send_keys(self.email)
            
            # 2️⃣ Fill Password
            pass_field = browser.find_element_by_name("password")
            pass_field.clear()
            pass_field.send_keys(self.password)
            
            # 3️⃣ CLICK!
            submit_btn = WebDriverWait(browser, 2).until(
                EC.element_to_be_clickable((By.NAME, "Login"))
            )
            submit_btn.click()
            print "   ✅ Login Clicked!"
            time.sleep(2) # Wait for page load
            
        except Exception as e:
            print "   ❌ Login Failed: " + str(e)
            browser.quit()

    def start_scan(self):
        try:
            # 👻 Start PhantomJS (Headless Browser)
            browser = webdriver.PhantomJS()
            
            # 1️⃣ Login First
            self.login(browser)

            # 🍪 Set Search Cookie (Example for DVWA logic)
            # cookie = {'domain': '192.168.250.1', 'name': 'security', 
            #           'value': 'low', 'path': '/dvwa/', 'httponly': False, 'secure': False}
            # browser.add_cookie(cookie)
            
            # 📸 Snapshot
            browser.save_screenshot('login_success.png')
            print "   📸 Saved 'login_success.png'"

            # 2️⃣ Crawl Links
            print "\n   🕷️ Crawling links..."
            soup = BeautifulSoup(browser.page_source, "html.parser")
            anchors = soup.find_all("a")
            
            vulnerable_forms = []

            for i, link in enumerate(anchors):
                href = link.attrs.get("href", "")
                
                # Clean up path logic
                clean_href = href.replace("/.", "/")
                
                if clean_href in self.target_paths:
                    full_url = self.target + clean_href
                    print "\n   🔎 Inspecting: " + full_url
                    
                    browser.get(full_url)
                    browser.save_screenshot("scan_step_" + str(i) + ".png")
                    
                    # 📝 Analyze Forms
                    page_soup = BeautifulSoup(browser.page_source, "html.parser")
                    forms = page_soup.find_all("form")
                    
                    if not forms:
                        print "      (No forms found on page)"
                    
                    for form_idx, form in enumerate(forms):
                        print "      📝 Analyzing Form #" + str(form_idx + 1)
                        is_protected = False
                        
                        # Check hidden inputs for token names
                        inputs = form.find_all("input")
                        for inp in inputs:
                            if inp.attrs.get("type") == "hidden":
                                name = inp.attrs.get("name")
                                if name in self.hidden_input_names:
                                    print "         🛡️ Found Anti-CSRF Token: " + name
                                    is_protected = True
                        
                        if not is_protected:
                            print "         ⚠️ NO TOKEN FOUND! (Potential CSRF)"
                            vulnerable_forms.append({"url": full_url, "html": str(form)[:100] + "..."})
                            browser.save_screenshot('csrf_vuln_' + str(form_idx) + '.png')

            # 3️⃣ Report
            print "\n   📊 === SCAN REPORT ==="
            if vulnerable_forms:
                print "   🔥 Vulnerable Forms Found: " + str(len(vulnerable_forms))
                for item in vulnerable_forms:
                    print "      📍 URL: " + item["url"]
                    print "      📝 Form: " + item["html"]
            else:
                print "   ✅ No obvious CSRF vulnerabilities found."

            browser.quit()

        except Exception as ex:
            print "   ❌ Critical Error: " + str(ex)

if __name__ == "__main__":
    target = "http://192.168.250.1/dvwa/"
    base = "http://192.168.250.1/"
    bot = CSRFAutomator(target, base)
    bot.start_scan()
