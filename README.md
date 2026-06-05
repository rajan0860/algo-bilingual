# algo-bilingual

A bilingual data structures and algorithms practice repository with parallel Python and Go solutions. Each problem includes a `notes.md` file comparing the pattern, complexity, implementation details, and language-specific tradeoffs.

---

## Purpose

This repository is designed to:
- improve algorithmic thinking with consistent problem patterns
- reinforce idiomatic Python and idiomatic Go implementations
- make language differences explicit rather than hiding them behind syntax
- support interview prep and cross-language learning

## Why Both Languages?

Most DSA practice focuses on one language. This repo solves each problem in both Python and Go so you can:
- compare a fast Python prototype with an explicit Go implementation
- learn how the same algorithm maps to two runtime models
- identify where convenience helps and where explicitness matters

| Python 🐍 | Go ⚡ |
|---|---|
| fast prototyping | explicit performance
| dynamic typing | strong typing
| rich standard library | minimal runtime and concurrency support
| common in AI/ML roles | common in backend and systems roles |

---

## Prerequisites & Setup

To work with this repository, ensure you have the following installed:
* **Python**: `3.10+` (leveraging modern standard library type hints)
* **Go**: `1.18+` (supporting standard constructs and generics if needed)

No external libraries are required, as solutions rely entirely on standard library packages.

To initialize your local Go environment:
```bash
# Verify Go installation and path setup
go version
# The Go module has been pre-configured for the repository
```

---

## Repo Structure

```
algo-bilingual/
├── arrays/
│   └── two_sum/
│       ├── solution.py
│       ├── solution.go
│       └── notes.md
├── linked-list/
├── stacks-queues/
├── trees/
├── graphs/
├── binary-search/
├── sliding-window/
├── two-pointers/
├── dynamic-programming/
├── backtracking/
└── sorting/
```

Each problem folder should contain:
- `solution.py` — idiomatic Python solution
- `solution.go` — idiomatic Go solution
- `notes.md` — pattern, complexity, and a direct comparison of both implementations

---

## Progress Tracker

A central table to track problem-solving and comparison notes. This table is updated automatically when using the `scaffold.py` script.

| # | Problem | Category | Python 🐍 | Go ⚡ | Notes 📝 | Difficulty |
|---|---|---|---|---|---|---|
<!-- START_TRACKER -->
| 001 | [Two Sum](./arrays/two_sum/) | Arrays | ⏳ In Progress | ❌ Todo | ❌ Todo | Easy |
| 002 | [Reverse Linked List](./linked-list/reverse_linked_list/) | Linked List | ⏳ In Progress | ❌ Todo | ❌ Todo | Easy |
<!-- END_TRACKER -->

---

## How to Use This Repo

1. Choose a category and open a problem folder.
2. Read `notes.md` to understand the problem pattern.
3. Compare `solution.py` and `solution.go` implementations.
4. Run and test each solution if tests are available.
5. Add your own notes on pitfalls or alternative approaches.

---

## Testing Your Solutions

### Python
Python solutions can be tested by executing them directly if they contain embedded assertions or main function wrappers, or via standard testing tools:
```bash
python <category>/<problem_name>/solution.py
```

### Go
Go solutions can be run directly or tested via the standard `go test` suite:
```bash
# Run a specific solution
go run <category>/<problem_name>/solution.go

# Run tests (if *_test.go is present)
go test ./...
```

---

## Adding a New Problem

You can automate the creation of new problem folders using the helper script `scaffold.py`:

```bash
# Option 1: Interactive mode (will prompt you step-by-step)
python scaffold.py

# Option 2: Command-line mode
python scaffold.py --category arrays --name "Two Sum" --difficulty Easy
```

This script will:
1. Create the appropriate subdirectory structure.
2. Generate template boilerplate for `solution.py`, `solution.go`, and `notes.md`.
3. Auto-register the problem and update the table in [Progress Tracker](#progress-tracker).

To add a problem manually:
1. Create a new folder in the appropriate category.
2. Add `solution.py` with a clear Python solution.
3. Add `solution.go` with a clear Go solution.
4. Create `notes.md` describing the approach, complexities, and tradeoffs using the template below.

---

## Notes Template (per problem)

Every `notes.md` follows this structure:

```
Pattern        → e.g. Two Pointers / Sliding Window / DFS
Approach       → step-by-step logic before any code
Complexity     → time and space for both languages
Key Differences → what Go makes explicit that Python hides
Gotchas        → edge cases, common mistakes
Problem Link   → original problem source or ID
Status         → solved / in progress / review needed
```

---

## Workflow Per Problem

1. Watch a lecture or read the problem statement.
2. Solve in Python first for rapid validation.
3. Re-implement in Go to reinforce explicit design.
4. Write or update `notes.md` with cross-language comparisons.
5. Commit one problem at a time for clean history.

---

## Connect

- GitHub: [rajan0860](https://github.com/rajan0860)
