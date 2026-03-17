pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                echo 'Clonación gestionada por Jenkins desde SCM'
            }
        }

        stage('Test') {
            steps {
                sh 'python3 -m pip install flask pytest'
                sh 'pytest'
            }
        }

        stage('Build Image') {
            steps {
                sh 'docker build -t bkrrt/proyecto-ci-cd-fatima:latest .'
            }
        }

        stage('DockerHub') {
            steps {
                sh 'docker push bkrrt/proyecto-ci-cd-fatima:latest'
            }
        }

        stage('Deploy') {
            steps {
                sh 'minikube kubectl -- apply -f deployment.yaml'
                sh 'minikube kubectl -- apply -f service.yaml'
            }
        }
    }
}
