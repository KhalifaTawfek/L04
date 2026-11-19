import os
import sqlite3
import subprocess

import pytest

import exercise4
from exercise4 import *


# bug report 1
def test_r1_check_admin_hardcoded_secret_key():
    """Test that check_admin returns False for a wrong password (bug: hardcoded secret key)"""
    assert check_admin("admin123") == False


# bug report 2
def test_r2_find_user_sql_injection():
    """Test that find_user does not allow SQL injection by using a malicious username."""
    # Example of a malicious input that should cause SQL injection
    malicious_username = "' OR '1'='1"
    result = find_user(None, malicious_username)
    assert result is None
