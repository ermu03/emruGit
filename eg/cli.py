import typer

from eg.commands.init import init

app = typer.Typer(add_completion=False)
app.command()(init)


@app.command()
def commit():
    print("Your run commit.")


@app.command()
def hello(name: str):
    print(f"hello {name}")


def main():
    app()


# if __name__ == "__main__":
#     main()  # 直接运行cli.py的入口
