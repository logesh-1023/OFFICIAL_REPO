pipeline {
    agent any
    
    environment {
        GIT_CREDENTIALS_ID = 'logesh-1023'
        EC2_SSH_CREDENTIALS = 'dc907b5c-9b90-4d6e-af60-49d2645e6f4b'
        EC2_SERVER_IP = '18.208.113.159'
        REPO_PATH = '/home/ec2-user/SLACKAPP/SERVER'
        GIT_BRANCH = 'TEST_MASTER'
    }
    
    stages {
        stage('Check Webhook') {
            steps {
                echo 'Webhook is working!'
            }
        }
        
        stage('Pull Repo on EC2') {
            steps {
                script {
                    withCredentials([sshUserPrivateKey(credentialsId: "${EC2_SSH_CREDENTIALS}", keyFileVariable: 'SSH_KEY')]) {
                        sh """
                            chmod 400 ${SSH_KEY}
                            ssh -o StrictHostKeyChecking=no -i ${SSH_KEY} ec2-user@${EC2_SERVER_IP} << 'EOF'
                                cd ${REPO_PATH}
                                if [ ! -d ".git" ]; then
                                    echo "Git repository not found! Initializing..."
                                    git init
                                    git remote add origin https://github.com/logesh-1023/OFFICIAL_REPO.git
                                fi
                                git reset --hard
                                git clean -fd
                                git fetch origin
                                git checkout ${GIT_BRANCH}
                                git pull origin ${GIT_BRANCH}
                            EOF
                        """
                    }
                }
            }
        }
        
        stage('Run Python App on EC2') {
            steps {
                script {
                    withCredentials([sshUserPrivateKey(credentialsId: "${EC2_SSH_CREDENTIALS}", keyFileVariable: 'SSH_KEY')]) {
                        sh """
                            chmod 400 ${SSH_KEY}
                            ssh -o StrictHostKeyChecking=no -i ${SSH_KEY} ec2-user@${EC2_SERVER_IP} << 'EOF'
                                cd /etc/systemd/system
                                sudo systemctl restart flask_server.service
                            EOF
                        """
                    }
                }
            }
        }
    }
}
