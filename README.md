# Algorithms

Educational set of data structures and algorithms in Python, with tests and benchmarks.

This repository is intended for coursework and experimentation: you can explore core data structures, verify correctness with tests, and compare performance using included benchmark scripts.

## Structure
- [src/](src/) - implementations of algorithms and data structures.
- [tests/](tests/) - unit tests.
- [benchmarks/](benchmarks/) - benchmarks.
- [data/](data/) - source datasets.
- [generated_data/](generated_data/) and [outputs/](outputs/) - generated artifacts and run outputs.

## Implementations overview
- [src/linked_list.py](src/linked_list.py) - linked list implementation and operations.
- [src/vector.py](src/vector.py) - dynamic array / vector structure.
- [src/trees.py](src/trees.py) - tree structures (BST/AVL/TST) and operations.
- [src/card_data_handler.py](src/card_data_handler.py) - dataset parsing and normalization helpers.
- [src/utils.py](src/utils.py) - shared utilities.

## Requirements
- Python 3.10+

## Installation
1. Install dependencies from [requirements.txt](requirements.txt).
2. Optionally install the project in editable mode.

## Usage notes
- Algorithms are exposed through modules in [src/](src/). Import the needed structure or function directly.
- CSV inputs used in some tasks are stored in [data/](data/), while generated results are saved to [outputs/](outputs/).

## Tests
- Run tests via [test.bat](test.bat).

## Benchmarks
- Runner scripts are in [benchmarks/](benchmarks/).
- Benchmark outputs are written to [outputs/](outputs/).

## Entry points
- Core logic lives in [src/](src/).

## Project goals
- Provide clear reference implementations for common data structures.
- Maintain deterministic, repeatable tests.
- Support lightweight benchmarking for comparison and analysis.