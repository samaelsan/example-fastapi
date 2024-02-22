pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                sh 'echo "Building.."'
                sh 'whoami'
            }
        }

        stage('test') {
            steps {
                sh 'echo "Testing..."'
                sh 'python --version'
                sh 'whoami'
            }
        }
    }
}