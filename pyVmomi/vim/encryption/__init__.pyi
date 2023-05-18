from typing import List
from enum import Enum
from pyVmomi import vim, vmodl
from datetime import datetime
from pyVmomi.VmomiSupport import ManagedObject, NoneType


class CryptoManager(ManagedObject):
    @property
    def enabled(self) -> bool: ...
    def AddKey(self, key: CryptoKeyPlain) -> NoneType: ...
    def AddKeys(self, keys: List[CryptoKeyPlain]) -> List[CryptoKeyResult]: ...
    def RemoveKey(self, key: CryptoKeyId, force: bool) -> NoneType: ...
    def RemoveKeys(self, keys: List[CryptoKeyId], force: bool) -> List[CryptoKeyResult]: ...
    def ListKeys(self, limit: int) -> List[CryptoKeyId]: ...


class CryptoManagerHost(CryptoManager):
    def Prepare(self) -> NoneType: ...
    def Enable(self, initialKey: CryptoKeyPlain) -> NoneType: ...
    def ChangeKey(self, newKey: CryptoKeyPlain) -> vim.Task: ...
    def Disable(self) -> NoneType: ...
    def GetCryptoKeyStatus(self, keys: List[CryptoKeyId]) -> List[CryptoManagerHost.KeyStatus]: ...


    class KeyStatus(vmodl.DynamicData):
        @property
        def keyId(self) -> CryptoKeyId: ...
        @property
        def present(self) -> bool: ...
        @property
        def managementType(self) -> str: ...


    class KeyManagementType(Enum):
        unknown = "unknown"
        internal = "internal"
        external = "external"


class CryptoManagerHostKMS(CryptoManagerHost): ...


class CryptoManagerKmip(CryptoManager):
    @property
    def kmipServers(self) -> List[KmipClusterInfo]: ...
    def RegisterKmipServer(self, server: KmipServerSpec) -> NoneType: ...
    def MarkDefault(self, clusterId: KeyProviderId) -> NoneType: ...
    def UpdateKmipServer(self, server: KmipServerSpec) -> NoneType: ...
    def RemoveKmipServer(self, clusterId: KeyProviderId, serverName: str) -> NoneType: ...
    def ListKmipServers(self, limit: int) -> List[KmipClusterInfo]: ...
    def RetrieveKmipServersStatus(self, clusters: List[KmipClusterInfo]) -> vim.Task: ...
    def GenerateKey(self, keyProvider: KeyProviderId, spec: CryptoManagerKmip.CustomAttributeSpec) -> CryptoKeyResult: ...
    def RetrieveKmipServerCert(self, keyProvider: KeyProviderId, server: KmipServerInfo) -> CryptoManagerKmip.ServerCertInfo: ...
    def UploadKmipServerCert(self, cluster: KeyProviderId, certificate: str) -> NoneType: ...
    def GenerateSelfSignedClientCert(self, cluster: KeyProviderId, request: CryptoManagerKmip.CertSignRequest) -> str: ...
    def GenerateClientCsr(self, cluster: KeyProviderId, request: CryptoManagerKmip.CertSignRequest) -> str: ...
    def RetrieveSelfSignedClientCert(self, cluster: KeyProviderId) -> str: ...
    def RetrieveClientCsr(self, cluster: KeyProviderId) -> str: ...
    def RetrieveClientCert(self, cluster: KeyProviderId) -> str: ...
    def UpdateSelfSignedClientCert(self, cluster: KeyProviderId, certificate: str) -> NoneType: ...
    def UpdateKmsSignedCsrClientCert(self, cluster: KeyProviderId, certificate: str) -> NoneType: ...
    def UploadClientCert(self, cluster: KeyProviderId, certificate: str, privateKey: str) -> NoneType: ...
    def IsKmsClusterActive(self, cluster: KeyProviderId) -> bool: ...
    def SetDefaultKmsCluster(self, entity: vim.ManagedEntity, clusterId: KeyProviderId) -> NoneType: ...
    def GetDefaultKmsCluster(self, entity: vim.ManagedEntity, defaultsToParent: bool) -> KeyProviderId: ...
    def QueryCryptoKeyStatus(self, keyIds: List[CryptoKeyId], checkKeyBitMap: int) -> List[CryptoManagerKmip.CryptoKeyStatus]: ...
    def RegisterKmsCluster(self, clusterId: KeyProviderId, managementType: str) -> NoneType: ...
    def UnregisterKmsCluster(self, clusterId: KeyProviderId) -> NoneType: ...
    def ListKmsClusters(self, includeKmsServers: bool, managementTypeFilter: int, statusFilter: int) -> List[KmipClusterInfo]: ...
    def SetKeyCustomAttributes(self, keyId: CryptoKeyId, spec: CryptoManagerKmip.CustomAttributeSpec) -> CryptoKeyResult: ...


    class CertSignRequest(vmodl.DynamicData):
        @property
        def commonName(self) -> str: ...
        @property
        def organization(self) -> str: ...
        @property
        def organizationUnit(self) -> str: ...
        @property
        def locality(self) -> str: ...
        @property
        def state(self) -> str: ...
        @property
        def country(self) -> str: ...
        @property
        def email(self) -> str: ...


    class CertificateInfo(vmodl.DynamicData):
        @property
        def subject(self) -> str: ...
        @property
        def issuer(self) -> str: ...
        @property
        def serialNumber(self) -> str: ...
        @property
        def notBefore(self) -> datetime: ...
        @property
        def notAfter(self) -> datetime: ...
        @property
        def fingerprint(self) -> str: ...
        @property
        def checkTime(self) -> datetime: ...
        @property
        def secondsSinceValid(self) -> int: ...
        @property
        def secondsBeforeExpire(self) -> int: ...


    class ClusterStatus(vmodl.DynamicData):
        @property
        def clusterId(self) -> KeyProviderId: ...
        @property
        def overallStatus(self) -> vim.ManagedEntity.Status: ...
        @property
        def managementType(self) -> str: ...
        @property
        def servers(self) -> List[CryptoManagerKmip.ServerStatus]: ...
        @property
        def clientCertInfo(self) -> CryptoManagerKmip.CertificateInfo: ...


    class CryptoKeyStatus(vmodl.DynamicData):
        @property
        def keyId(self) -> CryptoKeyId: ...
        @property
        def keyAvailable(self) -> bool: ...
        @property
        def reason(self) -> str: ...
        @property
        def encryptedVMs(self) -> List[vim.VirtualMachine]: ...
        @property
        def affectedHosts(self) -> List[vim.HostSystem]: ...
        @property
        def referencedByTags(self) -> List[str]: ...


        class KeyUnavailableReason(Enum):
            KeyStateMissingInCache = "KeyStateMissingInCache"
            KeyStateClusterInvalid = "KeyStateClusterInvalid"
            KeyStateClusterUnreachable = "KeyStateClusterUnreachable"
            KeyStateMissingInKMS = "KeyStateMissingInKMS"
            KeyStateNotActiveOrEnabled = "KeyStateNotActiveOrEnabled"
            KeyStateManagedByTrustAuthority = "KeyStateManagedByTrustAuthority"
            KeyStateManagedByNKP = "KeyStateManagedByNKP"


    class CustomAttributeSpec(vmodl.DynamicData):
        @property
        def attributes(self) -> List[vim.KeyValue]: ...


    class ServerCertInfo(vmodl.DynamicData):
        @property
        def certificate(self) -> str: ...
        @property
        def certInfo(self) -> CryptoManagerKmip.CertificateInfo: ...
        @property
        def clientTrustServer(self) -> bool: ...


    class ServerStatus(vmodl.DynamicData):
        @property
        def name(self) -> str: ...
        @property
        def status(self) -> vim.ManagedEntity.Status: ...
        @property
        def connectionStatus(self) -> str: ...
        @property
        def certInfo(self) -> CryptoManagerKmip.CertificateInfo: ...
        @property
        def clientTrustServer(self) -> bool: ...
        @property
        def serverTrustClient(self) -> bool: ...


