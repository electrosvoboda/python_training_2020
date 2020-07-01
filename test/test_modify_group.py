from model.group import Group


def test_modify_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="New Group"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(name="hardbop"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="New Group"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(header="Bebop"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)