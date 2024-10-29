pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/abhishekSingh22222/devops-website.git'
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
                sh 'docker run -d -p 8080:80 --name test-container devops-website:latest'
                sh 'pytest tests/test_homepage.py'
            }
            post {
                always {
                    sh 'docker stop test-container'
                    sh 'docker rm test-container'
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    sh 'docker stop website-container || true'
                    sh 'docker rm website-container || true'
                    sh 'docker run -d -p 80:80 --name website-container devops-website:latest'
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
