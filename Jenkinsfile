String cron_string = BRANCH_NAME == "master" ? "H/30 * * * *" : ""

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
            image 'python:3.7.2-onbuild'
        }
    }

    stages {
        stage('Run') {
            steps {
                script {
                    sh '''
                    virtualenv venv --distribute
                    . venv/bin/activate && pip3 install -r requirements.txt >/dev/null 2>&1
                    python3 main.py
                    '''
                }
            }
        }
    }
}