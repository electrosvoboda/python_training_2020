from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count_con() == 0:
        app.contact.create_contact(Contact(lastname="Davis"))
    app.contact.delete_first_contact()