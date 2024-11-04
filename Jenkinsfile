pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/abhishekSingh22222/devops-website.git', credentialsId: 'github-token'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build('devops-website:latest')
                }
            }
        }

        stage('Run Tests') {
            steps {
                bat 'docker run -d -p 8080:80 --name test-container devops-website:latest'
                bat 'pytest tests/test_homepage.py'
            }
            post {
                always {
                    bat 'docker stop test-container'
                    bat 'docker rm test-container'
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    bat 'docker stop website-container || true'
                    bat 'docker rm website-container || true'
                    bat 'docker run -d -p 80:80 --name website-container devops-website:latest'
                }
            }
        }
    }

    post {
        success {
            echo 'Website successfully built, tested, and deployed!'
        }
        failure {
            echo 'Build failed.'
        }
    }
}
