# from asyncio.windows_events import NULL

class SalaryTool:

    def ISR(self,salary):
        annualRent = 0
        impoAnnual = salary * 12

        if (impoAnnual < 416220.00):
            annualRent = 0
        elif impoAnnual > 416220.01 and impoAnnual < 624329.00:
            annualRent = (impoAnnual - 416220.01) * 0.15
        elif impoAnnual > 624329.01 and impoAnnual < 867123.00:
            annualRent = (impoAnnual - 624329.01) * 0.2 + 31216.00
        elif impoAnnual > 867123.00:
            annualRent = (impoAnnual - 867123.01) * 0.25 + 79776.00

        isr = annualRent / 12

        isr=float("{:.2f}".format(isr)) 
        
        return isr

    def AFP(self,salary):
        monto= salary * 0.0287
        return float("{:.2f}".format(monto)) 
    

    def SFS(self,salary):
        monto=salary * 0.0304
        return float("{:.2f}".format(monto)) 


    def Total(self,sueldo, afp, sfs, isr):
        monto =sueldo - afp - sfs - isr;
        return  float("{:.2f}".format(monto)) 


    def validationInput(self,_number):
        if _number is not None and _number is not '':
                return eval(_number)
        return 0
