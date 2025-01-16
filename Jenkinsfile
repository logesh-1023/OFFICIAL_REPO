pipeline {
    agent any
    
environment {
    GIT_CREDENTIALS_ID = 'logesh-1023'
    EC2_SSH_CREDENTIALS = 'dc907b5c-9b90-4d6e-af60-49d2645e6f4b'
    EC2_SERVER_IP = '18.208.113.159'
    }
    stages {
        stage('Check Webhook') {
            steps {
                echo 'Webhook is working!'
            }
        }
        stage('Run Python App on EC2') {
            steps {
                script {
                    withCredentials([sshUserPrivateKey(credentialsId: "${EC2_SSH_CREDENTIALS}", keyFileVariable: 'SSH_KEY')]) {
                        sh '''
                            chmod 400 ${SSH_KEY}
                            ssh -o StrictHostKeyChecking=no -i ${SSH_KEY} ec2-user@${EC2_SERVER_IP} 'cd /etc/systemd/system && sudo systemctl restart flask_server.service'
                        '''
                    }
                }
             }
        }
    }
}
