#!/usr/bin/env bash

set -e

DIST_DIR="${PWD}/dist"
DIST_MAP="${DIST_DIR}/map.json"
DIST_CFG="${DIST_DIR}/80-sensys.conf"

# clean previous setup
rm -rf ${DIST_DIR}

# make sensys distribution
mkdir -p ${DIST_DIR}
python3 setup.py sdist
cp ${PWD}/resources/rsyslog-receiver.example.conf ${DIST_CFG}
cp ${PWD}/resources/map.example.json ${DIST_MAP}
