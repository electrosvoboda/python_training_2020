import re


def test_all_value_contact(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_view_page = app.contact.open_contact_view_page_by_index(0)
    assert contact_from_home_page.address == merge_address_like_on_home_page(contact_from_view_page)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_address_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.address]))))
