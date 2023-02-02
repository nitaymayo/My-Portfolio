class HyperParameter:

    def __init__(self, name, value, step, start, stop, update_rate=None, chart: bool = False):
        self.stop = stop
        self.start = start
        self.step = step
        self.value = value
        self.name = name
        self.past_values = []
        self.update_rate = update_rate
        self.chart = chart

    def to_str(self):
        res = "\r\nname: {0}\r\n" \
              "value: {1}\r\n" \
              "start: {2}\r\n" \
              "step: {3}\r\n" \
              "stop: {4}\r\n" \
              "update rate: {5} \r\n".format(self.name, self.value, self.start, self.step, self.stop, self.update_rate)
        return res

    def __repr__(self):
        return int(self.value)

    def set_value(self, value):
        if value in range(self.start, self.stop):
            self.past_values.append(self.value)
            self.value = value
            return True
        else:
            return False

    def increase(self, value=None):
        if value:
            if self.value + value <= self.stop:
                self.past_values.append(self.value)
                self.value += value
                return True
            else:
                return False
        else:
            if self.value + self.step <= self.stop:
                self.past_values.append(self.value)
                self.value += self.step
                return True
            else:
                return False

    def decrease(self, value=None):
        if value:
            if self.value - value >= self.start:
                self.past_values.append(self.value)
                self.value -= value
                return True
            else:
                return False
        else:
            if self.value - self.step >= self.start:
                self.past_values.append(self.value)
                self.value -= self.step
                return True
            else:
                return False

    def get_slope(self, past_steps=None):
        if len(self.past_values) < 2:
            return False
        if past_steps:
            if past_steps < len(self.past_values):
                res = (self.past_values[-1] - self.past_values[-past_steps]) / past_steps
                return res

        return (self.past_values[-1] - self.past_values[-2]) / 2

    def get_value(self):
        return self.value

    def make_chart(self):
        return self.chart

    def set_parameter(self):
        print("Set {0}(leave empty to keep last value):".format(self.name))

        for x in ["Value", "Step", "Start", "Stop", "Update_rate", "Chart"]:
            while True:
                user_input = input("{0}(current value: {1}): ".format(x, self.__dict__[x.lower()]))
                try:
                    if user_input != "":
                        if x == "Chart":
                            self.__dict__[x.lower()] = bool(user_input)
                        else:
                            self.__dict__[x.lower()] = float(user_input)

                        break
                    else:
                        break
                except Exception as err:
                    print(err.args)
                    print("Error, try again")
