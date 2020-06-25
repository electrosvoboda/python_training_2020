from model.contact import Contact


def test_modify_contact_firstname(app):
    if app.contact.count_con() == 0:
        app.contact.create_contact(Contact(lastname="Pass"))
    app.contact.modify_first_contact(Contact(firstname="cherry"))


def test_modify_contact_nickname(app):
    if app.contact.count_con() == 0:
        app.contact.create_contact(Contact(lastname="Parker"))
    app.contact.modify_first_contact(Contact(nickname="bomb"))