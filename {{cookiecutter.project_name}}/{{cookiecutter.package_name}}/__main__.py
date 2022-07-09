import typer

app = typer.Typer()


@app.command()
def run():
    print("Hello, World!")


if __name__ == "__main__":
    app()
