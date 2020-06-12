#!/bin/bash

function prepareWorkspace {
    sh prepare_workspace.sh
}

function detectQuestionName {
    sh detect_question_name.sh
}

function calculateCodeSmellScore {
    cd code_smell
    sh start.sh
    cd ..
}

function calculateTestCoverageScore {
    cd test_coverage
    sh start.sh
    cd ..
}

function main {
    prepareWorkspace
    detectQuestionName
    calculateCodeSmellScore
    calculateTestCoverageScore
}

main