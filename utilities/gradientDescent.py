from utilities.utils import is_digit


class GradientDescent:

    def __init__(self, starting_t0=None, starting_t1=None, learning_rate=None):
        # init basic params
        self.m = 0
        self.theta0 = 0
        self.theta1 = 0
        self.learning_rate = 0.01
        # set if provided
        if is_digit(starting_t0, none=True):
            self.theta0 = starting_t0
        if is_digit(starting_t1, none=True):
            self.theta1 = starting_t1
        if is_digit(learning_rate, none=True):
            self.learning_rate = learning_rate

    def _derivative(self, data):
        theta0_dx = [(self.theta0+self.theta1*data[i]['x']-data[i]['y']) for i in range(self.m)]
        theta1_dx = [(self.theta0+self.theta1*data[i]['x']-data[i]['y'])*data[i]['x'] for i in range(self.m)]
        # save
        self.theta0 = self.theta0 - self.learning_rate/self.m * sum(theta0_dx)
        self.theta1 = self.theta1 - self.learning_rate/self.m * sum(theta1_dx)

    def _mean_squared_error(self, data):
        t0 = self.theta0
        t1 = self.theta1
        results = []
        for i in range(self.m):
            computation = t0**2+2*t0*t1*data[i]['x']-2*t0*data[i]['y']-2*t1*data[i]['x']*data[i]['y']+(t1*data[i]['x'])**2+data[i]['y']**2
            results.append(computation)
        return 1/2*self.m*(sum(results))

    def calculate(self, data):
        if not isinstance(data, list):
            raise TypeError
        self.m = len(data)
        max_iterations = 10000
        temp_t0 = self.theta0
        temp_t1 = self.theta1
        for i in range(max_iterations):
            mse = self._mean_squared_error(data)
            if mse < 0.0001:
                print ('MSE lower than 0.0001, aborting...')
                return self.theta0, self.theta1
            self._derivative(data)
            if temp_t0 == self.theta0 and temp_t1 == self.theta1:
                print('Found after {} iterations'.format(i))
                return self.theta0, self.theta1
        return self.theta0, self.theta1
