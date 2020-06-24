from model.contact import Contact


def test_modify_contact_firstname(app):
    app.contact.modify_first_contact(Contact(firstname="cherry"))


def test_modify_contact_nickname(app):
    app.contact.modify_first_contact(Contact(nickname="bomb"))