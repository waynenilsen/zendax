import pandas
import numpy
from plotnine import *

N = 100
S0 = 32.0

def foo(initial_price):

    token1_value = []
    price = []
    for n in range(-4, 3, 2):
        price.append(initial_price * numpy.float_power(2.0, n))
        token1_value.append(0)

        price.append(initial_price * numpy.float_power(2.0, n + 1))
        token1_value.append(initial_price * numpy.float_power(2.0, n + 1))

        price.append(initial_price * numpy.float_power(2.0, n + 2))
        token1_value.append(0)

    price = numpy.array(price)
    token1_value = numpy.array(token1_value)
    token2_value = price - token1_value

    return (price, token1_value, token2_value)


def main():
    price, token1_value, token2_value = foo(S0)
    price2, token3_value, token4_value = foo(3.0 * S0 / 2.0)

    interp_price = numpy.linspace(start = 0, stop = 2**3 * S0, num = N)
    interp_token1_value = numpy.interp(interp_price, price, token1_value)
    interp_token2_value = numpy.interp(interp_price, price, token2_value)

    data = pandas.DataFrame({'price': interp_price,
                             'token1_value': interp_token1_value,
                             'token2_value': interp_token2_value,
                             'linear': interp_price
                             })

    print(data)

    data = data.melt(id_vars='price', var_name='type', value_name='value')

    print(
        ggplot(data, aes(x = 'price', y = 'value', colour='type'))
          + geom_line()
          + theme_bw()
    )


if __name__ == '__main__':
    main()