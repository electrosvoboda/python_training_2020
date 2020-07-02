from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count_con() == 0:
        app.contact.create_contact(Contact(lastname="Davis"))
    old_list_contact = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    new_contact = app.contact.get_contact_list()
    assert len(old_list_contact) - 1 == len(new_contact)
    old_list_contact[0:1] = []
    assert sorted(old_list_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)