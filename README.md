# algo-bilingual

A bilingual data structures and algorithms practice repository featuring parallel **Python** and **Go** solutions. Each problem includes a structured `notes.md` file comparing patterns, complexity, implementation details, and language-specific tradeoffs.

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Go](https://img.shields.io/badge/Go-1.18+-00ADD8?style=flat-square&logo=go&logoColor=white)](https://go.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

---

## Purpose

This repository is designed to:
- **Improve algorithmic thinking** by identifying consistent, language-agnostic problem patterns.
- **Reinforce idiomatic syntax** and design choices in both Python and Go.
- **Expose runtime models** and language differences explicitly rather than hiding them behind syntax.
- **Support interview preparation** and cross-language learning.

## Why Both Languages?

Most DSA practice focuses on a single language. Solving each problem in both Python and Go allows you to:
- Compare a fast, high-level Python prototype with an explicit, high-performance Go implementation.
- Understand how the same algorithm maps to two different runtime and memory models.
- Identify where Python's convenience helps versus where Go's type-safety and explicitness prevent bugs.

| Feature / Aspect | Python 🐍 | Go ⚡ |
| :--- | :--- | :--- |
| **Development** | Fast prototyping, concise syntax | Explicit, structured code |
| **Typing** | Dynamic typing | Strong, static typing |
| **Standard Library** | Rich, built-in algorithms/data structures | Minimal runtime, built-in concurrency |
| **Primary Industry Use** | AI/ML, data science, scripting | Backend systems, cloud, microservices |

---

## Prerequisites & Setup

Ensure you have the following installed:
* **Python**: `3.10+` (leveraging modern standard library type hints)
* **Go**: `1.18+` (supporting standard constructs and generics)

All solutions rely strictly on the standard library—no external dependencies or external packages are required.

To verify your environment:
```bash
python --version
go version
```

---

## Repo Structure

```text
algo-bilingual/
├── arrays/
│   └── two_sum/
│       ├── solution.py   # Idiomatic Python solution
│       ├── solution.go   # Idiomatic Go solution
│       └── notes.md      # Approach, complexity analysis, and comparisons
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

Each problem folder contains:
- `solution.py` — Idiomatic Python solution
- `solution.go` — Idiomatic Go solution
- `notes.md` — Problem analysis, complexity table, and a direct comparison of both implementations

---

## Progress Tracker

A central table to track problem-solving and comparison notes. This table is updated automatically when using the `scaffold.py` script.

### Status Legend
- ❌ **`Todo`**: Solution has not been started.
- ⏳ **`In Progress`**: Solution is under active implementation or review.
- ✅ **`Solved`** / **`Completed`**: Solution is fully implemented and tested.

| # | Problem | Category | Python 🐍 | Go ⚡ | Notes 📝 | Difficulty |
|---|---|---|---|---|---|---|
<!-- START_TRACKER -->
| 001 | [Two Sum](./arrays/two_sum/) | Arrays | ⏳ In Progress | ❌ Todo | ❌ Todo | Easy |
| 002 | [Reverse Linked List](./linked-list/reverse_linked_list/) | Linked List | ⏳ In Progress | ❌ Todo | ❌ Todo | Easy |
<!-- END_TRACKER -->

---

## Testing & Execution

### Running Python Solutions

Execute the solution script directly to run embedded assertions or main function wrappers:
```bash
python arrays/two_sum/solution.py
```

### Running Go Solutions

Run the solution file directly:
```bash
go run arrays/two_sum/solution.go
```

To run all tests (if any `*_test.go` files are present in the package):
```bash
go test ./...
```

---

## Coding Standards & Conventions

To keep the codebase consistent:
1. **Standard Library Only**: Do not add external dependencies to `go.mod` or use `pip` packages.
2. **Self-Contained Runner**: Each `solution.py` and `solution.go` should contain a driver function (`if __name__ == "__main__":` or `func main()`) demonstrating a simple verification test.
3. **Bilingual Mirroring**: Use parallel naming for variables, data structures, and functions, adapting to each language's idiomatic styling (e.g. CamelCase in Go, snake_case in Python).

---

## Adding a New Problem

You can automate the creation of new problem folders using the helper script `scaffold.py`:

```bash
# Option 1: Interactive mode (will prompt you step-by-step)
python scaffold.py

# Option 2: Command-line mode
python scaffold.py --category arrays --name "Two Sum" --difficulty Easy
```

### Supported Categories & Difficulties

When using the command-line options, choose from:
- **Categories**: `arrays`, `linked-list`, `stacks-queues`, `trees`, `graphs`, `binary-search`, `sliding-window`, `two-pointers`, `dynamic-programming`, `backtracking`, `sorting`
- **Difficulties**: `Easy`, `Medium`, `Hard`

The script will:
1. Create the appropriate subdirectory structure.
2. Generate boilerplate templates for `solution.py`, `solution.go`, and `notes.md`.
3. Auto-register the problem and update the table in [Progress Tracker](#progress-tracker).

---

## Notes Template (per problem)

Every `notes.md` follows this structure:

```markdown
# Problem Name

| Pattern | Time Complexity | Space Complexity | Difficulty |
|---|---|---|---|
| Pattern Name | O(N) | O(1) | Easy/Medium/Hard |

---

## Approach
*Provide a step-by-step breakdown of the logic before coding.*

## Key Differences

| Python 🐍 | Go ⚡ |
|---|---|
| *dynamic / simple* | *strongly typed / explicit* |

## Gotchas & Edge Cases
- Edge case 1

---

## Resources
- **Problem Link:** [LeetCode]()
- **Status:** ⏳ In Progress
```

---

## Connect

- GitHub: [rajan0860](https://github.com/rajan0860)
