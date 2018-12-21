pipeline {
  agent {
    docker {
      image 'centos'
    }

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