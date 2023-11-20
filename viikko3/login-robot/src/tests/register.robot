*** Settings ***
Resource  resource.robot

*** Test Cases ***
Register With Valid Username And Password
    Input  new
    Input Credentials  kalle  kalle123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input  new
    Input Credentials  kalle  kalle123
    Input  new
    Input Credentials  kalle  kalle321
    Output Should Contain  User with username kalle already exists 

Register With Too Short Username And Valid Password
    Input  new
    Input Credentials  as  kalle321kalle
    Output Should Contain  Invalid username

Register With Enough Long But Invalid Username And Valid Password
    Input  new
    Input Credentials  kalle321  kalle321
    Output Should Contain  Invalid username

Register With Valid Username And Too Short Password
    Input  new
    Input Credentials  kalle  kalle1
    Output Should Contain  Password must be at least 8 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input  new
    Input Credentials  kalle  kallekallekalle
    Output Should Contain  Password must contain at least one digit
