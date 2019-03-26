from utilities.gradientDescent import GradientDescent

import matplotlib.pyplot as plt


class WeekOne:

    @staticmethod
    def run_gd():
        # gen data
        x = [1, 1, 2, 3, 4, 3, 4, 6, 4]
        y = [2, 1, 0.5, 1, 3, 3, 2, 5, 4]

        t0 = 0
        t1 = 0.1

        m = len(x)
        data = []
        for i in range(m):
            data.append({'x': x[i], 'y': y[i]})

        try:
            gd = GradientDescent()
            result = gd.calculate(data)
        except Exception as e:
            print('Error occurred: {}'.format(str(e)))
            return

        # trash for now - will be refactored
        plt.plot(x, y, 'ro')
        plt.axis([0, 10, 0, 10])

        # first plot before
        y_before = []
        for i in range(m):
            y_before.append(t0+t1*x[i])

        plt.plot(x, y_before, color='orange')

        # second plot after
        t0, t1 = result
        x_new = x
        x_new.append(8)
        m_new = len(x_new)
        y_after = []
        for i in range(m_new):
            y_after.append(t0+t1*x[i])

        plt.plot(x_new, y_after, color='g')
        plt.show()


# run
print(WeekOne.run_gd())
