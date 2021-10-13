#!/bin/sh
figlet bandit
bandit -r . | tee bandit_report.txt
