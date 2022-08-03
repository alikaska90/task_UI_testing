import os.path


def test_check_halva_checkbox_agree(app):
    app.halva.click_halva_request()
    app.halva.click_checkbox_agree()
    # check that checkbox is disabled
    assert not app.halva.check_status_checkbox_agree()

    # check message for disabled checkbox
    assert app.halva.get_status_messages("checkbox")
    text_message = app.halva.checkbox_message
    assert text_message == "Необходимо согласие с условиями"


def test_check_halva_invalid_card_request(app):
    app.halva.click_halva_request()
    current_url = app.driver.current_url
    if app.halva.check_status_checkbox_agree():
        app.halva.click_checkbox_agree()
    app.halva.click_get_card_button()
    new_url = app.driver.current_url

    # check that url wasn't changed
    assert current_url == new_url

    app.halva.get_status_messages("fields")
    field_list = ['Фамилия Имя Отчество',
                  'Дата рождения',
                  'Телефон',
                  'Регион']
    fild_messages = app.halva.field_messages
    # check that all fields have warning message
    assert list(fild_messages) == field_list
    print(fild_messages)
    app.halva.close_page()
    if "website" in app.search_engine.window_handle:
        app.search_engine.switch_to_website()


def test_credits(app):
    app.credits.open_credit_page()
    app.credits.download_file_remainder_ib()
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../downloads/Памятка ИБ.docx")
    # check that file was downloaded
    assert os.path.exists(file_path)
    # check type of file
    assert os.path.isfile(file_path)
