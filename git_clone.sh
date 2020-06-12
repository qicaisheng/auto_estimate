#!/bin/bash

declare gitRepositoryURL
declare currentWorkspacePath
WORK_SPACE_DIRECTORY='./workspace'
DATA_DIRECTORY='./data'

function readGitRepositoryURLFromInput {
	echo "请输入需要检查的git repository url，例如：https://github.com/pmd/pmd.git"

    read -p 'git repository url:' gitRepositoryURL
	echo "需要检查的代码git repository url:${gitRepositoryURL}"
}

function gitClone {
    cd ${WORK_SPACE_DIRECTORY}
   
    local currentWorkspace=${gitRepositoryURL#*//*/}
    currentWorkspace=${currentWorkspace////_}
   
    rm -rf ${currentWorkspace}
    mkdir ${currentWorkspace}
   
    cd ${currentWorkspace}
    git clone ${gitRepositoryURL} code

    currentWorkspacePath=$PWD

    cd ../..
}

function writeCurrentWorkspacePathToData {
    echo ${currentWorkspacePath} > ${DATA_DIRECTORY}/currentWorkspacePath.txt
}


function main {
    readGitRepositoryURLFromInput
    gitClone
    writeCurrentWorkspacePathToData
}

main