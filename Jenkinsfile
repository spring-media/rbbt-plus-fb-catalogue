String cron_string = BRANCH_NAME == "master" ? "H H/2 * * *" : ""

pipeline {
    triggers {
        cron( cron_string )
    }

    options {
        buildDiscarder(logRotator(numToKeepStr: '25'))
        disableConcurrentBuilds()
    }

    agent {
        docker {
            reuseNode true
            image 'python:2.7.15-onbuild'
        }
    }

    stages {
        stage('Run') {
            steps {
                script {
                    sh '''
                    virtualenv venv --distribute
                    . venv/bin/activate && pip2 install -r requirements.txt >/dev/null 2>&1
                    python2.7 main.py
                    '''
                }
            }
        }
    }
}