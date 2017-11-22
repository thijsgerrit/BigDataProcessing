def reduceL(xs, init, function):
    acc = init

    for x in xs:
        acc = function(acc, x)

    return acc


def reduceR(xs, init, function):
    acc = init

    for i in range(len(xs)):
        acc = function(xs[-i-1], acc)

    return acc

xs = list(range(1,10))
print(xs)
print("reduceL: {0}".format(reduceL(xs, 1, lambda x, y: x * 1 / y)))
print("reduceR: {0}".format(reduceR(xs, 1, lambda x, y: x * 1 / y)))


def reduceLwithR(xs, init, function):
    new_xs = []
    for i in range(len(xs)):
        new_xs.append(1/xs[i])

    return reduceR(new_xs,init,function)

print(reduceLwithR(xs, 1, lambda x, y: x * 1 / y))
