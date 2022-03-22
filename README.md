# Simple Movie Db Api
This is a Python `3.9` service

# 🛑Please Keep the repository private🛑

This is a private repo. Please, only push your changes to this repo.

# Simple TMDB API. 

## Purpose
Simple TMDB API is a proxy api to TMDB API and simplifies the way to use of it so our mobile application
won't have to deal with it directly. It is also to owns api credentials in order to avoid exposing it
by malicious extraction from app.

## CHALLENGE

[Check challenge page for more details](CHALLENGE.md)

# Getting Started

Documentation: https://developers.themoviedb.org/3/getting-started/introduction

Register for an account on the TMBD API above and acquire your API_KEY following the instructions.

## Install Python

Download Python: https://www.python.org/downloads/

OSX/Homebrew: https://docs.brew.sh/Homebrew-and-Python


## Environment Variables:
```Bash
    # Environment variable description
    export API_KEY=<api_key>
```

## Install Locally

### Dev requirements:
Includes all testing and build tooling
```bash
 pip install -r requirements-dev.txt
```

### Running requirements:
```bash
$ pip install -r requirements.txt
```

### Run Locally
```bash
cd src/
python run.py
```

### Requests examples

Searching for Terminator movies:
    http://localhost:8000/v1/movies/search?query=terminator&page=1&region=en_US&genres=878

Looking for The Terminator movie details
    http://localhost:8000/v1/movies/218/details

## Tests

```bash
$ pytest
$ pylint src tests
```

