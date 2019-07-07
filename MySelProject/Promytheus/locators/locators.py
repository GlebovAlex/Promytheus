class Locators:

    # Login Page locators
    email_textbox_xpath = "//input[@name='email']"
    password_textbox_xpath = "//input[@name='password']"
    login_button_xpath = "//button[@id='login']"
    error_message_invalid_email_or_pass = "//div[@class='alert alert-danger ng-binding ng-scope']"
    error_message_blank_email = "//input[@name='email']/parent::div/span[2]"
    error_message_blank_pass = "//input[@name='password']/parent::div/span[2]"
    register_button = "//a[text()='Register Now']"
    reset_password_link = "//a[contains(text(), 'password')]"

    # Home Page locators
    user_icon_link_xpath = "//ul[@class='nav navbar-nav navbar-right']/li[2]/a"
    sign_out_link_xpath = "//p[contains(text(), 'Sign Out')]//ancestor::div[2]/parent::a"

    #Talent Page Locators
    new_button_xpath="//a[@class='btn btn-primary mr']"
    category_xpath="//div[@class='col-lg-10']//div[@name='category']"
    painting_xpath="//span[@class='ui-select-choices-row-inner'][contains(text(),'Painting')]"
    Next_button_xpath="//div[@class='form-wizard-footer']//button[@class='btn btn-primary ng-binding'][contains(text(),'Next')]"

    #Talent Form Personal tab locators
    first_name_xpath="//input[@placeholder='Enter First name']"
    last_name_xpath="//input[@placeholder='Enter Last name']"
    Sex_female_xpath="//label[contains(text(),'Female')]"
    country_name_selection_xpath="//input[@placeholder='Enter country name...']"
    country_option_USA="//span[@class='ui-select-choices-row-inner'][contains(text(),'USA')]"
    address_line1_xpath="//input[@id='address']"
    address_line2_xpath="//input[@name='address2']"
    city_xpath="//input[@placeholder='Enter city']"
    state_xpath="//input[@placeholder='Enter state']"
    postalcode_xpath="//input[@placeholder='Enter postal code']"
    contact_email_xpath="//input[@placeholder='Enter Email']"
    conatct_phone_xpath="//input[@placeholder='Enter Phone']"
    height_xpath="//input[@placeholder='Enter Height']"
    weight_xpath="//input[@placeholder='Enter Weight']"
    personalPage_next_button_xpath="//div[@class='form-wizard-footer']//button[@class='btn btn-primary ng-binding'][contains(text(),'Next')]"


    #Talent Traits Locators
    
