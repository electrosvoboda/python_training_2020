from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count_con() == 0:
        app.contact.create_contact(Contact(lastname="Davis"))
    old_list_contact = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    assert len(old_list_contact) - 1 == app.contact.count_con()
    new_contact = app.contact.get_contact_list()
    old_list_contact[0:1] = []
    assert sorted(old_list_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)