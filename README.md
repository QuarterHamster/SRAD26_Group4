# SRAD26_Group4
## Project idea
The project aims to create a non-profit event hub for a campus where students, teachers, sponsor, and administrators can post their events.

Users are split into three types:
* Campus user: University students or staff, which can create events and join them.
* Administrators: Admins can approve or reject events, admins can give temporary access to sponsors.
* Sponsors: Sponsors can gain temporary access to the system to post events for an organization

## How to run the project
Clone the project from GitHub
```
gh repo clone QuarterHamster/SRAD26_Group4
```
Open the command console in the project folder and write
```
python Project/main.py
```

## Unit testing (Exercise 5.2)
Test files are located in `tests/`.

Run all unit tests:
```
python -m unittest discover -s tests -p "test_*.py" -v
```

Measure coverage (after installing coverage.py):
```
python -m pip install coverage
python -m coverage run -m unittest discover -s tests -p "test_*.py"
python -m coverage report -m
```

Functionalities tested:
* Event time tag generation (`morning/afternoon/evening/night`, `weekday/weekend`, month)
* Event tag normalization and merge logic
* Private event visibility rules
* Invite-user behavior (duplicate prevention)
* Visible-events filtering by user access
* Sorting visible events by name and date fallback
* Event creation storage in logic layer

Current untested areas:
* Interactive UI input/output flows (console loop and prompts)
* Admin UI workflows and integration paths
* Data layer persistence behavior (currently a stub)

## Code quality tool (Exercise 5.3)
Selected tool:
* Ruff (linter)

Why we chose it:
* It is fast, easy to run in CI, and helps catch real code issues early.

What it improved:
* We added an automatic Pull Request check using GitHub Actions (`.github/workflows/pr_checks.yml`).
* Each PR now runs:
  * unit tests (`unittest`)
  * `ruff check .`
* This gives immediate feedback on high-signal code problems before merge.

## Team Members
Bjarni Anton Bjarnason, Elmar Sigmarsson, Isak Eli Hauksson, Sindri Freysson, Tomas Karl Robertsson, Vigfus Haukur Hauksson, Viktor Yngvi Isaksson
