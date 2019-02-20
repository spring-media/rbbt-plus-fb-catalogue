String cron_string = BRANCH_NAME == "master" ? "H H/2 * * *" : ""

pipeline {
    agent { docker { reuseNode true; image 'python:2.7.15-onbuild' } }

    triggers {
        cron( cron_string )
    }

    options {
        buildDiscarder(logRotator(numToKeepStr: '25'))
        disableConcurrentBuilds()
    }

    stages {
        stage('Run') {
            steps {
                withCredentials([file(credentialsId: 'PRODUCT_CATALOGUE_CONFIG', variable: 'CONFIG')]) {
                    script {
                        sh '''
                            virtualenv venv --distribute
                            . venv/bin/activate && pip2 install -r requirements.txt >/dev/null 2>&1
                            python2.7 production.py
                        '''
                    }
                }
            }

            post {
                failure {
                    slackSend color: "danger", channel: "#up-status", message: ":facepalm: *Plus Facebook Catalogue* build failed! ${env.BUILD_URL}"
                }
            }
        }
    }
}