@echo off
set PYTHONPATH=.
python tests/test_algorithms.py -v
python tests/test_card_data_handler.py -v
