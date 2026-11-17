# Bug analysis and fixes

| Function | Fuzzed failure | Fix |
|---|---|---|
| `format_player_name` | `None` caused `AttributeError` at `.strip()`. | Return an empty string for non-string input; preserve trim, title case, and 10-character limit for strings. |
| `parse_frame` | `None`, empty/short strings, invalid symbols, and impossible pin totals caused exceptions or invalid results. | Validate type, length, notation, digits, and total pins; return `(0, 0)` for invalid notation. |
| `parse_scoreboard` | `None`, missing/extra separators, blank or non-numeric scores caused exceptions. | Return `{}` for non-string input; skip malformed entries; accept only non-empty names and digit scores from 0 through 300. |

The fuzz test run against the original code failed. After the fixes, all 7 tests passed.
