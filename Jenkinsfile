pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/yourusername/devops-website.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image
                    def dockerImage = docker.build('devops-website:latest')
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Run tests inside the Docker container
                    def dockerImage = docker.image('devops-website:latest')
                    dockerImage.inside("-p 8080:80") {
                        bat 'pytest tests/test_homepage.py'
                    }
                }
            }
            post {
                always {
                    // Clean up container after tests
                    bat 'docker stop test-container || true'
                    bat 'docker rm test-container || true'
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Stop and remove any previous container, then deploy
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
