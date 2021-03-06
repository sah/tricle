def math():
    response = yield "1+2"
    print("I got:", response)
    response = yield "3*3"
    print("I got:", response)
    response = yield "4*7"
    print("I got:", response)


def event_loop(g):
    command = next(g)
    while True:
        if command == "1+2":
            command = g.send("3")
        elif command == "3*3":
            command = g.send("9")
        elif command == "4*7":
            command = g.send("28")
        else:
            g.throw(Exception())
            return


event_loop(math())
