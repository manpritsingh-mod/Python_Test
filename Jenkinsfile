pipeline {
    agent any

    options {
        skipDefaultCheckout(true)
    }

    parameters {
        booleanParam(
            name: 'SIMULATE_FAILURE',
            defaultValue: true,
            description: 'Create a temporary failing pytest test to validate Jenkins -> webhook -> healing-engine'
        )
    }

    environment {
        REPO_URL = 'https://github.com/manpritsingh-mod/Python_Test.git'
        REPO_BRANCH = 'master'
        HEALING_WEBHOOK_URL = 'http://healing-engine:5000/webhook/jenkins'
        PYTEST_LOG = 'pytest-output.log'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: "${env.REPO_BRANCH}", url: "${env.REPO_URL}"
            }
        }

        stage('Setup Python') {
            steps {
                sh '''
                    python3 --version
                    python3 -m venv .venv
                    . .venv/bin/activate
                    python -m pip install --upgrade pip setuptools wheel
                    if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
                    if [ -f requirements-dev.txt ]; then pip install -r requirements-dev.txt; fi
                    pip install -e .
                '''
            }
        }

        stage('Inject Failure Scenario') {
            when {
                expression { return params.SIMULATE_FAILURE }
            }
            steps {
                writeFile file: 'tests/test_ci_failure_webhook.py', text: '''
def test_intentional_webhook_failure():
    assert 2 + 2 == 5, "Intentional CI failure to validate Jenkins -> webhook -> healing-engine"
'''.stripIndent()
            }
        }

        stage('Unit Tests') {
            steps {
                sh '''
                    . .venv/bin/activate
                    set +e
                    python -m pytest tests > "$PYTEST_LOG" 2>&1
                    status=$?
                    cat "$PYTEST_LOG"
                    exit $status
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'pytest-output.log', allowEmptyArchive: true
        }

        failure {
            script {
                def logText = fileExists(env.PYTEST_LOG) ? readFile(env.PYTEST_LOG) : "pytest log not found"

                def payload = groovy.json.JsonOutput.toJson([
                    name: env.JOB_NAME,
                    url: env.BUILD_URL,
                    build: [
                        number: env.BUILD_NUMBER as Integer,
                        status: currentBuild.currentResult ?: 'FAILURE',
                        url: env.BUILD_URL,
                        log: logText.take(20000)
                    ]
                ])

                writeFile file: 'jenkins-webhook-payload.json', text: payload

                sh '''
                    curl -sS -X POST "$HEALING_WEBHOOK_URL" \
                      -H "Content-Type: application/json" \
                      --data @jenkins-webhook-payload.json
                '''
            }
        }
    }
}
