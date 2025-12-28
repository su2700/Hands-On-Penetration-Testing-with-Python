import os
import sys

# 🌍 Add current directory to path so we can find modules
sys.path.append(os.getcwd())

# 🛠️ Django Imports
# (We assume Django environment is set up correctly in manage.py context)
# from xtreme_server.models import * 
# Note: In a real run, this needs the DJANGO_SETTINGS_MODULE set.

try:
    from xtreme_server.models import Project
    from crawler import Crawler
    from logger import Logger
except ImportError:
    # 🩹 Fallback for when running outside of full Django context
    print "⚠️ Warning: Django modules not found. Ensure you run this via 'python manage.py shell' or similar context."
    sys.exit(1)

def run_mission():
    print "\n" + "="*50
    print "      🕷️  XTREME SPIDER LAUNCHER  🕷️"
    print "="*50

    if len(sys.argv) < 2:
        print "   ❌ Error: Please provide a Project Name!"
        print "   👉 Usage: python run_crawler.py <project_name>"
        return

    project_name = sys.argv[1]
    print "   📂 Loading Project: '%s'..." % project_name

    try:
        project = Project.objects.get(project_name=project_name)
    except Exception as e:
        print "   ❌ Project not found in Database! (%s)" % e
        return

    # 📥 Unpack Project Settings
    print "   ⚙️  Configuring Spider..."
    
    # Conversions (Handling Python 2 strings/unicode)
    start_url = str(project.start_url)
    query_url = str(project.query_url)
    login_url = str(project.login_url)
    logout_url = str(project.logout_url)
    username_field = str(project.username_field)
    password_field = str(project.password_field)
    
    # 📦 Settings Dictionary
    settings = {}
    
    # Using eval() is risky but part of original logic. Keeping it but noting it.
    try:
        settings['allowed_extensions'] = eval(str(project.allowed_extensions))
        settings['allowed_protocols']  = eval(str(project.allowed_protocols))
        settings['consider_only']      = eval(str(project.consider_only))
        settings['exclude']            = eval(str(project.exclude_fields))
    except SyntaxError:
        print "   ⚠️ Error parsing settings lists. Using empty lists."
        settings['allowed_extensions'] = []
        settings['allowed_protocols'] = []
        settings['consider_only'] = []
        settings['exclude'] = []

    settings['username'] = project.username
    settings['password'] = project.password
    settings['auth_mode'] = project.auth_mode

    print "   🕸️  Initializing Crawler Instance..."
    
    # 🚀 Create the Crawler
    c = Crawler(
        crawler_name = project_name, 
        start_url = start_url, 
        query_url = query_url,
        login_url = login_url,
        logout_url = logout_url,
        
        # Lists
        allowed_protocols_list = settings['allowed_protocols'],
        allowed_extensions_list = settings['allowed_extensions'],
        list_of_types_to_consider = settings['consider_only'],
        list_of_fields_to_exclude = settings['exclude'],
        
        # Auth
        username = settings['username'],
        password = settings['password'],
        auth_mode = settings['auth_mode'],
        username_field = username_field,
        password_field = password_field,
        
        # Extra
        queueName = str(project.queueName),
        redisIP = str(project.redisIP),
        auth_parameters = str(project.auth_parameters)
    )

    print "   🚀 LAUNCHING CRAWLER! Good hunting!"
    print "-"*50
    c.start()

if __name__ == "__main__":
    run_mission()
