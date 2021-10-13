#!/bin/sh
# https://github.com/Bachmann1234/diff-cover
figlet diff
coverage xml
diff-cover coverage.xml
diff-quality --violations=flake8
echo "Implement diff check"
