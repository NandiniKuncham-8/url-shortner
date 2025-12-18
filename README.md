\#URL Shortener

A simple and efficient URL shortening service built with Python and FastAPI, using SQLite for storage. It validates URLs, generates compact Base62-encoded short codes, and supports redirection from short URLs to original long URLs.

\#Features

1.Validates URLs to ensure proper format before shortening (using Pydantic’s HttpUrl)

2.Generates unique short codes using Base62 encoding of auto-increment IDs

3.Stores URLs and short codes in an SQLite database

4.Redirects short URLs to their original long URLs

5.Handles duplicate URLs gracefully by returning existing short codes

**#**Tech Stack

Python 3.10+

FastAPI

SQLite

Pydantic

Uvicorn (ASGI server)

