pipeline {
    agent any

    environment {
        IMAGE_NAME = 'devops-website:latest'
        TEST_CONTAINER = 'test-container'
        DEPLOY_CONTAINER = 'website-container'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/abhishekSingh22222/devops-website.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image with a specific tag
                    docker.build("${IMAGE_NAME}")
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Run the Docker container in detached mode for testing
                    sh "docker run -d -p 8080:80 --name ${TEST_CONTAINER} ${IMAGE_NAME}"
                    // Run tests (replace 'tests/test_homepage.py' with the correct path if different)
                    sh 'pytest tests/test_homepage.py'
                }
            }
            post {
                always {
                    // Ensure the test container is stopped and removed
                    script {
                        sh "docker stop ${TEST_CONTAINER} || true"
                        sh "docker rm ${TEST_CONTAINER} || true"
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Stop and remove the existing deployment container if it exists
                    sh "docker stop ${DEPLOY_CONTAINER} || true"
                    sh "docker rm ${DEPLOY_CONTAINER} || true"
                    // Run the new Docker container as the deployment
                    sh "docker run -d -p 80:80 --name ${DEPLOY_CONTAINER} ${IMAGE_NAME}"
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
