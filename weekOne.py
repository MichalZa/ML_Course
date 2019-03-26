from utilities.gradientDescent import GradientDescent


class WeekOne:

    @staticmethod
    def run_gd():
        # add reading from file or generate data
        dataset = {'x': 10, 'y': 5}, {'x': 15, 'y': 7}
        params = {'data': dataset}
        gd = GradientDescent(params)
        try:
            result = gd.calculate(5, 1)
        except Exception as e:
            print('Error occurred: {}'.format(str(e)))
            return

        return result


# run
print(WeekOne.run_gd())
