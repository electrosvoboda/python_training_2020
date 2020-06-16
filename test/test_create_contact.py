# -*- coding: utf-8 -*-
from model.contact import Contact
from fixture.application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_create_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_contact(Contact(firstname="keks", lastname="uffff", nickname="xxxxxxxxm", company="psss",
                                address="cosmos", homephone="+79990124563", mobilephone="+74952149695",
                                workphone="+79883961245", fax="+79004523625", email="agrrhzerh@mail.ru",
                                bday="7", bmonth="July", byear="1999"))
    app.session.logout()
