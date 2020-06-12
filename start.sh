#!/bin/bash

function prepare {
    sh prepare.sh
}

function gitClone {
    sh git_clone.sh
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

function calculateGitCommitScore {
    cd git_commit
    sh start.sh
    cd ..
}

function main {
    prepare
    detectQuestionName
    gitClone
    calculateCodeSmellScore
    calculateTestCoverageScore
    calculateGitCommitScore
}

main