@echo off
set PYTHONPATH=.

python -m pytest tests/ -v

rem Or run individually:
rem python tests/test_vector.py -v
rem python tests/test_linked_list.py -v
rem python tests/test_algorithms.py -v
rem python tests/test_card_data_handler.py -v
