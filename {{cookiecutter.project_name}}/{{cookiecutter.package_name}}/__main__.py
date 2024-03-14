import asyncio
from functools import wraps
import logging
import sys

import typer

app = typer.Typer()
logging.basicConfig(stream=sys.stderr, level=logging.INFO, format="[%(asctime)s] %(levelname)s: %(name)s: %(message)s")


logger = logging.getLogger(__name__)


# REF: https://github.com/pallets/click/issues/85
def coro(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        return asyncio.run(f(*args, **kwargs))

    return wrapper


@app.command()
@coro
async def async_run():
    logger.info("Hello, World!")


@app.command()
def run():
    logger.info("Hello, World!")


if __name__ == "__main__":
    app()
