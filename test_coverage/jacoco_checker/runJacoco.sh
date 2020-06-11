#!/bin/bash

DATA_DIRECTORY='../../data'
declare currentWorkspacePath

function readCurrentWorkspacePath {
    currentWorkspacePath=$(cat ${DATA_DIRECTORY}/currentWorkspacePath.txt)
}

function executeJacoco {
    cd ${currentWorkspacePath}
    mkdir -p jacoco
    cd code
    
    if [[ -f "./mvnw" ]]; then
        ./mvnw clean test
        cp -R target/site/jacoco/ ../jacoco
    elif [[ -f "./gradlew" ]]; then
        ./gradlew clean test jacocoTestReport
        cp -R build/reports/jacoco/test ../jacoco
    elif [[ -f "pom.xml" ]]; then
        mvn clean test
        cp -R target/site/jacoco/ ../jacoco
    elif [[ -f "build.gradle" ]]; then
        gradle clean test jacocoTestReport
        cp -R build/reports/jacoco/test ../jacoco
    fi
}

function main {
    readCurrentWorkspacePath
    executeJacoco
}

main