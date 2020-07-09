# -*- coding: utf-8 -*-
from model.contact import Contact


def test_create_contact(app):
    old_list_contact = app.contact.get_contact_list()
    contact = Contact(firstname="keks", lastname="uffff", nickname="xxxxxxxxm", company="psss",
                                address="cosmos", homephone="+79883961245", mobilephone="+79883961245",
                                workphone="+79883961245", email="agrrhzerh@mail.ru",
                                byear="1999")
    app.contact.create_contact(contact)
    assert len(old_list_contact) + 1 == app.contact.count_con()
    new_contact = app.contact.get_contact_list()
    old_list_contact.append(contact)
    assert sorted(old_list_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)