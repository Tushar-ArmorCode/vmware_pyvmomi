from typing import List
from enum import Enum
from pyVmomi import vim, vmodl
from datetime import datetime
from pyVmomi.VmomiSupport import ManagedObject, NoneType, PropertyPath, binary, byte


class HostProfile(vim.profile.Profile):
    @property
    def validationState(self) -> str: ...
    @property
    def validationStateUpdateTime(self) -> datetime: ...
    @property
    def validationFailureInfo(self) -> HostProfile.ValidationFailureInfo: ...
    @property
    def complianceCheckTime(self) -> datetime: ...
    @property
    def referenceHost(self) -> vim.HostSystem: ...
    def ResetValidationState(self) -> NoneType: ...
    def UpdateReferenceHost(self, host: vim.HostSystem) -> NoneType: ...
    def Update(self, config: HostProfile.ConfigSpec) -> NoneType: ...
    def Execute(self, host: vim.HostSystem, deferredParam: List[vim.profile.DeferredPolicyOptionParameter]) -> ExecuteResult: ...


    class CompleteConfigSpec(HostProfile.ConfigSpec):
        @property
        def applyProfile(self) -> HostApplyProfile: ...
        @property
        def customComplyProfile(self) -> vim.profile.ComplianceProfile: ...
        @property
        def disabledExpressionListChanged(self) -> bool: ...
        @property
        def disabledExpressionList(self) -> List[str]: ...
        @property
        def validatorHost(self) -> vim.HostSystem: ...
        @property
        def validating(self) -> bool: ...
        @property
        def hostConfig(self) -> HostProfile.ConfigInfo: ...


    class ConfigInfo(vim.profile.Profile.ConfigInfo):
        @property
        def applyProfile(self) -> HostApplyProfile: ...
        @property
        def defaultComplyProfile(self) -> vim.profile.ComplianceProfile: ...
        @property
        def defaultComplyLocator(self) -> List[vim.profile.ComplianceLocator]: ...
        @property
        def customComplyProfile(self) -> vim.profile.ComplianceProfile: ...
        @property
        def disabledExpressionList(self) -> List[str]: ...
        @property
        def description(self) -> vim.profile.Profile.Description: ...


    class ConfigSpec(vim.profile.Profile.CreateSpec): ...


    class HostBasedConfigSpec(HostProfile.ConfigSpec):
        @property
        def host(self) -> vim.HostSystem: ...
        @property
        def useHostProfileEngine(self) -> bool: ...


    class SerializedHostProfileSpec(vim.profile.Profile.SerializedCreateSpec):
        @property
        def validatorHost(self) -> vim.HostSystem: ...
        @property
        def validating(self) -> bool: ...


    class ValidationFailureInfo(vmodl.DynamicData):
        @property
        def name(self) -> str: ...
        @property
        def annotation(self) -> str: ...
        @property
        def updateType(self) -> str: ...
        @property
        def host(self) -> vim.HostSystem: ...
        @property
        def applyProfile(self) -> HostApplyProfile: ...
        @property
        def failures(self) -> List[vim.fault.ProfileUpdateFailed.UpdateFailure]: ...
        @property
        def faults(self) -> List[vmodl.MethodFault]: ...


        class UpdateType(Enum):
            HostBased = "HostBased"
            Import = "Import"
            Edit = "Edit"
            Compose = "Compose"


    class ValidationState(Enum):
        Ready = "Ready"
        Running = "Running"
        Failed = "Failed"


class HostSpecificationManager(ManagedObject):
    def UpdateHostSpecification(self, host: vim.HostSystem, hostSpec: HostSpecification) -> NoneType: ...
    def UpdateHostSubSpecification(self, host: vim.HostSystem, hostSubSpec: HostSubSpecification) -> NoneType: ...
    def RetrieveHostSpecification(self, host: vim.HostSystem, fromHost: bool) -> HostSpecification: ...
    def DeleteHostSubSpecification(self, host: vim.HostSystem, subSpecName: str) -> NoneType: ...
    def DeleteHostSpecification(self, host: vim.HostSystem) -> NoneType: ...
    def GetUpdatedHosts(self, startChangeID: str, endChangeID: str) -> List[vim.HostSystem]: ...


