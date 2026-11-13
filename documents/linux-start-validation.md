# Linux development launcher

`bash start.sh` uses this checkout's `.venv/bin/python`, runs `manage.py migrate --noinput`, then starts Django's development server on **127.0.0.1:8000**. It works from a different working directory and paths containing spaces. It does not download a database, install packages, open a browser or modify production configuration.

**Running the launcher applies migrations to the database configured by Django.** Use a disposable development database and verify settings first; do not point it at a production or irreplaceable database. This PR's tests never run Django or migrate either repository database.

To choose a local port or pass Django arguments:

```bash
bash start.sh 127.0.0.1:8123 --noreload
```

Missing executable virtual-environment Python or `manage.py` fails before execution. Migration failure stops startup; server exit status is propagated. The caller's PATH/environment is not changed by activation. A non-loopback address supplied explicitly can expose the development server; use loopback only for ordinary local work. `runserver` is not a production server.

## Regression check

```bash
bash -n start.sh
python -m unittest discover -s tests -v
```

Six synthetic tests create temporary fake interpreters to check prerequisites, project directory with spaces, default loopback, argument forwarding and migration/server failure. No network or database is used. Passing these tests is launcher validation only, not full Django integration, database compatibility, security review or deployment acceptance.

## Existing prerequisites not addressed

The tracked `requirements.txt` is empty, and `build_venv.sh` currently looks for singular `requirement.txt`. README's Python minimum and Django 6 runtime compatibility also require separate review. Prepare a compatible environment before using this launcher; this candidate does not claim the initialization pipeline is working end to end.
