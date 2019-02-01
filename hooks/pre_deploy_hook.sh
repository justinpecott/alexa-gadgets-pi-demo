#!/bin/bash
# Shell script for ask-cli pre-deploy hook for Node.js
# Script Usage: pre_deploy_hook.sh <SKILL_NAME> <DO_DEBUG> <TARGET>

# SKILL_NAME is the preformatted name passed from the CLI, after removing special characters.
# DO_DEBUG is boolean value for debug logging
# TARGET is the deploy TARGET provided to the CLI. (eg: all, skill, lambda etc.)

# Run this script under skill root folder

# The script does the following:
#  - Run "npm install" in each sourceDir in skill.json

SKILL_NAME=$1
DO_DEBUG=${2:-false}
TARGET=${3:-"all"}

if [ $DO_DEBUG == false ]
then
    exec > /dev/null 2>&1
fi

echo "###########################"
echo "##### pre-deploy hook #####"
echo "###########################"

build_codebase() {
    npm run build
    return $?
}

echo -e "\nBuilding codebase."
if build_codebase; then
    echo "Codebase built successfully."
    exit 0
else
    echo "There was a building codebase."
    exit 1
fi
