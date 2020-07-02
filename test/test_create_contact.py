# -*- coding: utf-8 -*-
from model.contact import Contact


def test_create_contact(app):
    old_list_contact = app.contact.get_contact_list()
    contact = Contact(firstname="keks", lastname="uffff", nickname="xxxxxxxxm", company="psss",
                                address="cosmos", homephone="+79990124563", mobilephone="+74952149695",
                                workphone="+79883961245", fax="+79004523625", email="agrrhzerh@mail.ru",
                                byear="1999")
    app.contact.create_contact(contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_list_contact) + 1 == len(new_contact)
    old_list_contact.append(contact)
    assert sorted(old_list_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)