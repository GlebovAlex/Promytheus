class Locators:

    # Login Page locators
    email_textbox_xpath = "//input[@name='email']"
    pass_textbox_xpath = "//input[@name='password']"
    login_btn_xpath = "//button[@id='login']"
    error_msg_login_xpath = "//div[@class='alert alert-danger ng-binding ng-scope']"
    error_msg_blank_email_xpath = "//input[@name='email']/parent::div/span[2]"
    error_msg_blank_pass_xpath = "//input[@name='password']/parent::div/span[2]"
    register_btn_xpath = "//a[text()='Register Now']"
    reset_pass_link_xpath = "//a[contains(text(), 'password')]"

    # Home Page locators
    user_icon_link_xpath = "//ul[@class='nav navbar-nav navbar-right']/li[2]/a"
    sign_out_link_xpath = "//p[contains(text(), 'Sign Out')]//ancestor::div[2]/parent::a"

    # Registration Page locators

    regpage_register_btn_xpath = "//a[@class='btn btn-block btn-default']"
    regpage_fname_xpath = "//input[@id='signUpFirstName']"
    regpage_mname_xpath = "//input[@id='signUpMiddleName']"
    regpage_lname_xpath = "//input[@id='signUpLastName']"
    regpage_phone_xpath = "//input[@id='signUpPhone']"
    regpage_email_xpath = "//input[@id='signUpRegisterEmail']"
    regpage_pwd_xpath = "//input[@id='signUpRegisterPassword']"
    regpage_retypepwd_xpath = "//input[@id='signUpRegisterRePassword']"
    regpage_country_xpath = "//span[@class='ui-select-match-text pull-left']"
    regpage_address_xpath = "//input[@id='signUpAddress']"
    regpage_city_xpath = "//input[@id='signUpCity']"
    regpage_state_xpath = "//input[@id='signUpState']"
    regpage_zipcode_xpath = "//input[@id='signUpZip']"
    regpage_pvtcheck_xpath = "//input[@id='privacyPolicyAgree']"
    regpage_createbtn_xpath = "//button[@id='createAccount']"
    regpage_okbtn_aftcreate_xpath = "/html/body/div[2]/div[7]/div/button"
    regpage_exixting_emailid_errormsg_xpath = "//span[@class='text-danger']"

    # Personal Tab

    # Personality Traits tab
    pt_personality_tab_xpath = "//span[contains(text(),'Personality Traits')]"
    pt_checkbox1_xpath = "//tr[3]//td[2]//label[1]//input[1]"
    pt_checkbox6_xpath = "//tr[6]//td[2]//label[1]//input[1]"
    # pt_checkbox16_xpath = "//tr[16]//td[2]//label[1]//input[1"
    pt_nextbtn_xpath = "//div[@class='form-wizard-footer']//button[@class='btn btn-primary ng-binding'][contains(text(),'Next')]"

    # Story tab
    stry_storytab_xpath = "//span[contains(text(),'Story')]"
    stry_age_xpath = "//input[@placeholder='Years Old']"
    stry_interest_level_xpath = "//select[@name='interestLevel']"
    stry_interest_menusel_xpath = "//option[contains(text(),'Moderate - Would consider making it a career')]"
    stry_nextbtn_xpath = "//div[@class='form-wizard-footer']//button[@class='btn btn-primary ng-binding'][contains(text(),'Next')]"

