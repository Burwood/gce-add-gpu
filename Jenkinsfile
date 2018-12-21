pipeline {
  agent {
    label 'jenkins-jx-base'
  }
  stages {
    stage('Docker Build') {
      agent {
        dockerfile {
          filename 'Dockerfile'
        }

      }
      steps {
        sh 'docker build -t gce-add-gpu:latest .'
      }
    }
    stage('Push to Repo') {
      steps {
        sh 'echo toDO: push to repo'
      }
    }
  }
}