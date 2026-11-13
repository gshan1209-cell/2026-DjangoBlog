"""No network/packages/real venv: all Python invocations are temporary fakes."""
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'build_venv.sh'
FAKE = '''#!/bin/bash
printf '%s|%s\\n' "$PWD" "$*" >> "$CALLS"
case "$*" in
  '-m venv .venv')
    [ "${CREATE_FAIL:-0}" = 0 ] || exit 5
    mkdir -p .venv/bin
    cp "$0" .venv/bin/python
    chmod +x .venv/bin/python;;
  '-m pip --version') exit "${INVALID:-0}";;
  '-m pip install --upgrade pip') exit "${UPGRADE_FAIL:-0}";;
  '-m pip install -r requirements.txt') exit "${INSTALL_FAIL:-0}";;
esac
'''

class BootstrapTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='bootstrap test ')
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.project = self.root / 'project space'
        self.project.mkdir()
        shutil.copyfile(SCRIPT, self.project / 'build_venv.sh')
        (self.project / 'requirements.txt').write_text('Django==6.0\n')
        self.bin = self.root / 'fakebin'
        self.bin.mkdir()
        fake = self.bin / 'python3'
        fake.write_text(FAKE)
        fake.chmod(0o755)
        self.log = self.root / 'calls'
        self.env = {**os.environ, 'PATH': str(self.bin)+':'+os.environ['PATH'], 'CALLS': str(self.log)}
        for key in ('CREATE_FAIL', 'INVALID', 'UPGRADE_FAIL', 'INSTALL_FAIL'):
            self.env.pop(key, None)
    def run_script(self, **extra):
        return subprocess.run(['bash', str(self.project/'build_venv.sh')], cwd=self.root,
                              env={**self.env, **extra}, capture_output=True, text=True)
    def calls(self):
        return self.log.read_text() if self.log.exists() else ''
    def existing(self):
        dest = self.project/'.venv/bin'
        dest.mkdir(parents=True)
        shutil.copy2(self.bin/'python3', dest/'python')
    def test_missing_requirements_stops_before_python(self):
        (self.project/'requirements.txt').unlink()
        self.assertNotEqual(self.run_script().returncode, 0)
        self.assertEqual(self.calls(), '')
    def test_empty_requirements_stops_before_python(self):
        (self.project/'requirements.txt').write_text('')
        self.assertNotEqual(self.run_script().returncode, 0)
        self.assertEqual(self.calls(), '')
    def test_comment_only_requirements_stops(self):
        (self.project/'requirements.txt').write_text('  # pending\n \n')
        self.assertNotEqual(self.run_script().returncode, 0)
        self.assertEqual(self.calls(), '')
    def test_create_from_other_directory_with_spaces(self):
        self.assertEqual(self.run_script().returncode, 0)
        self.assertIn('-m pip install -r requirements.txt', self.calls())
        self.assertTrue(all(line.startswith(str(self.project)+'|') for line in self.calls().splitlines()))
        self.assertFalse((self.root/'.venv').exists())
    def test_invalid_existing_preserved(self):
        self.existing()
        sentinel = self.project/'.venv/keep-me'
        sentinel.write_text('untouched')
        self.assertNotEqual(self.run_script(INVALID='2').returncode, 0)
        self.assertEqual(sentinel.read_text(), 'untouched')
        self.assertNotIn('install', self.calls())
    def test_partial_existing_preserved(self):
        (self.project/'.venv').mkdir()
        self.assertNotEqual(self.run_script().returncode, 0)
        self.assertEqual(self.calls(), '')
    def test_valid_existing_reused(self):
        self.existing()
        self.assertEqual(self.run_script().returncode, 0)
        self.assertNotIn('-m venv', self.calls())
    def test_creation_failure_stops(self):
        self.assertEqual(self.run_script(CREATE_FAIL='5').returncode, 5)
        self.assertNotIn('install', self.calls())
    def test_upgrade_failure_stops_before_requirements(self):
        self.existing()
        result = self.run_script(UPGRADE_FAIL='7')
        self.assertEqual(result.returncode, 7)
        self.assertNotIn('install -r', self.calls())
        self.assertNotIn('completed successfully', result.stdout)
    def test_install_failure_no_success(self):
        self.existing()
        result = self.run_script(INSTALL_FAIL='9')
        self.assertEqual(result.returncode, 9)
        self.assertNotIn('completed successfully', result.stdout)

if __name__ == '__main__':
    unittest.main()
