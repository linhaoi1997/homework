from run import run


def test_1(login, pytestconfig):
    print(pytestconfig.getini("markers"))
    print(login)


if __name__ == '__main__':
    run(__file__)
