from unittest import skip

from tests.integration.unit_test.unit_test_base import UnitTestBase


class UnitTest_java11_cookiecutter_aws_sam_hello_java_gradle(UnitTestBase.JavaUnitTestGradleBase):
    directory = "java11/hello-gradle"
    code_directories = ["HelloWorldFunction"]


class UnitTest_java11_cookiecutter_aws_sam_hello_java_maven(UnitTestBase.JavaUnitTestMavenBase):
    directory = "java11/hello-maven"
    code_directories = ["HelloWorldFunction"]

class UnitTest_java11_cookiecutter_aws_sam_hello_java_powertools_maven(UnitTestBase.JavaUnitTestMavenBase):
    directory = "java11/hello-pt-maven"
    code_directories = ["HelloWorldFunction"]


class UnitTest_java11_cookiecutter_aws_sam_eventbridge_hello_java_gradle(UnitTestBase.JavaUnitTestGradleBase):
    directory = "java11/event-bridge-gradle"
    code_directories = ["HelloWorldFunction"]


class UnitTest_java11_cookiecutter_aws_sam_eventbridge_hello_java_maven(UnitTestBase.JavaUnitTestMavenBase):
    directory = "java11/event-bridge-maven"
    code_directories = ["HelloWorldFunction"]


@skip("eventbridge schema app requires credential to pull missing files, skip")
class UnitTest_java11_cookiecutter_aws_sam_eventbridge_schema_app_java_gradle(UnitTestBase.JavaUnitTestGradleBase):
    directory = "java11/event-bridge-schema-gradle"
    code_directories = ["HelloWorldFunction"]


@skip("eventbridge schema app requires credential to pull missing files, skip")
class UnitTest_java11_cookiecutter_aws_sam_eventbridge_schema_app_java_maven(UnitTestBase.JavaUnitTestMavenBase):
    directory = "java11/event-bridge-schema-maven"
    code_directories = ["HelloWorldFunction"]


class UnitTest_java11_cookiecutter_aws_sam_step_functions_sample_app_gradle(UnitTestBase.JavaUnitTestGradleBase):
    directory = "java11/step-func-gradle"
    code_directories = [
        "functions/StockBuyer",
        "functions/StockChecker",
        "functions/StockSeller",
    ]


class UnitTest_java11_cookiecutter_aws_sam_step_functions_sample_app_maven(UnitTestBase.JavaUnitTestMavenBase):
    directory = "java11/step-func-maven"
    code_directories = [
        "functions/StockBuyer",
        "functions/StockChecker",
        "functions/StockSeller",
    ]