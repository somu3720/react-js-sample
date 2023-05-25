pipeline{
  agent any
  
 environment{
    SSH_USER = "deployserver"//"deploy_jenkins"
    SSH_HOST = "20.127.193.201"//"40.76.244.235"
    //SSH_KNOWN_HOSTS = ""
    DESTINATION_FOLDER = "/var/www/html"
    BACKUP_FOLDER = "backup"
    ROLLBACK_FOLDER = "rollback"
    
    SONAR_PROJECT_KEY = "ri_frontend"
    SONAR_HOST = "https://sonarqube.mydrreddys.com"
    SONAR_KEY = "91f262086d32d33838c731a39683712c6343d056"
  } 
  
  stages{
    stage('Build'){
      steps{
        script{
          try{
            sh 'echo "Build started"'
            sh 'npm run build'
            sh 'echo "Build Ended"'
            }catch(e){
              sh 'echo "Build failed: $(e.message)"'
            }
        }
      }
    }
    //stage('Sonar Analysis'){
      //steps{
        //script{
          //try{
            //withSonarQubeEnv('SonarQube'){
              //sh 'sonar-scanner Dsonar.projectkey=${SONAR_PROJECT_KEY} Dsonar.sources=. Dsonar.host.url=${SONAR_HOST_URL} Dsonar.login=${SONAR_KEY}'
            //}
            //timeout(time: 1, unit: 'Hours'){
              //waitforquQualityGate abortPipeline: true
            //}
            //}catch(e){
              //sh 'echo "Build failed: $(e.message)"'
            //}
        //}
      //}
    //}
    
    /*
    stage('dependencyTrackPublisher') {
            steps {
                withCredentials([string(credentialsId: '506ed685-4e2b-4d31-a44f-8ba8e67b6341', variable: 'API_KEY')]) {
                    dependencyTrackPublisher artifact: 'target/bom.xml', projectName: 'my-project', projectVersion: 'my-version', synchronous: true, dependencyTrackApiKey: API_KEY, projectProperties: [tags: ['tag1', 'tag2'], swidTagId: 'my swid tag', group: 'my group', parentId: 'parent-uuid']
                }
            }  */
    
    
    stage('Pre Deploy'){
      steps{
        script{
          try{
            //sh "tar -czvf build_$BUILD_NUMBER.tar.gz *"
            sh 'echo "Ssh Login started"'
            sh "ssh '${SSH_USER}@${SSH_HOST}'"
            sh 'service nginx status'
            sh "scp -o StrictHostKeyChecking=no -r build/* ${SSH_USER}@${SSH_HOST}:${BACKUP_FOLDER}"
            //sh "rm -rf *tar.gz"
            }catch(e){
              sh 'echo "Pre Deployment failed: $(e.message)"'
            }
        }
      }
    }
    stage('Deploy'){
      steps{
        script{
          try{
            sh 'echo "Deployment started"'
            
            
            //sh 'mkdir ${BACKUP_FOLDER}'
            
            
            sh "scp -o StrictHostKeyChecking=no -r build/* ${SSH_USER}@${SSH_HOST}:${DESTINATION_FOLDER}"
            
            }catch(e){
              sh 'echo "Build failed: $(e.message)"'
              sh 'echo "Rollback started"'
              sh "mv ${BACKUP_FOLDER} ${ROLLBACK_FOLDER} && mv ${ROLLBACK_FOLDER} ${DESTINATION_FOLDER}"
            }
        }
      }
    }
  }
  post{
      failure{
        sh 'echo failure'
      }
      success{
        sh 'echo success'
      }
    }
}
