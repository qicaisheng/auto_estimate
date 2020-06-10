#!/bin/bash

PMD_BIN_FOLDER_NAME="pmd-bin-6.24.0"
PMD_RULESETS_NAME="pmd-rulesets.xml"
declare codeRepositoryFolderPath
declare pmdResultReport="./pmd-result-report.json"

function readCodeRepositoryFolderPathFromInput {
	echo "请输入需要检查的代码绝对路径，例如：/path/code/example/src"

	while true; do
		read -p '代码绝对路径：' codeRepositoryFolderPath
		if [[ -d ${codeRepositoryFolderPath} ]]; then
			break
		else
			echo "请输入有效的绝对路径"
  	    fi
	done
	echo "需要检查的代码绝对路径：${codeRepositoryFolderPath}"
}

function executePMD {
    ./${PMD_BIN_FOLDER_NAME}/bin/run.sh pmd -d ${codeRepositoryFolderPath} -f json -R ./${PMD_RULESETS_NAME} -r ${pmdResultReport}
}

function main {
    readCodeRepositoryFolderPathFromInput
    executePMD
}

main