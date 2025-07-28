# Logging to Files

## Basic File Logging with `FileHandler`

- Use `logging.FileHandler` to write log records to a file.
- `mode='a'` (append) preserves existing logs; `mode='w'` (write) overwrites on each run.
- You can specify `encoding` (e.g., `'utf-8'`) and `delay=True` to open the file only on first write.

## Size-Based Rotation with `RotatingFileHandler`

- `RotatingFileHandler` rotates when the file reaches `maxBytes`.
- `backupCount` determines how many old files to keep (`.1`, `.2`, …). E.g., if we have `backupCount=2` and if new backup file is created, then `.1` will be `.2` and `.2` will be the new backup file.
- New rotations rename existing backups, deleting the oldest beyond `backupCount`.

## Time-Based Rotation with `TimedRotatingFileHandler`

- `TimedRotatingFileHandler` rotates based on elapsed time (`when`, `interval`).
- Common `when` values (case insensitive): `'S'`, `'M'`, `'H'`, `'D'`, `'midnight'`, `'W0'`-`'W6'`
  - **`'S'`** – Rotate every _N_ **seconds** (as given by `interval`), useful for very short-lived scripts or testing.
  - **`'M'`** – Rotate every _N_ **minutes**, good for high-volume services where hourly isn’t fine-grained enough.
  - **`'H'`** – Rotate every _N_ **hours**, often used for long-running daemons that batch logs hourly.
  - **`'D'`** – Rotate every _N_ **days**, for simple daily log files without tying to midnight.
  - **`'midnight'`** – Rotate once per day exactly at midnight (local time), regardless of `interval`, ideal for calendar-aligned logs.
  - **`'W0'`–`'W6'`** – Rotate weekly on a specific weekday, where `W0` = Monday through `W6` = Sunday. Use `interval` weeks between rotations.
- `backupCount` limits number of rotated files; use `.suffix` to customize timestamp format.
