#!/bin/bash

declare currentWorkspacePath
DATA_DIRECTORY='../data'
GIT_COMMIT_REPORT_FOLDER_NAME='git_commit'

function readCurrentWorkspacePath {
    currentWorkspacePath=$(cat ${DATA_DIRECTORY}/currentWorkspacePath.txt)
}

function generateGitCommitReport {
    cd ${currentWorkspacePath}
    mkdir -p ${GIT_COMMIT_REPORT_FOLDER_NAME}
    cd code
    git log --pretty=oneline --abbrev-commit > ${currentWorkspacePath}/${GIT_COMMIT_REPORT_FOLDER_NAME}/git-commit-report.txt
}


function main {
    readCurrentWorkspacePath
    generateGitCommitReport
}

main