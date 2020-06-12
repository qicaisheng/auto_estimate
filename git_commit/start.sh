#!/bin/bash


function generateGitCommitReport {
	sh generate_git_commit_report.sh
}

function calculateScore {
	python score_calculator.py
}

function main {
    generateGitCommitReport
    calculateScore
}

main