from model.contact import Contact


def test_modify_contact_firstname(app):
    if app.contact.count_con() == 0:
        app.contact.create_contact(Contact(lastname="Pass"))
    old_list_contact = app.contact.get_contact_list()
    contact = Contact(firstname="cherry")
    contact.id = old_list_contact[0].id
    new_contact = app.contact.get_contact_list()
    app.contact.modify_first_contact(contact)
    assert len(old_list_contact) == len(new_contact)
    old_list_contact[0] = contact
    assert sorted(old_list_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)


# def test_modify_contact_nickname(app):
#     if app.contact.count_con() == 0:
#         app.contact.create_contact(Contact(lastname="Parker"))
#     app.contact.modify_first_contact(Contact(nickname="bomb"))