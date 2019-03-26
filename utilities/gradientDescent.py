class GradientDescent:

    def __init__(self, params={}):
        # init params
        self.theta0 = params['theta0'] if 'theta0' in params and params['theta0'].isdigit() else 0
        self.theta1 = params['theta1'] if 'theta1' in params and params['theta1'].isdigit() else 0
        self.learning_rate = params['learning_rate'] if 'learning_rate' in params and params['learning_rate'].isdigit() else 0.01
        self.data = params['data'] if 'data' in params else []
        self.m = len(self.data)

    def _derivative(self):
        theta0_dx = self.learning_rate/self.m*(sum([self.theta0+self.theta1*self.data[i]['x']-self.data[i]['y']] for i in range(self.m)))
        theta1_dx = self.learning_rate/self.m*(sum([(self.theta0+self.theta1*self.data[i]['x']-self.data[i]['y'])*self.data[i]['x']] for i in range(self.m)))
        # save
        self.theta0 = self.theta0 - self.learning_rate * theta0_dx
        self.theta1 = self.theta1 - self.learning_rate * theta1_dx

    def calculate(self, starting_t0=None, starting_t1=None):
        # if starting theta's provided check type and replace
        if isinstance(starting_t0, float) or isinstance(starting_t0, int):
            self.theta0 = starting_t0
        if isinstance(starting_t1, float) or isinstance(starting_t1, int):
            self.theta0 = starting_t1

        max_iterations = 10000
        temp_t0 = self.theta0
        temp_t1 = self.theta1
        for i in range(max_iterations):
            self._derivative()
            if temp_t0 == self.theta0 and temp_t1 == self.theta1:
                print('Found at %i iteration', i)
                return self.theta0, self.theta1
        return self.theta0, self.theta1
