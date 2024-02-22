pipeline {
    agent { docker { image 'python:3.12.1-alpine3.19' } }
    
    stages {
        stage('Docker Setup') {
            steps {
                sh 'sudo apt update '
                sh 'sudo apt install docker'
            }
        }

        stage('test') {
            steps {
                sh 'echo "Testing..."'
                sh 'sudo apt install python'
                sh 'python --version'                
            }
        }
    }
}