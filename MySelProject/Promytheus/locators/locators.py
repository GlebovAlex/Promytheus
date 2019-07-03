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
