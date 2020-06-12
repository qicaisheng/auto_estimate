#!/bin/bash

WORK_SPACE_DIRECTORY='./workspace'
DATA_DIRECTORY='./data'

function prepareWorkspace {
    if [[ ! -d ${WORK_SPACE_DIRECTORY} ]]; then
		mkdir ${WORK_SPACE_DIRECTORY}
	fi
}

function prepareData {	
    if [[ ! -d ${DATA_DIRECTORY} ]]; then
		mkdir ${DATA_DIRECTORY}
	fi
}

function prepare {
    prepareWorkspace
    prepareData
}


function main {
    prepare
}

main