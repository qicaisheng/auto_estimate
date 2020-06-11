#!/bin/bash

declare currentWorkspacePath

function prepare_workspace {
    sh prepare_workspace.sh
}

function main {
    prepare_workspace
}

main