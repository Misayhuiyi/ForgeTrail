"""Smoke tests for the public module entry point, without model credentials."""

import os
from pathlib import Path
import subprocess
import sys


def test_module_help_runs_outside_the_repository_without_config(tmp_path):
    """Catch stale imports in the renamed entry point before any provider loads."""
    env = os.environ.copy()
    env["PYTHONPATH"] = str(Path(__file__).resolve().parents[1])
    result = subprocess.run(
        [sys.executable, "-m", "forgetrail", "--help"],
        cwd=tmp_path,
        env=env,
        capture_output=True,
        text=True,
        timeout=20,
    )
    assert result.returncode == 0, result.stderr
    assert "usage: forgetrail" in result.stdout
    assert "--output-format" in result.stdout
