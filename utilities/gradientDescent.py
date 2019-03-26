from utilities.utils import TypeHelper


class GradientDescent:

    def __init__(self, params={}):
        # init params
        self.theta0 = 0
        self.theta1 = 0
        self.learning_rate = 0.01
        self.data = params['data'] if 'data' in params and isinstance(params['data'], list) else []
        self.m = len(self.data)

    def _derivative(self):
        theta0_dx = self.learning_rate/self.m*(sum([self.theta0+self.theta1*self.data[i]['x']-self.data[i]['y']] for i in range(self.m)))
        theta1_dx = self.learning_rate/self.m*(sum([(self.theta0+self.theta1*self.data[i]['x']-self.data[i]['y'])*self.data[i]['x']] for i in range(self.m)))
        # save
        self.theta0 = self.theta0 - self.learning_rate * theta0_dx
        self.theta1 = self.theta1 - self.learning_rate * theta1_dx

    def calculate(self, starting_t0=None, starting_t1=None, learning_rate=None):
        # if starting theta's or lr provided, check and replace
        if TypeHelper.is_digit(starting_t0, none=True):
            self.theta0 = starting_t0
        if TypeHelper.is_digit(starting_t0, none=True):
            self.theta1 = starting_t1
        if TypeHelper.is_digit(starting_t0, none=True):
            self.learning_rate = learning_rate

        max_iterations = 10000
        temp_t0 = self.theta0
        temp_t1 = self.theta1
        for i in range(max_iterations):
            self._derivative()
            if temp_t0 == self.theta0 and temp_t1 == self.theta1:
                print('Found at %i iteration', i)
                return self.theta0, self.theta1
        return self.theta0, self.theta1
