def runge_kutta(edo, x0, y0, X, h, casas_decimais=5):
    """ Aplica o método de Runge-Kutta de ordem 4 para solucionar
    problemas de valor inicial (PVI).

    :param edo: Edo a ser resolvida.
    :type edo: str
    :param x0: valor inicial da variável independente.
    :type x0: float
    :param y0: valor inicial da variável dependente.
    :type y0: float
    :param X: valor da variável independente para o qual se deseja determinar o valor y(X).
    :type X: float
    :param h: passo de cada iteração
    :type h: float
    :param casas_decimais: número de casas decimais da solução
    :type casas_decimais: int
    :return: solução do PVI (y) e o valor de x relacionado ao valor de y.
    """

    # Define dx/dy
    Y = lambda x, y: eval(edo)

    # Define as equações do Método de Runge_Kutta
    K1 = lambda x, y, h: h * Y(x, y)
    K2 = lambda x, y, h: h * Y(x + h / 2, y + K1(x, y, h) / 2)
    K3 = lambda x, y, h: h * Y(x + h / 2, y + K2(x, y, h) / 2)
    K4 = lambda x, y, h: h * Y(x + h, y + K3(x, y, h))
    Yk = lambda x, y, h: y + (1 / 6) * (K1(x, y, h) + 2 * K2(x, y, h) + 2 * K3(x, y, h) + K4(x, y, h))

    # Aplicação do método
    while True:
        k1 = K1(x0, y0, h)
        k2 = K2(x0, y0, h)
        k3 = K3(x0, y0, h)
        k4 = K4(x0, y0, h)
        yk = Yk(x0, y0, h)

        if x0 >= X:
            x, y = round(x0, casas_decimais), round(y0, casas_decimais)
            return x, y
        y0 = yk
        x0 += h