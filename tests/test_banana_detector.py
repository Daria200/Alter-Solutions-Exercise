import logging
import os
import sys
from io import StringIO

from service.banana_detector import log_bananas, minion


def test_log_bananas_no_bananas(banana_preparer):
    # Input with no bananas
    input_data = "apple\norange\nkiwi\napple\n"

    # Redirect stdin to the mock input stream
    sys.stdin = StringIO(input_data)

    # Call the function being tested
    log_bananas()

    # Check that the minion was logged to the file
    with open("banana.log", "r") as f:
        content = f.read()
        assert minion not in content


def test_log_bananas_with_bananas(banana_preparer):
    # Input with bananas
    input_data = "apple\norange\nkiwi\napple\nbanana\nbanana\n"

    # Redirect stdin to the mock input stream
    sys.stdin = StringIO(input_data)

    # Call the function being tested
    log_bananas()

    # Check that the minion was logged to the file
    with open("banana.log", "r") as f:
        content = f.read()
        assert minion in content
