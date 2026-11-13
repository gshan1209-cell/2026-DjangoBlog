# Isolated Django smoke checks

Python 3.12.14 with Django 6.0.10 was used. The 6.0 series follows the repository's AGENT.md and migration header, not a production upgrade recommendation. Package availability was checked against https://pypi.org/simple/django/ on 2026-11-13; the isolated environment installed Django 6.0.10, asgiref 3.13.0 and sqlparse 0.6.1. These exact versions are in requirements-smoke.txt for this test environment only; no vulnerability audit or cross-platform lock is claimed.

```bash
python -m venv /tmp/djangoblog-smoke
/tmp/djangoblog-smoke/bin/python -m pip install -r requirements-smoke.txt
/tmp/djangoblog-smoke/bin/python -m django test smoke_tests --settings=smoke_tests.settings -v 2
```

The standalone settings do not import DjangoBlog.settings. They use a synthetic non-production secret and SQLite memory database. The real repository URLconf, article model/migration/view and template are exercised by Django's test client, without starting a server. Six checks cover the memory database, empty homepage/template/context, descending publication date, HTML title escaping, unauthenticated admin redirect and missing-CSRF rejection. The two admin checks validate the explicitly enabled test middleware, NOT the untested production security configuration.

Observed: six tests pass, system check reports no issues, repository SQLite file hashes unchanged before/after. Migrations apply only to the temporary memory test database, destroyed after the run. No existing database rows were queried; no real user credentials or production service was used. The initial system Python 3.13 venv attempt lacked ensurepip; a separate available Python 3.12 venv succeeded without system package installation.

This is an added regression baseline, not a bugfix with a red-green claim, independent code review or CI execution. It does not validate the default settings, persisted DB, dependency vulnerabilities, full bootstrap, browser layout or deployment. Existing requirements.txt remains unchanged/empty. PR #1/#2 files are not part of this slice.
