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
    user_icon_link_xpath = "//em[@class='icon-user']"
    my_profile_link_xpath = "//p[text()='My Profile']"
    sign_out_link_xpath = "//p[text()='Sign Out']"
    home_icon_xpath = "//div[@class='brand-logo']"
    # user_icon_link_xpath = "//ul[@class='nav navbar-nav navbar-right']/li[2]/a"
    # sign_out_link_xpath = "//p[contains(text(), 'Sign Out')]//ancestor::div[2]/parent::a"

    # My Profile Page locators
    my_profile_tab_link_xpath = "//a[text()='Profile']"
    pass_change_tab_link_xpath = "//a[text()='Password change']"
    current_pass_textbox_xpath = "//input[@id='currentPassword']"
    new_pass_textbox_xpath = "//input[@id='newPassword']"
    confirm_new_pass_textbox_xpath = "//input[@id='confirmNewPassword']"
    pass_update_btn_xpath = "//div[@id='tabPasswordChange']//button[text()='Update']"
    pass_change_confirm_msg_xpath = "//div[@class='sweet-alert showSweetAlert visible']/p"
    pass_change_confirm_ok_btn_xpath = "//button[@class='confirm']/parent::div"

    p_user_icon_link_xpath = "//em[@class='icon-user']"
    p_sign_out_link_xpath = "//p[text()='Sign Out']"

    # Registration Page locators

    # Personal Tab
