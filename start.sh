#!/bin/bash

function prepareWorkspace {
    sh prepare_workspace.sh
}

function calculateCodeSmellScore {
    cd code_smell
    sh start.sh
}

function main {
    prepareWorkspace
    calculateCodeSmellScore
}

main