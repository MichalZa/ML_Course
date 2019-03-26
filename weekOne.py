from utilities.gradientDescent import GradientDescent


class WeekOne:

    @staticmethod
    def run_gd():
        # add reading from file or generate data
        data = {}
        gd = GradientDescent(data)
        try:
            result = gd.calculate()
        except Exception as e:
            print('Error occured: %s', str(e))
            return

        return result


# run
week_one = WeekOne()
print(week_one.run_gd())
