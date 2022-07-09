import logging
import sys

import typer

app = typer.Typer()
logging.basicConfig(stream=sys.stderr, level=logging.INFO, format="[%(asctime)s] %(levelname)s: %(name)s: %(message)s")


logger = logging.getLogger(__name__)


@app.command()
def run():
    logger.info("Hello, World!")


if __name__ == "__main__":
    app()
