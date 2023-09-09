pipeline {
    
    agent any
 /* environment{
        DOCKERHUB_USER = "mahmudulrm"
        APP_NAME = "gitops-argo-app"
        IMAGE_TAG = "${BUILD_NUMBER}"
        IMAGE_NAME = "${DOCKERHUB_USER}" + "/" + "${APP_NAME}"
        REGISTRY_CREDS = 'dockerhub'
        // add - manage jenkins > credentials > system > global credentials - add credentials
        // git hub access personal token
    }*/
    stages{
        stage('clean workspace'){
            steps{
                script{
                    cleanWs()
                }
            }
        }
    }




}