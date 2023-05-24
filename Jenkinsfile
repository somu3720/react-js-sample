pipeline {
  agent any
  environment {
    SSH_USER = "deploy_jenkins"
    SSH_HOST = "40.76.244.235"
 //   CURRENT_DATE = new Date().format("yyyy-MM-dd_HH-mm-ss")
    DESTINATION_FOLDER = "/var/www/example.com/html"
    BACKUP_FOLDER = "backup_RI/"
    ROLLBACK_FOLDER = "rollback_RI/"
  }
  
  stages {
    stage('Build') {
      steps {
        retry(3) {
          timeout(time: 1, unit: 'HOURS') {
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
      }
    }
    
    stage('Pre Deploy') {
      steps {
        retry(3) {
          timeout(time: 30, unit: 'MINUTES') {
            script {
              try {
                sh 'echo "Ssh Login started"'
                sh "ssh '${SSH_USER}@${SSH_HOST}'"
                sh "sudo mkdir -p ${BACKUP_FOLDER}"
                sh "sudo mkdir -p ${DESTINATION_FOLDER}"
                sh "sudo mkdir -p ${ROLLBACK_FOLDER}"
                sh "scp -o StrictHostKeyChecking=no -r build/* ${SSH_USER}@${SSH_HOST}:${BACKUP_FOLDER}"
              } catch (e) {
                sh 'echo "Pre Deployment failed: $(e.message)"'
              }
            }
          }
        }
      }
    }
    
    stage('Deploy') {
      steps {
        retry(3) {
          timeout(time: 1, unit: 'HOURS') {
            script {
              try {
                sh 'echo "Deployment started"'
                sh "scp -o StrictHostKeyChecking=no -r build/* ${SSH_USER}@${SSH_HOST}:${DESTINATION_FOLDER}"
              } catch (e) {
                sh 'echo "Build failed: $(e.message)"'
                sh 'echo "Rollback started"'
                sh "mv ${BACKUP_FOLDER} ${ROLLBACK_FOLDER} && mv ${ROLLBACK_FOLDER} ${DESTINATION_FOLDER}"

              }
            }
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
