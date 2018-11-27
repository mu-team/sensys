#!/usr/bin/env bash

SENSYS_VERSION=0.1.0

DIST_DIR="${PWD}/dist"
DIST_MAP="${DIST_DIR}/map.json"
DIST_CFG="${DIST_DIR}/80-sensys.conf"

if [ -d ${1} ]; then
    echo "SEPARATOR is not define";
    exit 1;
fi

# Installation
sudo pip3 install ${DIST_DIR}/sensys-${SENSYS_VERSION}.tar.gz

PLUGIN_PATH=$(which sensys)
SENSYS_PATH=/etc/sensys
RSYSLOG_PATH=/etc/rsyslog.d

# additional configuration
sudo mkdir -p ${SENSYS_PATH}

# setup rsyslog
sed -i "
    s|--SEPARATOR--|${1}|g
    s|--MAPPING--|${SENSYS_PATH}/map.json|g
    s|--PLUGIN_PATH--|${PLUGIN_PATH}|g" ${DIST_CFG}

sudo cp --backup=numbered ${DIST_MAP} ${SENSYS_PATH}/
sudo cp ${DIST_CFG} ${RSYSLOG_PATH}/
