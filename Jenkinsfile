pipeline {
    agent {docker { image 'python:3.12.1-alpine3.19'}}
    
    stages {
        stage('Build') {
            steps {
                sh 'echo "Building.."'
                sh 'whoiam'
            }
        }

        stage('test') {
            steps {
                sh 'python --version'
                sh 'whoiam'
            }
        }
    }
}