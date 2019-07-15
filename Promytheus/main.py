#!/usr/bin/python3
import subprocess

subprocess.call("./tests/test_login_page.py")
subprocess.call("./tests/test_password_change.py")
subprocess.call("./tests/test_talent_form_evidence_tab.py")
subprocess.call("./tests/test_talent_form_training.py")
