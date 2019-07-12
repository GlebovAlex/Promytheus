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


    # New Talent Page Locators
    new_button_xpath = "//a[@class='btn btn-primary mr']"
    category_xpath = "//div[@class='col-lg-10']//div[@name='category']"
    painting_xpath = "//span[@class='ui-select-choices-row-inner'][contains(text(),'Painting')]"
    Next_button_xpath = "//div[@class='form-wizard-footer']//button[@class='btn btn-primary ng-binding'][contains(text(),'Next')]"

    # Talent Form Personal tab locators
    first_name_xpath = "//input[@placeholder='Enter First name']"
    last_name_xpath = "//input[@placeholder='Enter Last name']"
    Sex_female_xpath = "//label[contains(text(),'Female')]"
    country_name_selection_xpath = "//input[@placeholder='Enter country name...']"
    country_option_USA = "//span[@class='ui-select-choices-row-inner'][contains(text(),'USA')]"
    address_line1_xpath = "//input[@id='address']"
    address_line2_xpath = "//input[@name='address2']"
    city_xpath = "//input[@placeholder='Enter city']"
    state_xpath = "//input[@placeholder='Enter state']"
    postalcode_xpath = "//input[@placeholder='Enter postal code']"
    contact_email_xpath = "//input[@placeholder='Enter Email']"
    conatct_phone_xpath = "//input[@placeholder='Enter Phone']"
    height_xpath = "//input[@placeholder='Enter Height']"
    weight_xpath = "//input[@placeholder='Enter Weight']"
    personalPage_next_button_xpath = "//div[@class='form-wizard-footer']//button[@class='btn btn-primary ng-binding'][contains(text(),'Next')]"

    # Talent Traits Locators
    first_question_xpath = "//fieldset[1]//trait-scaler[1]//button[9]"
    second_question_xpath = "//fieldset[2]//trait-scaler[1]//button[8]"
    third_question_xpath = "//div[@class='row']//div[2]//div[1]//fieldset[3]//trait-scaler[1]//button[8]"
    fourth_question_xpath = "//fieldset[4]//trait-scaler[1]//button[5]"
    fifth_question_xpath = "//fieldset[5]//trait-scaler[1]//button[9]"
    sixth_question_xpath = "//fieldset[6]//trait-scaler[1]//button[9]"
    seventh_question_xpath = "//fieldset[7]//trait-scaler[1]//button[9]"
    eight_question_xpath = "//fieldset[8]//trait-scaler[1]//button[9]"
    ninth_question_xpath = "//fieldset[9]//trait-scaler[1]//button[8]"
    tenth_question_xpath = "//fieldset[10]//trait-scaler[1]//button[9]"
    eleventh_question_xpath = "//fieldset[11]//trait-scaler[1]//button[5]"
    twelfth_question_xpath = "//fieldset[12]//trait-scaler[1]//button[5]"
    thirteenth_question_xpath = "//fieldset[13]//trait-scaler[1]//button[9]"
    fourteenth_question_xpath = "//fieldset[14]//trait-scaler[1]//button[5]"
    fifteenth_question_xpath = "//fieldset[15]//trait-scaler[1]//button[5]"
    sixteenth_question_xpath = "//fieldset[16]//trait-scaler[1]//button[5]"
    traits_next_button_xpath = "//div[@class='form-wizard-footer']//button[@class='btn btn-primary ng-binding'][contains(text(),'Next')] "
