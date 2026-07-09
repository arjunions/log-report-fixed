#!/bin/bash

mkdir -p /logs/verifier

pytest /tests/test_outputs.py -rA
EXIT_CODE=$?

if [ $EXIT_CODE -eq 0 ]; then
  echo 1 > /logs/verifier/reward.txt
  echo '{"results":{"tool":"pytest","summary":{"passed":1,"failed":0}}}' > /logs/verifier/ctrf.json
else
  echo 0 > /logs/verifier/reward.txt
  echo '{"results":{"tool":"pytest","summary":{"passed":0,"failed":1}}}' > /logs/verifier/ctrf.json
fi