class ProfileManager(vim.profile.ProfileManager):
    def ApplyHostConfiguration(self, host: vim.HostSystem, configSpec: ConfigSpec, userInput: List[vim.profile.DeferredPolicyOptionParameter]) -> vim.Task: ...
    def GenerateConfigTaskList(self, configSpec: ConfigSpec, host: vim.HostSystem) -> ProfileManager.ConfigTaskList: ...
    def GenerateTaskList(self, configSpec: ConfigSpec, host: vim.HostSystem) -> vim.Task: ...
    def QueryProfileMetadata(self, profileName: List[type], profile: vim.profile.Profile) -> List[vim.profile.ProfileMetadata]: ...
    def QueryProfileStructure(self, profile: vim.profile.Profile) -> vim.profile.ProfileStructure: ...
    def CreateDefaultProfile(self, profileType: type, profileTypeName: str, profile: vim.profile.Profile) -> vim.profile.ApplyProfile: ...
    def UpdateAnswerFile(self, host: vim.HostSystem, configSpec: ProfileManager.AnswerFileCreateSpec) -> vim.Task: ...
    def RetrieveAnswerFile(self, host: vim.HostSystem) -> AnswerFile: ...
    def RetrieveAnswerFileForProfile(self, host: vim.HostSystem, applyProfile: HostApplyProfile) -> AnswerFile: ...
    def ExportAnswerFile(self, host: vim.HostSystem) -> vim.Task: ...
    def CheckAnswerFileStatus(self, host: List[vim.HostSystem]) -> vim.Task: ...
    def QueryAnswerFileStatus(self, host: List[vim.HostSystem]) -> List[AnswerFileStatusResult]: ...
    def UpdateHostCustomizations(self, hostToConfigSpecMap: List[ProfileManager.HostToConfigSpecMap]) -> vim.Task: ...
    def RetrieveHostCustomizations(self, hosts: List[vim.HostSystem]) -> List[ProfileManager.StructuredCustomizations]: ...
    def RetrieveHostCustomizationsForProfile(self, hosts: List[vim.HostSystem], applyProfile: HostApplyProfile) -> List[ProfileManager.StructuredCustomizations]: ...
    def GenerateHostConfigTaskSpec(self, hostsInfo: List[ProfileManager.StructuredCustomizations]) -> vim.Task: ...
    def ApplyEntitiesConfiguration(self, applyConfigSpecs: List[ProfileManager.ApplyHostConfigSpec]) -> vim.Task: ...
    def ValidateComposition(self, source: vim.profile.Profile, targets: List[vim.profile.Profile], toBeMerged: HostApplyProfile, toReplaceWith: HostApplyProfile, toBeDeleted: HostApplyProfile, enableStatusToBeCopied: HostApplyProfile, errorOnly: bool) -> vim.Task: ...
    def CompositeProfile(self, source: vim.profile.Profile, targets: List[vim.profile.Profile], toBeMerged: HostApplyProfile, toBeReplacedWith: HostApplyProfile, toBeDeleted: HostApplyProfile, enableStatusToBeCopied: HostApplyProfile) -> vim.Task: ...


    class AnswerFileCreateSpec(vmodl.DynamicData):
        @property
        def validating(self) -> bool: ...


    class AnswerFileOptionsCreateSpec(ProfileManager.AnswerFileCreateSpec):
        @property
        def userInput(self) -> List[vim.profile.DeferredPolicyOptionParameter]: ...


    class AnswerFileSerializedCreateSpec(ProfileManager.AnswerFileCreateSpec):
        @property
        def answerFileConfigString(self) -> str: ...


    class ApplyHostConfigResult(vmodl.DynamicData):
        @property
        def startTime(self) -> datetime: ...
        @property
        def completeTime(self) -> datetime: ...
        @property
        def host(self) -> vim.HostSystem: ...
        @property
        def status(self) -> str: ...
        @property
        def errors(self) -> List[vmodl.MethodFault]: ...


    class ApplyHostConfigSpec(ExecuteResult):
        @property
        def host(self) -> vim.HostSystem: ...
        @property
        def taskListRequirement(self) -> List[str]: ...
        @property
        def taskDescription(self) -> List[vmodl.LocalizableMessage]: ...
        @property
        def rebootStateless(self) -> bool: ...
        @property
        def rebootHost(self) -> bool: ...
        @property
        def faultData(self) -> vmodl.MethodFault: ...


    class CompositionResult(vmodl.DynamicData):
        @property
        def errors(self) -> List[vmodl.LocalizableMessage]: ...
        @property
        def results(self) -> List[ProfileManager.CompositionResult.ResultElement]: ...


        class ResultElement(vmodl.DynamicData):
            @property
            def target(self) -> vim.profile.Profile: ...
            @property
            def status(self) -> str: ...
            @property
            def errors(self) -> List[vmodl.LocalizableMessage]: ...


    class CompositionValidationResult(vmodl.DynamicData):
        @property
        def results(self) -> List[ProfileManager.CompositionValidationResult.ResultElement]: ...
        @property
        def errors(self) -> List[vmodl.LocalizableMessage]: ...


        class ResultElement(vmodl.DynamicData):
            @property
            def target(self) -> vim.profile.Profile: ...
            @property
            def status(self) -> str: ...
            @property
            def errors(self) -> List[vmodl.LocalizableMessage]: ...
            @property
            def sourceDiffForToBeMerged(self) -> HostApplyProfile: ...
            @property
            def targetDiffForToBeMerged(self) -> HostApplyProfile: ...
            @property
            def toBeAdded(self) -> HostApplyProfile: ...
            @property
            def toBeDeleted(self) -> HostApplyProfile: ...
            @property
            def toBeDisabled(self) -> HostApplyProfile: ...
            @property
            def toBeEnabled(self) -> HostApplyProfile: ...
            @property
            def toBeReenableCC(self) -> HostApplyProfile: ...


    class ConfigTaskList(vmodl.DynamicData):
        @property
        def configSpec(self) -> ConfigSpec: ...
        @property
        def taskDescription(self) -> List[vmodl.LocalizableMessage]: ...
        @property
        def taskListRequirement(self) -> List[str]: ...


    class EntityCustomizations(vmodl.DynamicData): ...


    class HostToConfigSpecMap(vmodl.DynamicData):
        @property
        def host(self) -> vim.HostSystem: ...
        @property
        def configSpec(self) -> ProfileManager.AnswerFileCreateSpec: ...


    class StructuredCustomizations(ProfileManager.EntityCustomizations):
        @property
        def entity(self) -> vim.ManagedEntity: ...
        @property
        def customizations(self) -> AnswerFile: ...


    class AnswerFileStatus(Enum):
        valid = "valid"
        invalid = "invalid"
        unknown = "unknown"


    class TaskListRequirement(Enum):
        maintenanceModeRequired = "maintenanceModeRequired"
        rebootRequired = "rebootRequired"


