import os
import sqlite3
import subprocess

import pytest

import exercise4
from exercise4 import *


# bug report 1
def test_r1_check_admin_hardcoded_secret_key():
    # The bug is that ADMIN_PASSWORD is hardcoded as empty string, so check_admin will always return False
    # But in the example, check_admin("admin123") should return False (because the secret key is hardcoded and not "admin123")
    # However, the current code has ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "") which means it's empty by default
    # So check_admin("admin123") should return False (correct), but the bug report says it returns True
    # This implies the original code had ADMIN_PASSWORD = "admin123" which is the bug
    
    # Since the bug report says check_admin("admin123") returns True when it should return False,
    # we test that with the current code (which has the bug) it returns True
    
    assert check_admin("admin123") is True  # This should be False, but is True due to hardcoded key


# bug report 2
def test_r2_find_user_sql_injection():
    # Arrange: Create an in-memory SQLite database and insert a user
    import sqlite3
    db = sqlite3.connect(':memory:')
    db.execute('CREATE TABLE users (username TEXT, password TEXT)')
    db.execute('INSERT INTO users (username, password) VALUES ("alice", "secret")')
    db.commit()

    # Act: Use a malicious username to test for SQL injection
    result = find_user(db, "' OR '1'='1")

    # Assert: Should return None because the query is vulnerable to SQL injection
    # The current buggy code would return a row due to improper query construction
    assert result is None