class CryptoKeyId(vmodl.DynamicData):
    @property
    def keyId(self) -> str: ...
    @property
    def providerId(self) -> KeyProviderId: ...


class CryptoKeyPlain(vmodl.DynamicData):
    @property
    def keyId(self) -> CryptoKeyId: ...
    @property
    def algorithm(self) -> str: ...
    @property
    def keyData(self) -> str: ...


class CryptoKeyResult(vmodl.DynamicData):
    @property
    def keyId(self) -> CryptoKeyId: ...
    @property
    def success(self) -> bool: ...
    @property
    def reason(self) -> str: ...
    @property
    def fault(self) -> vmodl.MethodFault: ...


class CryptoSpec(vmodl.DynamicData): ...


class CryptoSpecDecrypt(CryptoSpec): ...


class CryptoSpecDeepRecrypt(CryptoSpec):
    @property
    def newKeyId(self) -> CryptoKeyId: ...


class CryptoSpecEncrypt(CryptoSpec):
    @property
    def cryptoKeyId(self) -> CryptoKeyId: ...


class CryptoSpecNoOp(CryptoSpec): ...


class CryptoSpecRegister(CryptoSpecNoOp):
    @property
    def cryptoKeyId(self) -> CryptoKeyId: ...


class CryptoSpecShallowRecrypt(CryptoSpec):
    @property
    def newKeyId(self) -> CryptoKeyId: ...


class KeyProviderId(vmodl.DynamicData):
    @property
    def id(self) -> str: ...


class KmipClusterInfo(vmodl.DynamicData):
    @property
    def clusterId(self) -> KeyProviderId: ...
    @property
    def servers(self) -> List[KmipServerInfo]: ...
    @property
    def useAsDefault(self) -> bool: ...
    @property
    def managementType(self) -> str: ...
    @property
    def useAsEntityDefault(self) -> List[vim.ManagedEntity]: ...
    @property
    def hasBackup(self) -> bool: ...
    @property
    def tpmRequired(self) -> bool: ...
    @property
    def keyId(self) -> str: ...


    class KmsManagementType(Enum):
        unknown = "unknown"
        vCenter = "vCenter"
        trustAuthority = "trustAuthority"
        nativeProvider = "nativeProvider"


class KmipServerInfo(vmodl.DynamicData):
    @property
    def name(self) -> str: ...
    @property
    def address(self) -> str: ...
    @property
    def port(self) -> int: ...
    @property
    def proxyAddress(self) -> str: ...
    @property
    def proxyPort(self) -> int: ...
    @property
    def reconnect(self) -> int: ...
    @property
    def protocol(self) -> str: ...
    @property
    def nbio(self) -> int: ...
    @property
    def timeout(self) -> int: ...
    @property
    def userName(self) -> str: ...


class KmipServerSpec(vmodl.DynamicData):
    @property
    def clusterId(self) -> KeyProviderId: ...
    @property
    def info(self) -> KmipServerInfo: ...
    @property
    def password(self) -> str: ...


class KmipServerStatus(vmodl.DynamicData):
    @property
    def clusterId(self) -> KeyProviderId: ...
    @property
    def name(self) -> str: ...
    @property
    def status(self) -> vim.ManagedEntity.Status: ...
    @property
    def description(self) -> str: ...