class ActiveDirectoryProfile(vim.profile.ApplyProfile): ...


class AnswerFile(vmodl.DynamicData):
    @property
    def userInput(self) -> List[vim.profile.DeferredPolicyOptionParameter]: ...
    @property
    def createdTime(self) -> datetime: ...
    @property
    def modifiedTime(self) -> datetime: ...


class AnswerFileStatusResult(vmodl.DynamicData):
    @property
    def checkedTime(self) -> datetime: ...
    @property
    def host(self) -> vim.HostSystem: ...
    @property
    def status(self) -> str: ...
    @property
    def error(self) -> List[AnswerFileStatusResult.AnswerFileStatusError]: ...


    class AnswerFileStatusError(vmodl.DynamicData):
        @property
        def userInputPath(self) -> vim.profile.ProfilePropertyPath: ...
        @property
        def errMsg(self) -> vmodl.LocalizableMessage: ...


class AuthenticationProfile(vim.profile.ApplyProfile):
    @property
    def activeDirectory(self) -> ActiveDirectoryProfile: ...


class DateTimeProfile(vim.profile.ApplyProfile): ...


class DvsHostVNicProfile(DvsVNicProfile): ...


class DvsProfile(vim.profile.ApplyProfile):
    @property
    def key(self) -> str: ...
    @property
    def name(self) -> str: ...
    @property
    def uplink(self) -> List[PnicUplinkProfile]: ...


