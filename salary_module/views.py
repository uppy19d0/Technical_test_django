from django.shortcuts import render

from salary_module.utils.salaryTool import SalaryTool
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

salarytoool = SalaryTool()

@csrf_exempt
def calculator(request):
    # afp = ''
    # isr = ''
    # sfs = ''
    afpSalary =''
    sfsSalary = ''
    isrSalary =''

    _salary =0
    _bonificacion=0
    _hoursExtra=0
    Total=0;
    try:
        if request.method == "POST":
            _salary = salarytoool.validationInput(request.POST.get('salary'))
            _bonus =  salarytoool.validationInput(request.POST.get('bono'))
            _extraHours =  salarytoool.validationInput(request.POST.get('hours'))
            
            totalIncome = _salary + _bonus + _extraHours

            withoutExtra = _salary + _bonus

            afpTotal = salarytoool.AFP(withoutExtra)
            sfsTotal = salarytoool.SFS(withoutExtra)
            isrTotal = salarytoool.ISR(totalIncome-afpTotal-sfsTotal)
            Total=salarytoool.Total(totalIncome,afpTotal,sfsTotal,isrTotal)
            
    except ValueError:
        print(ValueError)
        c = "Invalid calculator"
    return render(request, "calculator.html", {'isr': isrTotal, 'afp': afpTotal, 'sfs': sfsTotal,'Total':Total})

