pipeline {
    agent {docker { image 'python:3.12.1-alpine3.19'}}
    
    stages {

        stage('test') {
            steps {
                sh 'python --version'
                sh 'whoiam'
            }
        }
    }
}