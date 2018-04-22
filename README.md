# Quotes Challenge

## Getting Started

### Change directory into your newly created project.

```console
cd quotes_challenge
```
### Upgrade packaging tools.

```console
    pip install --upgrade pip setuptools
```

### Install the project in editable mode with its testing requirements.

```console
    pip install -e ".[testing]"
```

### Configure the database.

```console
    initialize_quotes_challenge_db development.ini
```

### Run your project's tests.

```console
    py.test
```

### Run your project.

```console
    pserve development.ini
```

## Website pages:

- localhost:6543/
- localhost:6543/quotes
- localhost:6543/quotes/{INTEGER}
- localhost:6543/quotes/random

## API Endpoints:

- localhost:6543/sessions/
- localhost:6543/sessions/{UUID}

## Fun way to test it

- Access some of the website pages
- Access the api endpoint sessions/
    - There, you will see a code of letters and numbers mixed, copy that
    - go to the /sessions/{Here goes the code that you copied}
    - Now you see the pages that you accessed :O (inside our, app of course, nothing like Mark and the Facebook does everyday with ALL pages)

## To test other methods rest with our api, you can use __curl__
(after use ```pserve development.ini```)

```console
    curl -d '{"uuid":"abc"}' -H "Content-Type: application/json" -X POST http://localhost:6543/sessions
    curl -d '{"uuid":"def"}' -H "Content-Type: application/json" -X PUT http://localhost:6543/sessions/abc
    curl -H "Content-Type: application/json" -X DELETE http://localhost:6543/sessions/def

```
