# from asyncio.windows_events import NULL

class SalaryTool:

    def ISR(self,salary):
        isr = 0
        sueldoAnual = salary * 12

        if (sueldoAnual < 416220.00):
            isr = 0
        elif sueldoAnual > 416220.01 and sueldoAnual < 624329.00:
            isr = (sueldoAnual - 416220.01) * 0.15

        elif sueldoAnual > 624329.01 and sueldoAnual < 867123.00:
            isr = (sueldoAnual - 624329.01) * 0.2 + 31216.00
        elif sueldoAnual > 867123.00:
            isr = (sueldoAnual - 867123.01) * 0.25 + 79776.00

        mensual = isr / 12

        mensual=float("{:.2f}".format(mensual)) 

        return mensual
        # return eval(mensual)

    def AFP(self,salary):
        monto= salary * 0.0287
        # montoAFP=format(monto, ".2f")
        # return eval(montoAFP)
        return float("{:.2f}".format(monto)) 
    

    def SFS(self,salary):
        monto=salary * 0.0304
        # montoSFS= format(monto, ".2f")
        # return eval(montoSFS)
        return float("{:.2f}".format(monto)) 


    def Total(self,sueldo, afp, sfs, isr):
        monto =sueldo - afp - sfs - isr;
        return  float("{:.2f}".format(monto)) 

    def validationInput(self,_number):
        if _number is not None and _number is not '':
                return eval(_number)
        return 0
