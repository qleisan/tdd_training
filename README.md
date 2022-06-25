## TDD - Red, Green, Refactor

### pytest notes:

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

### python notes:

Socratica [youtube-video](https://youtu.be/nlCKrKGHSSk) on python exceptions.



