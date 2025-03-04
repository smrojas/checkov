from typing import Any
from checkov.common.models.consts import ANY_VALUE
from checkov.common.models.enums import CheckCategories, CheckResult
from checkov.terraform.checks.resource.base_resource_value_check import BaseResourceValueCheck


class LivenessProbe(BaseResourceValueCheck):

    def __init__(self):
        name = "Liveness Probe Should be Configured"
        id = "CKV_K8S_8"
        supported_resources = ["kubernetes_pod"]
        categories = [CheckCategories.GENERAL_SECURITY]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources,
                         missing_block_result=CheckResult.FAILED)

    def get_inspected_key(self) -> str:
        return "spec/[0]/container/[0]/liveness_probe/[0]"

    def scan_resource_conf(self, conf) -> CheckResult:
        spec = conf.get('spec')[0]
        if spec:
            containers = spec.get("container")
            for idx, container in enumerate(containers):
                if not isinstance(container, dict):
                    return CheckResult.UNKNOWN
                if container.get("liveness_probe"):
                    return CheckResult.PASSED
                self.evaluated_keys = [f'spec/[0]/container/[{idx}]']
                return CheckResult.FAILED

        return CheckResult.FAILED

    def get_expected_value(self) -> Any:
        return ANY_VALUE


check = LivenessProbe()
