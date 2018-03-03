*** Settings ***
Library           Selenium2Library

*** Variables ***
${Username}       student2
${Password}       Testing1
${Browser}        Firefox
${SiteUrl}        http://demo.mahara.org
${DashboardTitle}    Dashboard - Mahara
${Delay}          5s

*** Test Cases ***
LoginTest
    Open Browser to the Login Page
    Enter User Name
    Enter Password
    Click Login
    sleep    ${Delay}
    Assert Dashboard Title
    [Teardown]    Close Browser

*** Keywords ***
Open Browser to the Login Page
    open browser    ${SiteUrl}    ${Browser}
    Maximize Browser Window

Enter User Name
    Input Text    login_login_username    ${Username}

Enter Password
    Input Text    login_login_password    ${Password}

Click Login
    click button    login_submit

Assert Dashboard Title
    Title Should be    ${DashboardTitle}