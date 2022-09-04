## TDD - Red, Green, Refactor
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![CI](https://github.com/qleisan/tdd_training/actions/workflows/CI.yaml/badge.svg)](https://github.com/qleisan/tdd_training/actions/workflows/CI.yaml)

### Installation:

```
pip3 install -r requirements.txt
```

### Pytest notes:

Official [pytest-documentation](https://docs.pytest.org/)

```
pytest              # run tests with minimal output
pytest -v           # run tests, listing name of all tests
pytest -v -s        # run tests, listing name of all tests, and show stdout
```

If a previously green test starts failing during "red", i.e. working to make a new test pass, comment out the new test and do the refactoring needed. This to avoid refactoring and adding new functinality at the same time.
```
@pytest.mark.skip(reason="new test disabled during refactoring")
```

### Code Formatting

This project uses [black](https://github.com/psf/black) to format code and [flake8](https://flake8.pycqa.org/en/latest/) for linting.

Format all files using command-line:
```
black <directory>
```
Lint all files:
```
flake8 --ignore=E203,E501
```
VSCode:
- install VSCode extension [Python: Black](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- shift+alt+f => format code
- `.vscode/settings.json` file contains VSCode settings for black and flake8
    - black autoformat on save
    - flake8 linting ("problems" tab and squiggly lines)


### Python notes:

Socratica [youtube-video](https://youtu.be/nlCKrKGHSSk) on python exceptions.



