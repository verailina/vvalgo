"""Test utils."""
from pathlib import Path

import pytest


@pytest.fixture()
def resources_path(request) -> Path:
    """Get test resources path."""
    return Path(request.fspath).parent / "resources"
