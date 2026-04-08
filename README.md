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
Open the command console in the project root and run
```
python Project/main.py
```

## Unit testing (Exercise 5.2)
Test coverage is currently split across:
* `tests/test_event_and_logic.py`
* `test_assignment63_regression.py`

Run the main unit test suite:
```
python -m unittest discover -s tests -p "test_*.py" -v
```

Run the regression suite:
```
python -m unittest test_assignment63_regression.py -v
```

Measure coverage (after installing `coverage`):
```
python -m pip install coverage
python -m coverage run -m unittest discover -s tests -p "test_*.py"
python -m coverage run -a -m unittest test_assignment63_regression.py
python -m coverage report -m
```

Functionalities tested:
* Event time tag generation (`morning/afternoon/evening/night`, `weekday/weekend`, month)
* Event tag normalization and merge logic
* Private event visibility rules
* Invite-user behavior (duplicate prevention)
* Visible-events filtering by user access
* Sorting visible events by name and date fallback
* Sorting visible events by branch
* Event creation storage in logic layer
* Join-event duplicate prevention
* Event reporting validation
* Favorite-event add/remove behavior
* Viewing favorite events that still exist
* Viewing old events for attended ended events

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
* The repository currently passes both test suites and `ruff check .`.

## Team Members
Bjarni Anton Bjarnason, Elmar Sigmarsson, Isak Eli Hauksson, Sindri Freysson, Tomas Karl Robertsson, Vigfus Haukur Hauksson, Viktor Yngvi Isaksson
