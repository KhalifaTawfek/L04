You get one bug report and the Python file.
Write exactly ONE pytest test that proves the bug.
Rules:
- Answer with Python code only. No markdown, no ``` fences, no explanation.
- One function whose name starts with test_.
- Do not import the exercise functions: they are already imported.
- Use the input from the Example line and assert the EXPECTED value, not the current output.
- The test must FAIL on the buggy code and PASS after the Fix.
- If the expected behavior is an error, use: with pytest.raises(ErrorType):
- If the docstring says what to return for an empty or zero input, assert that return value. Never use pytest.raises in that case.
- If a function takes a db argument, ALWAYS build a real sqlite3 in-memory database, create the table the query uses (e.g. users with a username column), insert one row, and pass that db. Never pass None.
