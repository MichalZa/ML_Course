
class GradientDescent:

    def __init__(self, params={}):
        # init params
        self.theta0 = params['theta0'] if 'theta0' in params and params['theta0'].isdigit() else 0
        self.theta1 = params['theta1'] if 'theta1' in params and params['theta1'].isdigit() else 0
        self.learning_rate = params['learning_rate'] if 'learning_rate' in params and params['learning_rate'].isdigit() else 0.01

    # compute derivative for function (x + 10)**2
    def _derivatie(self, x):
        return 2 * (x + 10)

    def _compute_each(self, x):
        if isinstance(x, str):
            raise ValueError()
        return x - (self.learning_rate * self._derivatie(x))

    def calculate(self, starting_value):
        iters = 10000
        temp = starting_value
        for i in range(iters):
            computed = self._compute_each(temp)
            if temp == computed:
                return computed
            temp = computed