class DvsServiceConsoleVNicProfile(DvsVNicProfile): ...


class DvsVNicProfile(vim.profile.ApplyProfile):
    @property
    def key(self) -> str: ...
    @property
    def ipConfig(self) -> IpAddressProfile: ...


class ExecuteResult(vmodl.DynamicData):
    @property
    def status(self) -> str: ...
    @property
    def configSpec(self) -> ConfigSpec: ...
    @property
    def inapplicablePath(self) -> List[PropertyPath]: ...
    @property
    def requireInput(self) -> List[vim.profile.DeferredPolicyOptionParameter]: ...
    @property
    def error(self) -> List[ExecuteResult.ExecuteError]: ...


    class ExecuteError(vmodl.DynamicData):
        @property
        def path(self) -> vim.profile.ProfilePropertyPath: ...
        @property
        def message(self) -> vmodl.LocalizableMessage: ...


    class Status(Enum):
        success = "success"
        needInput = "needInput"
        error = "error"


class FirewallProfile(vim.profile.ApplyProfile):
    @property
    def ruleset(self) -> List[FirewallProfile.RulesetProfile]: ...


    class RulesetProfile(vim.profile.ApplyProfile):
        @property
        def key(self) -> str: ...


class HostApplyProfile(vim.profile.ApplyProfile):
    @property
    def memory(self) -> HostMemoryProfile: ...
    @property
    def storage(self) -> StorageProfile: ...
    @property
    def network(self) -> NetworkProfile: ...
    @property
    def datetime(self) -> DateTimeProfile: ...
    @property
    def firewall(self) -> FirewallProfile: ...
    @property
    def security(self) -> SecurityProfile: ...
    @property
    def service(self) -> List[ServiceProfile]: ...
    @property
    def option(self) -> List[OptionProfile]: ...
    @property
    def userAccount(self) -> List[UserProfile]: ...
    @property
    def usergroupAccount(self) -> List[UserGroupProfile]: ...
    @property
    def authentication(self) -> AuthenticationProfile: ...


class HostMemoryProfile(vim.profile.ApplyProfile): ...


class HostPortGroupProfile(PortGroupProfile):
    @property
    def ipConfig(self) -> IpAddressProfile: ...


class HostSpecification(vmodl.DynamicData):
    @property
    def createdTime(self) -> datetime: ...
    @property
    def lastModified(self) -> datetime: ...
    @property
    def host(self) -> vim.HostSystem: ...
    @property
    def subSpecs(self) -> List[HostSubSpecification]: ...
    @property
    def changeID(self) -> str: ...


class HostSubSpecification(vmodl.DynamicData):
    @property
    def name(self) -> str: ...
    @property
    def createdTime(self) -> datetime: ...
    @property
    def data(self) -> List[byte]: ...
    @property
    def binaryData(self) -> binary: ...


class IpAddressProfile(vim.profile.ApplyProfile): ...


class IpRouteProfile(vim.profile.ApplyProfile):
    @property
    def staticRoute(self) -> List[StaticRouteProfile]: ...


class NasStorageProfile(vim.profile.ApplyProfile):
    @property
    def key(self) -> str: ...


class NetStackInstanceProfile(vim.profile.ApplyProfile):
    @property
    def key(self) -> str: ...
    @property
    def dnsConfig(self) -> NetworkProfile.DnsConfigProfile: ...
    @property
    def ipRouteConfig(self) -> IpRouteProfile: ...


class NetworkPolicyProfile(vim.profile.ApplyProfile): ...


