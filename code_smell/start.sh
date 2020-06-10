#!/bin/bash

function check_pmd {
	cd pmd_checker
	sh runPMD.sh
	cd ..
}

function calcuate_score {
	cd score_calculator/src
	python score_calculator.py
	cd ../..
}

function main {
    check_pmd
    calcuate_score
}

main