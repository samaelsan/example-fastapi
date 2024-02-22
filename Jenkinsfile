pipeline {
    agent any
    
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