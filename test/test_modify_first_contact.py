from model.contact import Contact
from random import randrange


def test_modify_some_contact(app):
    if app.contact.count_con() == 0:
        app.contact.create_contact(Contact(lastname="Pass"))
    old_list_contact = app.contact.get_contact_list()
    index = randrange(len(old_list_contact))
    contact = Contact(firstname="wtf", lastname="man")
    contact.id = old_list_contact[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_list_contact) == app.contact.count_con()
    old_list_contact[index] = contact
    assert sorted(old_list_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)


# def test_modify_contact_nickname(app):
#     if app.contact.count_con() == 0:
#         app.contact.create_contact(Contact(lastname="Parker"))
#     app.contact.modify_first_contact(Contact(nickname="bomb"))