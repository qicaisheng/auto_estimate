#!/bin/bash

PMD_BIN_FOLDER_NAME="pmd-bin-6.24.0"
PMD_RULESETS_NAME="pmd-rulesets.xml"
DATA_DIRECTORY='../../data'
PMD_RESULT_REPORT_JSON_NAME="pmd-result-report.json"
PMD_RESULT_REPORT_HTML_NAME="pmd-result-report.html"
declare codeRepositoryFolderPath

function readCurrentWorkspacePath {
    codeRepositoryFolderPath=$(cat $DATA_DIRECTORY/currentWorkspacePath.txt)
}

function executePMD {
    ./${PMD_BIN_FOLDER_NAME}/bin/run.sh pmd -d ${codeRepositoryFolderPath} -f json -R ./${PMD_RULESETS_NAME} -r ${codeRepositoryFolderPath}/${PMD_RESULT_REPORT_JSON_NAME}
    ./${PMD_BIN_FOLDER_NAME}/bin/run.sh pmd -d ${codeRepositoryFolderPath} -f html -R ./${PMD_RULESETS_NAME} -r ${codeRepositoryFolderPath}/${PMD_RESULT_REPORT_HTML_NAME}

	echo "PMD report is: ${codeRepositoryFolderPath}/${PMD_RESULT_REPORT_HTML_NAME}"
}

function main {
	readCurrentWorkspacePath
    executePMD
}

main