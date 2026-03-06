// Jenkinsfile — PYTHON TEST FAILURE scenario
// Simulates: pytest assertion failure
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
                echo 'Fetching origin/main...'
                echo 'HEAD is now at 8b4d92a fix typo'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing python dependencies with pip...'
                echo 'Successfully installed pytest-8.1.1 requests-2.31.0'
            }
        }

        stage('Unit Tests') {
            steps {
                echo 'Running pytest...'
                echo '============================= test session starts =============================='
                echo 'platform linux -- Python 3.10.12, pytest-8.1.1, pluggy-1.4.0'
                echo 'rootdir: /workspace'
                echo 'collected 3 items'
                echo ''
                echo 'tests/test_calculator.py ..F                                             [100%]'
                echo ''
                echo '=================================== FAILURES ==================================='
                echo '_____________________________ test_divide_by_zero ______________________________'
                echo ''
                echo '    def test_divide_by_zero():'
                echo '>       assert divide(10, 0) == "Error"'
                echo 'E       ZeroDivisionError: division by zero'
                echo ''
                echo 'src/calculator.py:15: ZeroDivisionError'
                echo '=========================== short test summary info ============================'
                echo 'FAILED tests/test_calculator.py::test_divide_by_zero - ZeroDivisionError: division by zero'
                echo '========================= 1 failed, 2 passed in 0.15s =========================='
                echo '[ERROR] pytest failed with exit code 1'
                error('Unit tests failed: 1 failure')
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying to staging...'
            }
        }
    }

    post {
        failure {
            echo '❌ Tests failed! Triggering self-healing via webhook...'
            // In a real pipeline, we'd fire the webhook here.
        }
    }
}
