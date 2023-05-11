pipeline{
  agent any
  
  stages{
    stage('Build'){
      steps{
        try{
          sh 'echo "Build started"'
          sh 'npm install'
          sh 'npm run build'
          }catch(e){
            sh 'echo "Build failed: $(e)"'
          }
      }
    }
  }
}
