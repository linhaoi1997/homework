import os


def find_dir(path, times=1):
    while times > 0:
        path = os.path.dirname(path)
        times -= 1
    return path


def return_path(path):
    pro_dir = os.path.dirname(__file__)
    return os.path.join(find_dir(__file__, 2), path)


if __name__ == '__main__':
    print(return_path("output/log/test.log"))
