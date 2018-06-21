import datetime
import math


class PricingUtil(object):
    def get_blackcalculator_std(self, dt_eval, dt_maturity, annualized_vol):
        stdDev = annualized_vol * math.sqrt(self.get_ttm(dt_eval,dt_maturity))
        return stdDev

    def get_discount(self, dt_eval, dt_maturity, rf):
        discount = math.exp(-rf * self.get_ttm(dt_eval,dt_maturity))
        return discount

    def get_ttm(self, dt_eval, dt_maturity):
        N = (dt_maturity - dt_eval).total_seconds() / 60.0
        N365 = 365 * 1440.0
        ttm = N/N365
        return ttm

class Calendar(object):
    def leepDates(self, dt1, dt2):
        # swap dt1 and dt2 if dt1 is earlier than dt2
        if (dt1 - dt2).days < 0:
            tmp = dt2
            dt2 = dt1
            dt1 = tmp
        # dt1 > dt2
        year1 = dt1.year
        year2 = dt2.year
        daysWithoutLeap = (year1 + 1 - year2) * 365
        daysWithLeap = (datetime.date(year1 + 1, 1, 1) - datetime.date(year2, 1, 1)).days
        leapDays = daysWithLeap - daysWithoutLeap
        if self.isLeapYear(dt1.year) and (dt1 - datetime.date(year1, 2, 29)).days < 0:
            print((dt1 - datetime.date(year1, 2, 29)).days)
            leapDays -= 1
        if self.isLeapYear(dt2.year) and (dt2 - datetime.date(year2, 2, 29)).days > 0:
            leapDays -= 1
        return (dt1 - dt2).days - leapDays

    def isLeapYear(self, year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

        # d1 = datetime.date(2016,12,22)
        # d2 = datetime.date(2015,1,11)
        #
        # d3 = datetime.date(d1.year,d2.month,d2.day)
        #
        # _leapdates = (d1-d3).days-leepDates(d1,d3)
        # frac_part = (d1-d3).days/(365.0+_leapdates)
        # yearFrac = (d1.year-d2.year)+frac_part
        #
        # print((d1-d2).days)
        # print(leepDates(d1,d2))
        # print(_leapdates)
        # print(leepDates(d1,d2)/365)
        # print(yearFrac)
