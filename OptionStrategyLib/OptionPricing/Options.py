import QuantLib as ql

class Option(object):
    def __init__(self,strike,maturitydt):
        self.strike = strike
        self.maturitydt = maturitydt

class OptionPlainEuropean(object):

    def __init__(self, strike, maturitydt, optionType,init_price=None):
        self.strike = strike
        self.maturitydt = maturitydt
        self.optionType = optionType
        exercise = ql.EuropeanExercise(maturitydt)
        payoff = ql.PlainVanillaPayoff(optionType, strike)
        option = ql.EuropeanOption(payoff, exercise)
        self.exercise = exercise
        self.payoff = payoff
        self.option_ql = option
        self.init_price = init_price

class OptionPlainAmerican:
    def __init__(self, strike,effectivedt, maturitydt, optionType):
        self.strike = strike
        self.maturitydt = maturitydt
        self.optionType = optionType
        exercise = ql.AmericanExercise(effectivedt,maturitydt)
        payoff = ql.PlainVanillaPayoff(optionType, strike)
        option = ql.VanillaOption(payoff, exercise)
        self.option_ql = option

class OptionBarrierEuropean:
    def __init__(self, strike, maturitydt, optionType, barrier, barrierType):
        self.strike = strike
        self.maturitydt = maturitydt
        self.optionType = optionType
        self.barrier = barrier
        self.barrierType = barrierType
        exercise = ql.EuropeanExercise(maturitydt)
        self.exercise = exercise
        payoff = ql.PlainVanillaPayoff(optionType, strike)
        self.payoff = payoff
        barrieroption = ql.BarrierOption(barrierType, barrier, 0.0, payoff, exercise)
        self.option_ql = barrieroption



# class OptionPlainAsian:
#     def __init__(self, strike,effectivedt, maturitydt, optionType):
#         self.strike = strike
#         self.maturitydt = maturitydt
#         self.optionType = optionType
#         exercise = ql.EuropeanExercise(maturitydt)
#         payoff = ql.PlainVanillaPayoff(optionType, strike)
#         option = ql.DiscreteAveragingAsianOption(payoff, exercise,)
#         self.option_ql = option