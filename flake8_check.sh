#!/bin/sh
figlet flake8
flake8 | tee flake8_report.txt
