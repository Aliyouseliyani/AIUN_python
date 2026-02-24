# AIUN Python Practice Repository

This repository contains small Python practice projects:

1. A **console banking application** (`bank/`) that stores account data in JSON.
2. A **general practice script** (`main.py`) with commented exercises and a custom string `strip` function.

## Project Structure

- `bank/main.py` – interactive CLI for creating accounts, checking balances, deposits, withdrawals, and filtering accounts above average balance.
- `bank/utils.py` – `DataBase` and `Bank` classes for JSON persistence and business logic.
- `bank/db/data.json` – local JSON datastore used by the bank app.
- `main.py` – standalone practice script containing multiple commented exercises and a custom `strip` implementation.

## Requirements

- Python 3.10+ (recommended)
- No external dependencies (standard library only)

## Running the Bank App

From the repository root:

```bash
cd bank
python main.py
```

You will be prompted to:

- enter an account holder name,
- optionally create one or more numbered accounts with initial balances,
- choose operations from a menu:
  - show balances,
  - deposit,
  - withdraw,
  - show accounts with above-average balance,
  - exit.

### Data Persistence

All banking data is saved to:

- `bank/db/data.json`

The JSON format is:

```json
{
  "account_holder_name": {
    "1": 1000,
    "2": 2500
  }
}
```

## Running the Practice Script

From the repository root:

```bash
python main.py
```

This script currently:

- measures execution time,
- defines a custom `strip(string)` function that removes leading/trailing spaces,
- includes several commented learning exercises (calculator, age converter, number tasks, matrix multiplication).

## Notes

- This repository appears to be learning/practice-oriented.
- The bank app uses relative paths, so run it from inside the `bank/` directory for correct data file resolution.
