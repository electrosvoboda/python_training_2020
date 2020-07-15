import json
# work is json
# f = open("G:/python_test1/jazz.json")
# text = f.read()
# f.close()
# f2 = open("G:/python_test1/tests/jazz.json", "w")
# f2.write(text)
# f2.close()


# work in exception
# g = open("G:/python_test1/jazz.json")
# try:
#     res = json.load(g)
# except ValueError as ex:
#     print(ex)
#     res = {}
# finally:
#     g.close()
#
# print(res)

# work in with
with open("G:/python_test1/jazz.json") as h:
    try:
        res = json.load(g)
    except ValueError as ex:
        print(ex)
        res = {}
