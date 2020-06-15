# -*- coding: utf-8 -*-
from contact import Contact
from application2 import Application2
import pytest


@pytest.fixture
def app2(request):
    fixture = Application2()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_create_contact(app2):
    app2.login(username="admin", password="secret")
    app2.create_contact(Contact(firstname="keks", lastname="uffff", nickname="xxxxxxxxm", company="psss",
                                address="cosmos", homephone="+79990124563", mobilephone="+74952149695",
                                workphone="+79883961245", fax="+79004523625", email="agrrhzerh@mail.ru",
                                bday="7", bmonth="July", byear="1999"))
    app2.logout()
