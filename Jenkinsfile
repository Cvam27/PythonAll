@Library('tenable.common')
import com.tenable.jenkins.*
import com.tenable.jenkins.builds.*
import com.tenable.jenkins.common.*
import com.tenable.jenkins.builds.git.*

// Set branch properties: keep max 10 builds and add boolean parameter to force unit tests to Jenkins UI build options
def projectProperties = [
        [$class: 'BuildDiscarderProperty', strategy: [$class: 'LogRotator',
                                                      numToKeepStr: '10']],
        [$class: 'ParametersDefinitionProperty', parameterDefinitions: [
                [$class: 'BooleanParameterDefinition', description: 'Force unit test run',
                 defaultValue: false, name: 'FORCE_UNIT_TESTS']]
        ]
]
properties(projectProperties)

// Class instances
Common common = new Common(this)
BuildParams baseParams = new BuildParams(this)

String dockerNode = Constants.DOCKERNODE
currentBuild.displayName += " @ ${dockerNode}"

List priorityClassifications = [
    common.isPullRequest(),
    env.BRANCH_NAME in ['master', 'develop'],
    env.BRANCH_NAME.toLowerCase().startsWith('release'),
    params.FORCE_UNIT_TESTS
]
Boolean priority = priorityClassifications.any{it}
String slackChannel = priority? '#nessus_catium_builds' : '#automation-notify'

// Configuration
// Base parameters, common for all builds
baseParams.retryCount = 1
baseParams.channels = slackChannel

parallel (
    "Lexical Tests": {
        stage("Lexical Tests") {
            AutomationDirectBuild autoBuilder = new AutomationDirectBuild(this)
            common.copyProperties(baseParams, autoBuilder.parameters)
            autoBuilder.parameters.pytestOptions = '--reruns=0'
            autoBuilder.parameters.pytestTestPaths = ['build_checks/test_nessus_module.py']
            autoBuilder.execute()
        }
    },

    "File Package and Code Validity Checks": {
        stage("File Package and Code Validity Checks") {
            // PyLint check must be done for the branch itself; merged result would not yield needed changes to analyze
            common.conditionalStage(priority) {
                AutomationDirectBuild autoBuilder = new AutomationDirectBuild(this)
                common.copyProperties(baseParams, autoBuilder.parameters)
                autoBuilder.parameters.pytestTestPaths = ['build_checks/test_file_validity.py']
                autoBuilder.parameters.pytestOptions = '-n1 --reruns=0'
                autoBuilder.execute()
            }
        }
    }
)

Logger.getLogger(this, GitFunctions.class).setLevel(Constants.LOG_LEVEL_DEBUG)

BuildParams bparams = new BuildParams(this, 459)
bparams.setPythonLibraryDefaults()
bparams.versionFile = 'nessus/__init__.py'  // File containing __version__ = 'x.y.z' line
bparams.container = Constants.DOCKER_CI_PYTEST_BASE
bparams.channels = slackChannel
bparams.test = false

currentBuild.result = currentBuild.result ?: Constants.JSUCCESS
if (currentBuild.result == Constants.JSUCCESS) {
    libraryBuildPipeline(bparams, [buildType: 'pythonlib'])
}
