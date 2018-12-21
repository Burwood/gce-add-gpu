pipeline {
  agent {
    label 'jenkins-bash'
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