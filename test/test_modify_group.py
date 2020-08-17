from random import randrange
from model.group import Group


def test_modify_group(app, db, check_ui):
    if app.group.count() == 0:
        app.group.create(Group(name="New Group"))
    old_groups = db.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="hardbop")
    group.id = old_groups[index].id
    app.group.modify_group_by_id(group.id)
    new_groups = db.get_group_list()
    assert len(old_groups) == app.group.count()
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


# def test_modify_group_header(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="New Group"))
#     old_groups = app.group.get_group_list()
#     app.group.modify_first_group(Group(header="Bebop"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)