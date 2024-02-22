pipeline {
    agent any
    
    stages {
        stage('Docker Setup') {
            steps {
                sh 'whoami'
                sh 'sudo apt update '
            }
        }

        stage('test') {
            steps {
                sh 'echo "Testing..."'
                sh 'python --version'                
            }
        }
    }
}