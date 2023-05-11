pipeline{
  agent any
  
  environment{
    SSH_USER = "azureuser"
    SSH_HOST = "52.146.92.195"
    SSH_KNOWN_HOSTS = ""
    DESTINATION_FOLDER = ""
  }  
  
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
            sh 'service nginx status'
            sh 'ssh azureuser@52.146.92.195'
            
            
            
            sh "scp -r build/* azureuser@52.146.92.195:var/www/html"
            }catch(e){
              sh 'echo "Build failed: $(e.message)"'
            }
        }
      }
    }
    post{
      success{
        sh 'echo success'
      }
      failure{
        sh 'echo failure'
      }
    }
  }
}
