#!/bin/bash

function checkPmd {
	cd pmd_checker
	sh runPMD.sh
	cd ..
}

function calculateScore {
	cd score_calculator/src
	python score_calculator.py
	cd ../..
}

function main {
    checkPmd
    calculateScore
}

main