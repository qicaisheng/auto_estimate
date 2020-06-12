#!/bin/bash

declare currentQuestionName
DATA_DIRECTORY='./data'

function readQuestionNameFromInput {
	echo "请输入需要当前检测的题目名称，例如：guessNumber, fizzBuzz. 默认为guessNumber"

    read -p '当前检测的题目名称: ' currentQuestionName
    if [[ "${currentQuestionName}" = '' ]]; then
        currentQuestionName='guessNumber'
    fi
	echo "当前需要检查的题目名称: ${currentQuestionName}"
}

function writeCurrentQuestionNameToData {
    echo ${currentQuestionName} > ${DATA_DIRECTORY}/currentQuestionName.txt
}

function main {
    readQuestionNameFromInput
    writeCurrentQuestionNameToData
}

main