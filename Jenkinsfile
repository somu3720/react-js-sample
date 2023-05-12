pipeline{
  agent any
  
  environment{
    SSH_USER = "deployserver"
    SSH_HOST = "20.127.193.201"
    //SSH_KNOWN_HOSTS = ""
    DESTINATION_FOLDER = "/usr/share/nginx/html"
    BACKUP_FOLDER = "/home/azureuser/backup/"
    ROLLBACK_FOLDER = "/home/azureuser/rollback"
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
    stage('Pre Deploy'){
      steps{
        script{
          try{
            //sh "mkdir -p ${DESTINATION_FOLDER} && test -d ${DESTINATION_FOLDER}"
            //sh "mkdir -p ${BACKUP_FOLDER} && test -d ${BACKUP_FOLDER}
            //sh "mkdir -p ${ROLLBACK_FOLDER} && test -d ${ROLLBACK_FOLDER}
            //sh "tar -czvf build_$BUILD_NUMBER.tar.gz *"
            //sh "mv build/* ${BACKUP_FOLDER}"
            //sh "rm -rf *tar.gz"
            
            
            //sh 'ssh azureuser@52.146.92.195'
            
            
       
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
            //sh 'service nginx status'
            sh "sshpass -p Deployserver@1 scp -o StrictHostKeyChecking=no -r build/* ${SSH_USER}@${SSH_HOST}:${DESTINATION_FOLDER}"
            
            }catch(e){
              sh 'echo "Build failed: $(e.message)"'
              //sh 'echo "Rollback started"'
              //sh "mv ${BACKUP_FOLDER} ${ROLLBACK_FOLDER} && mv ${ROLLBACK_FOLDER} ${DESTINATION_FOLDER}"
            }
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
