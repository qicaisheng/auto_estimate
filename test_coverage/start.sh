#!/bin/bash


function runJacoco {
	cd jacoco_checker
	sh runJacoco.sh
	cd ..
}

function calculateScore {
	cd score_calculator/src
	python score_calculator.py
	cd ../..
}

function main {
    runJacoco
    calculateScore
}

main