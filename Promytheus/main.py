#!/usr/bin/python3
import subprocess

subprocess.call("./Promytheus/tests/test_login_page.py")
subprocess.call("./Promytheus/tests/test_happy_path.py")
subprocess.call("./Promytheus/tests/test_password_change.py")
