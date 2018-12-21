pipeline {
  agent {
    label 'jenkins-jx-base'
  }
  stages {
    stage('print') {
      steps {
        sh '''touch /tmp/test
echo hello world'''
      }
    }
  }
}