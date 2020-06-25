from model.group import Group


def test_modify_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="New Group"))
    app.group.modify_first_group(Group(name="hardbop"))


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="New Group"))
    app.group.modify_first_group(Group(header="Bebop"))