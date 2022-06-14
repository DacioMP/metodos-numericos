from metodos.runge_kutta import runge_kutta

if __name__ == '__main__':
    edo = '(x / y) - (y / x)'
    x0 = 1
    y0 = 2
    X = 1.2
    h = 0.1

    solucao_range_kutta = runge_kutta(edo, x0, y0, X, h)
    print(f'y({solucao_range_kutta[0]}) = {solucao_range_kutta[1]}')
