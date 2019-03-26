from utilities.gradientDescent import GradientDescent


class WeekOne:

    @staticmethod
    def run_gd():
        # add reading from file or generate data
        data = {}
        gd = GradientDescent(data)
        return gd.calculate()


# run
week_one = WeekOne()
print(week_one.run_gd())
