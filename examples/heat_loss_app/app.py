from __future__ import annotations

from pathlib import Path

from .ui import run


def main() -> None:
    db_path = Path(__file__).with_name("heat_loss.db")
    run(db_path)


if __name__ == "__main__":
    main()
