# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import pytest
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


param_data_test = [Contact(firstname="", lastname="", address="", homephone="", mobilephone="",
                                workphone="", email="")] + [
           Contact(firstname=random_string("firstname", 8), lastname=random_string("lastname", 8), address=random_string("address", 20),
                   homephone=random_string("homephone", 11), mobilephone=random_string("mobilephone", 12),
                   workphone=random_string("workphone", 14), email=random_string("email", 18))
           for i in range(5)
]


@pytest.mark.parametrize("contact", param_data_test, ids=[repr(z) for z in param_data_test])
def test_create_contact(app, contact):
    old_list_contact = app.contact.get_contact_list()
    app.contact.create_contact(contact)
    assert len(old_list_contact) + 1 == app.contact.count_con()
    new_contact = app.contact.get_contact_list()
    old_list_contact.append(contact)
    assert sorted(old_list_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)