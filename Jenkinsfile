pipeline {
    agent any

    tools {
        jdk 'JAVA_HOME'
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Code pulled from GitHub'
            }
        }

        stage('Build') {
            steps {
                bat 'javac Hello.java'
            }
        }

        stage('Test') {
            steps {
                bat 'java Hello Jenkinsfile'
            }
        }
    }

    post {
        success {
            echo 'BUILD SUCCESSFUL ✅'
        }
        failure {
            echo 'BUILD FAILED ❌'
        }
        always {
            echo 'Pipeline execution finished.'
        }
    }
}
