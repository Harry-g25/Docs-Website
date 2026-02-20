# Heat Loss App (Stdlib Example)

A small **standard-library-only** reference project:

- GUI: `tkinter` (with `ttk`)
- Persistence: `sqlite3`
- Export: JSON + CSV + plain-text report (with assumptions/units notes)

In the UI:

- **Summary** shows totals across all rooms.
- The room list shows per-room total heat loss.
- **Export Report** writes a readable `.txt` breakdown per room.

## Run

From the repo root:

```powershell
.venv\Scripts\python.exe -m examples.heat_loss_app.app
```

## Run tests

```powershell
.venv\Scripts\python.exe -m unittest examples.heat_loss_app.tests.test_calc
```
