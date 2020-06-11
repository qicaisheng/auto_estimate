#!/bin/bash

declare currentWorkspacePath
DATA_DIRECTORY='./data'

function prepare_workspace {
    sh prepare_workspace.sh
}

function get_current_workspace_path {
    currentWorkspacePath=$(cat $DATA_DIRECTORY/currentWorkspacePath.txt)
    echo "current workspace path is: $currentWorkspacePath"
}

function main {
    prepare_workspace
    get_current_workspace_path
}

main