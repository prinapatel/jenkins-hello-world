#!/usr/bin/env/groovy

pipeline {
    agent { dockerfile true } 
    stages {
        stage('Stage 1') {
            steps {
				echo 'This was pushed'
                echo 'Hello world!' 
            }
        }
		stage('Python and Docker Statge') {
			steps {
				sh 'python --version'	
			}
		}
    }
}
