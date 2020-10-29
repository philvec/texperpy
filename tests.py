from texperpy import Experiments

if __name__ == '__main__':
    def f1(x):
        return x**2

    def f2(x, y):
        return x**2 + y

    texp = Experiments()
    texp.add(f1, [[1, 2, 3, 4, 5, 10, 15]])
    #texp.add(f1, [[1, 2, 3, 4, 5], [0, 2, 5]])
    results = texp.run()

    print(results)
