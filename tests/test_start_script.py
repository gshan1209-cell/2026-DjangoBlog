"""Isolated launcher tests: fake Python, no Django/DB/server/network."""
from pathlib import Path
import os
import shutil
import subprocess
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'start.sh'

class StartScriptTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='django launcher ')
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        shutil.copyfile(SCRIPT, self.root / 'start.sh')
        (self.root / 'manage.py').write_text('# synthetic only\n')
        self.log = self.root / 'calls.log'
        self.env = {**os.environ, 'LAUNCH_TEST_LOG': str(self.log)}

    def fake_python(self):
        p = self.root / '.venv/bin/python'
        p.parent.mkdir(parents=True)
        p.write_text('#!/bin/sh\nprintf "%s|%s\\n" "$PWD" "$*" >> "$LAUNCH_TEST_LOG"\nif [ "$2" = migrate ]; then exit "${LAUNCH_MIGRATE_EXIT:-0}"; fi\nexit "${LAUNCH_SERVER_EXIT:-0}"\n')
        p.chmod(0o700)

    def run_script(self, *args):
        return subprocess.run(['bash', str(self.root / 'start.sh'), *args], cwd='/tmp', env=self.env, text=True, capture_output=True)

    def test_missing_venv_fails_without_execution(self):
        result = self.run_script()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('.venv', result.stderr)
        self.assertFalse(self.log.exists())

    def test_missing_manage_fails_before_python(self):
        self.fake_python(); (self.root / 'manage.py').unlink()
        self.assertNotEqual(self.run_script().returncode, 0)
        self.assertFalse(self.log.exists())

    def test_runs_from_project_with_spaces_and_loopback_default(self):
        self.fake_python()
        result = self.run_script()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self.log.read_text().splitlines(), [f'{self.root}|manage.py migrate --noinput', f'{self.root}|manage.py runserver 127.0.0.1:8000'])

    def test_migration_failure_prevents_server_and_keeps_exit(self):
        self.fake_python(); self.env['LAUNCH_MIGRATE_EXIT'] = '7'
        self.assertEqual(self.run_script().returncode, 7)
        self.assertEqual(len(self.log.read_text().splitlines()), 1)

    def test_explicit_runserver_arguments_preserved(self):
        self.fake_python()
        self.assertEqual(self.run_script('127.0.0.1:8123', '--noreload').returncode, 0)
        self.assertTrue(self.log.read_text().endswith('manage.py runserver 127.0.0.1:8123 --noreload\n'))

    def test_server_exit_is_propagated(self):
        self.fake_python(); self.env['LAUNCH_SERVER_EXIT'] = '9'
        self.assertEqual(self.run_script().returncode, 9)

if __name__ == '__main__': unittest.main()
