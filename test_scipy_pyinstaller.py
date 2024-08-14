import subprocess
from pathlib import Path

import pytest

def test_pyinstaller(tmp_path):
    pyinstaller_cli = pytest.importorskip("PyInstaller.__main__").run

    source = Path(__file__).with_name("scipy_pyinstaller_bug_reproduction.py")
    args = [
        '--workpath', str(tmp_path / "build"),
        '--distpath', str(tmp_path / "dist"),
        '--specpath', str(tmp_path),
        str(source)
    ]

    pyinstaller_cli(args)

    exe = tmp_path / "dist" / source.stem / source.stem

    result = subprocess.run([str(exe)], capture_output=True, text=True)
    assert "Executed successfully" in result.stdout.strip()

