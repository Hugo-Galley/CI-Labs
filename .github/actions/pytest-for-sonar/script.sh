#!/usr/bin/env bash

MODULE="$1"
pytest --cov=$MODULE --cov-report=xml

if grep -q "$GITHUB_WORKSPACE" coverage.xml; then
            sed -i "s|$GITHUB_WORKSPACE/||g" coverage.xml || true
            head -n 40 coverage.xml || true
fi