from model.contact import Contact


def test_create_contact(app, json_contact):
    contact = json_contact
    old_list_contact = app.contact.get_contact_list()
    app.contact.create_contact(contact)
    assert len(old_list_contact) + 1 == app.contact.count_con()
    new_contact = app.contact.get_contact_list()
    old_list_contact.append(contact)
    assert sorted(old_list_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)