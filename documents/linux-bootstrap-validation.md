# Linux bootstrap failure handling

Run `bash build_venv.sh` from any directory. It resolves the project path, including spaces, and reads the tracked plural `requirements.txt`. Missing, empty or comment-only lists stop before Python is invoked. A populated list is not proof of valid versions or a working Django installation.

An existing unusable `.venv` is preserved and reported, not recursively removed. Repair/replacement is a separate deliberate action. A valid environment is reused. New-environment creation, pip upgrade and dependency-install failures stop immediately; completion is only printed after both install steps succeed. Existing environments may be modified by successful pip operations when the real script is deliberately run. This is development tooling, not a deployment script.

## Verification

`python -m unittest discover -s tests -p 'test_bootstrap_script.py' -v`: ten tests use temporary fake Python executables, including failure codes and path-with-spaces coverage. Baseline: ten failures; candidate: ten passes. `bash -n build_venv.sh` and `git diff --check` pass. Tests do not install packages, contact a registry, create a real venv, start Django, or migrate a database. No CI run or independent review is claimed.

## Remaining limitations

The repository's requirements file is still empty. Consequently the real project bootstrap now stops with an explicit error rather than falsely succeeding. Dependency selection, Python/Django version compatibility, Windows scripts, package vulnerability audit and full application initialization remain separate work. This change intentionally does not fill a guessed dependency list, download databases, edit credentials/settings, or change production. It is independent of the start.sh launcher candidate.
