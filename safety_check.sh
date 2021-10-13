#!/bin/sh
# pyup.io
figlet safety
safety check | tee safety_report.txt
