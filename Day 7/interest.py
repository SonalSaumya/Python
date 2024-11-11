class Bank_interest_calculator:
    __interest_rate = 8.6
    __interest_rate_SeniorCitizen = 8.4

    def __init__(self,p_amount,duration,seniorCitizen):
        self.p_amount = p_amount
        self.duration = duration
        self.seniorCitizen = seniorCitizen


    def simple_interest_calulator(self):
        if self.seniorCitizen > 65:
            print("Simple interst for Senior Citizen")
            self.SI = (self.p_amount * self.duration * self.__interest_rate_SeniorCitizen)/100
            self.emi = self.p_amount * self.__interest_rate_SeniorCitizen*(1+self.__interest_rate_SeniorCitizen)**self.duration / ((1+self.__interest_rate_SeniorCitizen)**self.duration-1)

        else:
            print("Simple interst for  Citizen")
            self.SI = (self.p_amount * self.duration * self.__interest_rate)/100
            self.emi = self.p_amount * self.__interest_rate * (1 + self.__interest_rate) ** self.duration / ((1 + self.__interest_rate) ** self.duration - 1)

        return self.SI,self.emi




if __name__ == '__main__':

    c1 = Bank_interest_calculator(100,2,70)
    c2 = Bank_interest_calculator(100,2,40)

    print(c1.simple_interest_calulator())
    print(c2.simple_interest_calulator())

