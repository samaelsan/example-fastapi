pipeline {
    agent any
    
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