*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Input Text  username  kalle
    Input Text  password  kalle321kalle
    Input Text  password_confirmation  kalle321kalle
    Click Button  Register
    Title Should Be  Welcome to Ohtu Application!

Register With Too Short Username And Valid Password
    Input Text  username  ka
    Input Text  password  kalle321kalle
    Input Text  password_confirmation  kalle321kalle
    Click Button  Register
    Page Should Contain  Invalid username

Register With Valid Username And Invalid Password
    Input Text  username  kalle
    Input Text  password  kallekalle
    Input Text  password_confirmation  kallekalle
    Click Button  Register
    Page Should Contain  Password must contain at least one digit
    Input Text  username  kalle
    Input Text  password  kalle1
    Input Text  password_confirmation  kalle1
    Click Button  Register
    Page Should Contain  Password must be at least 8 characters long


Register With Nonmatching Password And Password Confirmation
    Input Text  username  kalle
    Input Text  password  kalle12345
    Input Text  password_confirmation  kalle54321
    Click Button  Register
    Page Should Contain  Password and confirmation do not match


Login After Successful Registration
    Input Text  username  frodo
    Input Text  password  frodo321
    Input Text  password_confirmation  frodo321
    Click Button  Register
    Logout
    Go To  ${LOGIN_URL}
    Input Text  username  frodo
    Input Text  password  frodo321
    Click Button  Login
    Main Page Should Be Open

Login After Failed Registration
    Input Text  username  samwais
    Input Text  password  bagend
    Click Button  Register
    Go To  ${LOGIN_URL}
    Input Text  username  samwais
    Input Text  password  bagend
    Click Button  Login
    Page Should Contain  Invalid username or password
