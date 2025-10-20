import os
import sys


def pytest_sessionstart(session):
    """Ensure the project root (BackEnd) is on sys.path for imports."""
    root = os.path.dirname(os.path.dirname(__file__))
    if root not in sys.path:
        sys.path.insert(0, root)
