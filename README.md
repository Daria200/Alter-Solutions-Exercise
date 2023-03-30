# Alter-Solutions-Exercise-1

> This is a simple service that reads from stdin and logs an Ascii minion to the system log whenever the word "banana" is encountered.

## Configure Environment

> This project uses [poetry](https://python-poetry.org/) to manage python dependencies.

Install the project and its Python dependencies:

```sh
poetry install
```

## Scripts

How to run:

```
echo "I like bananas." | python service/banana_detector.py
```

Run tests:

```sh
poetry run python -m pytest
```
