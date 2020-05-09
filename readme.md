# PyBumpVersion

A date-based semantic versioning bumper for python files.

## What is it?

A python script/Docker image to automatically bump the version of a project in a single file. Instead of standard semantic versioning (`{major}.{minor}.{patch}`), PyBumpVersion uses a date-based approach marking the year, month, and build number of each version:

```
{year}.{month}.{build_number}
```

So version `20.05.0005` was the fifth build of May 2020.

## Why not standard semantic versioning?

Standard semantic versioning doesn't make a whole lot of sense in a continuous deployment setting. What, exactly, constitutes a major or minor version bump? Shouldn't it all be stable and intercompatible? After all, the package we deploy should version its API's as needed; pushing a new version of the source code shouldn't actually break anything.

All this means that many projects end up stuck on one major or minor version while the lesser versions get bumped. I feel date-based semantic versioning gives a bit more insight into where and when code changes occur.

Eg. `0.0.1989` doesn't convey as much information as `20.05.1989`.

## Usage
```
$ pybumpversion <file_path>
```

PyBumpVersion will bump the version in any file you give it. It looks for a standard format when bumping versions:

```python
__version__ = '20.05.0000'  # YY.MM.BUILD_NUMBER
```

For example: `$ pybumpversion app/__init__.py` will bump the `__version__` in `app/__init__.py`.


If using the Docker image, you'll need to mount your code directory as a volume:

```
$ docker run -v code:/code pybumpversion /code/app/__init__.py
```
