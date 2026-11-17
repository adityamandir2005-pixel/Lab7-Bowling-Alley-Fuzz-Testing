# Lab 7 - Bowling Alley Fuzz Testing

This repository contains the fixed Bowling Alley input parser and its Hypothesis fuzz tests for Lab 7.

## Files

- `bowling_alley_parser.py` - hardened application module
- `test_bowling_alley_parser.py` - Hypothesis tests for all three functions
- `SS1_Initial_Application.png` / `.txt` - original program output
- `SS2_Fuzz_Test_Failures.png` / `.txt` - failing tests against original code
- `SS3_Fixed_Application.png` / `.txt` - program output after fixes
- `SS4_Passing_Fuzz_Tests.png` / `.txt` - passing tests after fixes
- `PES1UG25CS825_Aditya_Mandir_LAB7.pdf` - submission report and evidence pages
- `Bug_Analysis.md` - identified issues and fixes

## Run

Install Python 3, pytest, and Hypothesis, then run from the repository root:

```bash
python bowling_alley_parser.py
python -m pytest -q test_bowling_alley_parser.py
```

The test suite includes Hypothesis-generated string/None inputs and explicit valid and invalid cases. Against the original buggy code it reports 6 failed and 1 passed; after the fixes all 7 tests pass.

## Evidence

The PNG panels and PDF evidence pages are rendered from saved command output logs, not direct desktop screenshots. The lab handout asks for terminal screenshots of the initial run, failing tests, fixed run, and passing tests. Capture and replace these panels with direct terminal screenshots if the instructor requires unaltered desktop captures.
