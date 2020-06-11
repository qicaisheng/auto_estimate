#!/bin/bash

declare currentWorkspacePath

function prepare_workspace {
    sh prepare_workspace.sh
}

function calculate_code_smell_score {
    cd code_smell
    sh start.sh
}

function main {
    prepare_workspace
    calculate_code_smell_score
}

main