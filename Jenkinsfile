pipeline {
  agent any
  environment {
    SSH_USER = "deploynginx"
    SSH_HOST = "20.55.8.149"
 //   CURRENT_DATE = new Date().format("yyyy-MM-dd_HH-mm-ss")
    DESTINATION_FOLDER1 = "/var/www/example.com/html"
    DESTINATION_FOLDER2 = "/var/www/test.com/html"
    BACKUP_FOLDER = "backup_RI"
    ROLLBACK_FOLDER = "rollback_RI"
  }
  
  stages {
    stage('Build') {
      steps {
        
          
            script {
              try {
                sh 'echo "Build started"'
                sh 'npm run build'
                sh 'echo "Build Ended"'
              } catch (e) {
                sh 'echo "Build failed: $(e.message)"'
                
              }
            
        }
      }
    }
    
    stage('Pre Deploy') {
      steps {
        
          
            script {
              try {
                sh 'echo "Ssh Login started"'
                sh "ssh '${SSH_USER}@${SSH_HOST}'"
                sh "scp -o StrictHostKeyChecking=no -r build/* ${SSH_USER}@${SSH_HOST}:${BACKUP_FOLDER}"
              } catch (e) {
                sh 'echo "Pre Deployment failed: $(e.message)"'
              }
            
          
        }
      }
    }
    
    stage('Deploy') {
      steps {
       
            script {
              try {
                sh 'echo "Deployment started"'
                sh "scp -o StrictHostKeyChecking=no -r build/* ${SSH_USER}@${SSH_HOST}:${DESTINATION_FOLDER1}"
                sh "scp -o StrictHostKeyChecking=no -r build/* ${SSH_USER}@${SSH_HOST}:${DESTINATION_FOLDER2}"
              } catch (e) {
                sh 'echo "Build failed: $(e.message)"'
                sh 'echo "Rollback started"'
                sh "mv ${BACKUP_FOLDER} ${ROLLBACK_FOLDER} && mv ${ROLLBACK_FOLDER} ${DESTINATION_FOLDER1}"
          }
        }
      }
    }
  }
  
  post {
    failure {
      sh 'echo failure'
    }
    success {
      sh 'echo success'
    }
  }
}
