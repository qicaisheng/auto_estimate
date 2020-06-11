#!/bin/bash


function runJacoco {
	cd jacoco_checker
	sh runJacoco.sh
	cd ..
}

function main {
    runJacoco
}

main