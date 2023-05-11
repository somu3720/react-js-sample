pipeline{
  agent any
  
  stages{
    stage('Build'){
      steps{
        script{
          try{
            sh 'echo "Build started"'
            sh 'npm run build'
            }catch(e){
              sh 'echo "Build failed: $(e.message)"'
            }
        }
      }
    }
    stage('Deploy'){
      steps{
        script{
          try{
            sh 'echo "Deployment started"'
            sh "scp -r build/* azureuser@52.146.92.195:var/www/html"
            }catch(e){
              sh 'echo "Build failed: $(e.message)"'
            }
        }
      }
    }
  }
}