class NetworkProfile(vim.profile.ApplyProfile):
    @property
    def vswitch(self) -> List[VirtualSwitchProfile]: ...
    @property
    def vmPortGroup(self) -> List[VmPortGroupProfile]: ...
    @property
    def hostPortGroup(self) -> List[HostPortGroupProfile]: ...
    @property
    def serviceConsolePortGroup(self) -> List[ServiceConsolePortGroupProfile]: ...
    @property
    def dnsConfig(self) -> NetworkProfile.DnsConfigProfile: ...
    @property
    def ipRouteConfig(self) -> IpRouteProfile: ...
    @property
    def consoleIpRouteConfig(self) -> IpRouteProfile: ...
    @property
    def pnic(self) -> List[PhysicalNicProfile]: ...
    @property
    def dvswitch(self) -> List[DvsProfile]: ...
    @property
    def dvsServiceConsoleNic(self) -> List[DvsServiceConsoleVNicProfile]: ...
    @property
    def dvsHostNic(self) -> List[DvsHostVNicProfile]: ...
    @property
    def nsxHostNic(self) -> List[NsxHostVNicProfile]: ...
    @property
    def netStackInstance(self) -> List[NetStackInstanceProfile]: ...
    @property
    def opaqueSwitch(self) -> OpaqueSwitchProfile: ...


    class DnsConfigProfile(vim.profile.ApplyProfile): ...


class NsxHostVNicProfile(vim.profile.ApplyProfile):
    @property
    def key(self) -> str: ...
    @property
    def ipConfig(self) -> IpAddressProfile: ...


class OpaqueSwitchProfile(vim.profile.ApplyProfile): ...


class OptionProfile(vim.profile.ApplyProfile):
    @property
    def key(self) -> str: ...


class PermissionProfile(vim.profile.ApplyProfile):
    @property
    def key(self) -> str: ...


class PhysicalNicProfile(vim.profile.ApplyProfile):
    @property
    def key(self) -> str: ...


class PnicUplinkProfile(vim.profile.ApplyProfile):
    @property
    def key(self) -> str: ...


class PortGroupProfile(vim.profile.ApplyProfile):
    @property
    def key(self) -> str: ...
    @property
    def name(self) -> str: ...
    @property
    def vlan(self) -> PortGroupProfile.VlanProfile: ...
    @property
    def vswitch(self) -> PortGroupProfile.VirtualSwitchSelectionProfile: ...
    @property
    def networkPolicy(self) -> NetworkPolicyProfile: ...


    class VirtualSwitchSelectionProfile(vim.profile.ApplyProfile): ...


    class VlanProfile(vim.profile.ApplyProfile): ...


class SecurityProfile(vim.profile.ApplyProfile):
    @property
    def permission(self) -> List[PermissionProfile]: ...


class ServiceConsolePortGroupProfile(PortGroupProfile):
    @property
    def ipConfig(self) -> IpAddressProfile: ...


class ServiceProfile(vim.profile.ApplyProfile):
    @property
    def key(self) -> str: ...


class StaticRouteProfile(vim.profile.ApplyProfile):
    @property
    def key(self) -> str: ...


class StorageProfile(vim.profile.ApplyProfile):
    @property
    def nasStorage(self) -> List[NasStorageProfile]: ...


class UserGroupProfile(vim.profile.ApplyProfile):
    @property
    def key(self) -> str: ...


class UserProfile(vim.profile.ApplyProfile):
    @property
    def key(self) -> str: ...


class VirtualSwitchProfile(vim.profile.ApplyProfile):
    @property
    def key(self) -> str: ...
    @property
    def name(self) -> str: ...
    @property
    def link(self) -> VirtualSwitchProfile.LinkProfile: ...
    @property
    def numPorts(self) -> VirtualSwitchProfile.NumPortsProfile: ...
    @property
    def networkPolicy(self) -> NetworkPolicyProfile: ...


    class LinkProfile(vim.profile.ApplyProfile): ...


    class NumPortsProfile(vim.profile.ApplyProfile): ...


class VmPortGroupProfile(PortGroupProfile): ...