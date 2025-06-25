import typer

app = typer.Typer(add_completion=False)

@app.command()
def init():
    print("Hello World")

@app.command()
def commit():
    print("Hello World")

@app.command()
def hello2(name: str):
    print(f"hello {name}")


def main():
    app()

# if __name__ == "__main__":
#     main()  # 直接运行cli.py的入口


