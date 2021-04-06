import copy
import json
import os
import platform
from pathlib import Path

from invoke import task

# Basic parameters
REPO_ROOT = Path(__file__).parent
OS = platform.system().lower()
VENV_DIRNAME = Path('.venv')
PATHONPATHS = {
    'windows': VENV_DIRNAME / 'Scripts' / 'python.exe',
    'linux': VENV_DIRNAME / 'bin' / 'python',
    'darwin': VENV_DIRNAME / 'bin' / 'python',
}
PATHONPATHS_ABS = {
    'windows': REPO_ROOT / VENV_DIRNAME / 'Scripts' / 'python.exe',
    'linux': REPO_ROOT.resolve() / VENV_DIRNAME / 'bin' / 'python',
    'darwin': REPO_ROOT.resolve() / VENV_DIRNAME / 'bin' / 'python',
}
# Default VS Code settings
# Related file: ./.vscode/settings.json
VSCODE_SETTINGS = {
    'python.pythonPath': str(PATHONPATHS[OS]),
    'python.linting.enabled': True,
    'python.linting.pylintEnabled': False,
    'python.linting.flake8Enabled': True,
    'python.linting.flake8Args': ['--max-line-length=160'],
    'python.formatting.provider': 'autopep8',
    'python.formatting.autopep8Args': ['--max-line-length=160']
}


# Read a .json file and update its key/value with default dict.
# For each keys in the default dict, if there is not in .json, add it, else keep it the same.
def update(path, default_dict, indent=4, *arg, **kwargs):
    d = copy.deepcopy(default_dict)
    with open(path, 'r', encoding='utf-8') as f:
        secrets = json.loads(f.read())
    d.update(secrets)
    s = json.dumps(d, indent=indent)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(s)


# Update VS Code settings
@task
def vscode(c):
    try:
        os.mkdir(REPO_ROOT / '.vscode')
    except FileExistsError:
        pass
    update(path=REPO_ROOT / '.vscode' / 'settings.json', default_dict=VSCODE_SETTINGS)
    print('Done!')
