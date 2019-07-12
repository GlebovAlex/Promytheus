class Locators:

    # ----------------------------------- Login Page locators ------------------------------------
    email_textbox_xpath = "//input[@name='email']"
    pass_textbox_xpath = "//input[@name='password']"
    login_btn_xpath = "//button[@id='login']"
    error_msg_login_xpath = "//div[@class='alert alert-danger ng-binding ng-scope']"
    error_msg_blank_email_xpath = "//input[@name='email']/parent::div/span[2]"
    error_msg_blank_pass_xpath = "//input[@name='password']/parent::div/span[2]"
    register_btn_xpath = "//a[text()='Register Now']"
    reset_pass_link_xpath = "//a[contains(text(), 'password')]"

    # ------------------------------------ Talents Home Page locators ------------------------------------
    # User icon
    user_icon_link_xpath = "//em[@class='icon-user']"
    # My Profile link
    my_profile_link_xpath = "//p[text()='My Profile']"
    # Sign Out Link
    sign_out_link_xpath = "//p[text()='Sign Out']"
    # Home icon
    home_icon_xpath = "//div[@class='brand-logo']"
    # user_icon_link_xpath = "//ul[@class='nav navbar-nav navbar-right']/li[2]/a"
    # sign_out_link_xpath = "//p[contains(text(), 'Sign Out')]//ancestor::div[2]/parent::a"

    # New Talent button
    new_talent_btn_xpath = "//a[text()='New']"

    # Edit icon of talent 1
    talent_1_edit_icon_xpath = "//em[@class='icon-pencil']"

    # ------------------------------------ My Profile Page locators ------------------------------------
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

    # ----------------------------- Registration Page locators ----------------------

    # ----------------------------- Talents Form General ----------------------------

    # Next button
    next_btn = "//form[@id='talentForm']//button[text()='Next']"
    # Previous button
    prev_btn = "//form[@id='talentForm']//button[text()='Previous']"

    # ------------------------------------ Category Tab ------------------------------------
    category_select_xpath = "//label[text()='Category']/parent::div//div[@name='category']/div/span"
    category_business_xpath = "//*[normalize-space(text()) and normalize-space(.)='Enter category name...'])[1]/following::span[3]"

    # ------------------------------------ Personal Tab ------------------------------------

    # ------------------------------------ Evidence Tab ------------------------------------

    # Evidence tab link
    # evidence_tab_link_xpath = "//form[@id='talentForm']//span[text()='Evidence']/parent::li[1]"
    evidence_tab_link_xpath = "//form[@id='talentForm']//span[text()='Evidence']"
    # evidence_tab_link_xpath = "//span[text()='Evidence']"

    # Testimonies of people who know talent
    testimony_checkbox_family_xpath = "//label[contains(text(), 'Family')]/span"
    testimony_checkbox_teachers_xpath = "//label[contains(text(), 'Teachers')]/span"
    testimony_checkbox_friends_xpath = "//label[contains(text(), 'Friends')]/span"
    testimony_checkbox_coworkers_xpath = "//label[contains(text(), 'Co-workers')]/span"
    testimony_family_textbox_01_xpath = "//textarea[@name='testimonyTextFieldFamily0']"
    talent_work_product_textfield_xpath = "//input[@name='workProduct']"
    family_01_upload_file_btn_name = "{{ TalentForm.testimonyFileFieldName(testimonyDefinition.textFieldName, $index) }}"
    # family_01_upload_file_btn_xpath = "//button[@name='testimonyFileFieldFamily0']"
    talent_work_product_upload_file_btn_xpath = "//button[@name='workProductFile']"

    # ----------------------------------------------------- Training ------------------------------------------------

    # Training tab link
    training_tab_link_xpath = "//span[text()='Training']"

    # Training History
    training_history_select_xpath = "//select[@name='trainingHistory']"
    training_history_select_none_xpath = "//select[@name='trainingHistory']/option[@value='NONE']"
    training_history_select_less_one_year_xpath = "//select[@name='trainingHistory']/option[contains(text(), 'Less than a year')]"
    training_history_select_more_one_year_xpath = "//select[@name='trainingHistory']/option[contains(text(), 'More than 1 year')]"
    training_history_select_more_two_year_xpath = "//select[@name='trainingHistory']/option[contains(text(), 'More than 2 years')]"
    training_history_select_more_three_year_xpath = "//select[@name='trainingHistory']/option[contains(text(), 'More than 3 years')]"
    training_history_select_more_five_year_xpath = "//select[@name='trainingHistory']/option[contains(text(), 'More than 5 years')]"

    # Professionally Coached
    coached_radio_yes_xpath = "//input[@name='coached']/parent::label[text()='Yes']/span"
    coached_radio_no_xpath = "//input[@name='coached']/parent::label[text()='No']/span"

    # If Coached yes, text fields:
    coached_enter_name_textbox_xpath = "//div[@class='col-lg-8']//input[@placeholder='Enter Name']"
    coached_enter_success_level_xpath = "//div[@class='col-lg-3']//input[@placeholder='Enter Success level']"

    # Types of Training
    training_type_intensive_xpath = "//input[@name='training']/parent::label[text()='Intensive']/span"
    training_type_sometimes_xpath = "//input[@name='training']/parent::label[text()='Sometimes']/span"

    # School or College
    school_textbox_xpath = "//input[@name='schoolName']"

    # Success Level
    school_success_level_textbox_xpath = "//input[@name='schoolSuccessLevel']"

    # Skill Level
    skill_level_radio_beginner_xpath = "//input[@name='skill']/parent::label[text()='Beginner']/span"
    skill_level_radio_advanced_xpath = "//input[@name='skill']/parent::label[text()='Advanced']/span"
    skill_level_radio_pro_xpath = "//input[@name='skill']/parent::label[text()='Pro']/span"

    # Next button
    training_button_next_xpath = "//button[text()='Next']"
    training_button_previous_xpath = "//button[text()='Previous']"
