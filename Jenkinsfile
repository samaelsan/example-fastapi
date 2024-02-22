pipeline {
    agent any
    
    stages {
        stage('Git Checkout') {
            steps {
                script {
                    git branch: 'main',
                        credentialsId: 'e35a5e28-e9b7-4c7d-adeb-0f68dd2fc55f'
                        url: 'https://github.com/samaelsan/example-fastapi'
                }
            }
        }

        stage('build') {
            steps {
                sh 'python--version'
                sh 'whoiam'
            }
        }
    }
}