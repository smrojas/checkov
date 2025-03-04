from __future__ import annotations

from typing import Any

from checkov.bicep.checks.resource.base_resource_check import BaseResourceCheck
from checkov.common.models.enums import CheckResult, CheckCategories


class StorageAccountAzureServicesAccessEnabled(BaseResourceCheck):
    def __init__(self) -> None:
        name = "Ensure 'Trusted Microsoft Services' is enabled for Storage Account access"
        id = "CKV_AZURE_36"
        supported_resources = ("Microsoft.Storage/storageAccounts",)
        categories = (CheckCategories.NETWORKING,)
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf: dict[str, Any]) -> CheckResult:
        properties = conf.get("properties")
        if properties:
            nacls = properties.get("networkAcls")
            if nacls:
                default_action = nacls.get("defaultAction")
                if default_action == "Deny":
                    bypass = nacls.get("bypass")
                    if not bypass or bypass == "None":
                        return CheckResult.FAILED

        return CheckResult.PASSED


check = StorageAccountAzureServicesAccessEnabled()
