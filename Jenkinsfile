pipeline{
  agent any
  stage('Build'){
    steps{
      try{
        sh 'echo "Build started"'
        sh 'npm install'
        sh 'npm run build'
        }catch(e){
          echo "Build failed: $(e)"
        }
      }
    }
  }
}
