import sys
from typing import Annotated
from pathlib import Path

from typer import Argument, echo


def init(directory: Annotated[str, Argument(help="Directory to initalize")] = "."):
    d = Path(directory) if directory is not None else Path(".")
    git_dir = d / ".git"

    if git_dir.exists():
        echo(f"fatal: git repo {git_dir.absolute()} already exists!", err=True)
        sys.exit(1)

    git_dir.mkdir(parents=True, exist_ok=False)
    (git_dir / "objects").mkdir()
    (git_dir / "refs" / "heads").mkdir(parents=True)
    (git_dir / "refs" / "tags").mkdir(parents=True)

    with (git_dir / "HEAD").open("w") as f:
        f.write("ref: refs/heads/main\n")

    echo(f"Initialized emptry EG repository in {git_dir.absolute()}")
