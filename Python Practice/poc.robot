*** Settings ***
Documentation    This is KVS API Test Suite
Suite Setup  Suite Precondition
Suite Teardown  Suite Cleanup
Library  ../Python_lib/device_api_robot.py
Library  OperatingSystem
Library  BuiltIn
Library  Process
Library  String


*** Test Cases ***
DeviceOpen
    [Documentation]  This is Open device test case documentation.
    [Tags]   Sanity  CLI
    [Setup]  Precondition
    ${out}=  open device  0
    Log  ${out}
    #Log To Console  [${out}]
    Should Be Equal As Numbers  ${out}  0
CreateContainer
    ${out}=  create container  0  Test
    Log  ${out}
    #Log To Console  [${out}]
    Should Be Equal As Numbers  ${out}  0
    ${out}=  create container  0  Test1  ordered1=1  index_count1=3   key_index1=[1,2,3]
    Log  ${out}
    #Log To Console  [${out}]
    Should Be Equal As Numbers  ${out}  1
    ${out}=  create container  0  Test2  ordered1=1  index_count1=3   key_index1=[1,2,3]
    Log  ${out}
    #Log To Console  [${out}]
    Should Be Equal As Numbers  ${out}  2

CloseDevice
    ${out}=  close device  0 
    Log  ${out}
    #Log To Console  [${out}]
    Should Be Equal As Numbers  ${out}  0
    [Teardown]  Cleanup
	
	
*** Keywords ***
Suite Precondition
    Log  Suite precondition  
Suite Cleanup
    Log  Suite cleanup  
Precondition
    Log  This is Precondition in KVS API test case.
Cleanup
    Log  This is Cleanup in KVS API test case.
	
	
*** Variables ***
${ssh_obj}
${hostname}  ssjc-eng-a4-stor1.eng.stellus.in
${username}  root
${password}  sfast1