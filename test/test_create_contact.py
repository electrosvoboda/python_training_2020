# -*- coding: utf-8 -*-
from model.contact import Contact


def test_create_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_contact(Contact(firstname="keks", lastname="uffff", nickname="xxxxxxxxm", company="psss",
                                address="cosmos", homephone="+79990124563", mobilephone="+74952149695",
                                workphone="+79883961245", fax="+79004523625", email="agrrhzerh@mail.ru",
                                byear="1999"))
    app.session.logout()