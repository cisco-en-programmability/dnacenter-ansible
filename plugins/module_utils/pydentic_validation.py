#!/usr/bin/python
# below packages for pandas for data customization
# Others are Pydentic module for customized yml input validation purpose
from pydantic import ValidationError 
from uuid import UUID, uuid4
from enum import Enum
from typing_extensions import Annotated
from pydantic import BaseModel, AnyHttpUrl, Field
from pydantic.networks import IPvAnyAddress
from pydantic.functional_validators import AfterValidator
from pydantic_extra_types.mac_address import MacAddress

"""
    All below classes are used for the Pydentic Validation usage.
"""
# This pydentic custom validation like list of family can be update here.
class DeviceFamily(Enum):
    SWITCHHUBS = "Switches and Hubs"

# This is pydentic validation used the validate URL as http:// or https://
class CheckUrl(BaseModel):
    hosturl: AnyHttpUrl

# This is used to validate names should be atlease one letter required.
class CheckNames(BaseModel):
    names: str = Field(min_length=1, frozen=True)

# This used to check the port number usally will be integer
class CheckPort(BaseModel):
    port: int

# Pydentic model is available to check IP address either ipv4 or ipv6
class CheckIPaddress(BaseModel):
    managementIpAddress: IPvAnyAddress

# Pydentic model is available to check MAC address
class CheckMACaddress(BaseModel):
    macAddress: MacAddress

# This is used to check the UUID is correct format of UUID4 type
class CheckUUIDtype(BaseModel):
    id: UUID = Field(default_factory=uuid4, frozen=False)

# To check the given input of Device family in the enum list.
class CheckDeviceFamily(BaseModel):
    family: DeviceFamily

# This custom function added to the pydentic validate the specific radio type
def check_radiotype(v: int) -> int:
    assert v in (1, 2, 3, 6), f'{v} is not a correct Radio Type'
    return v

# This class to check the Radio type in 1,2,3, 6
class CheckRadioType(BaseModel):
    ap_radiotype: Annotated[int, AfterValidator(check_radiotype)]

