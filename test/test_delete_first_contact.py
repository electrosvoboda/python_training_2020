from model.contact import Contact
from random import randrange


def test_delete_some_contact(app):
    if app.contact.count_con() == 0:
        app.contact.create_contact(Contact(lastname="Davis"))
    old_list_contact = app.contact.get_contact_list()
    index = randrange(len(old_list_contact))
    app.contact.delete_contact_by_index(index)
    new_contact = app.contact.get_contact_list()
    assert len(old_list_contact) - 1 == app.contact.count_con()
    old_list_contact[index:index + 1] = []
    assert sorted(old_list_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)