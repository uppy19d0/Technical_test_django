from django.shortcuts import render

from salary_module.utils.salaryTool import SalaryTool
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

salarytoool = SalaryTool()

@csrf_exempt
def calculator(request):
    afp = ''
    isr = ''
    sfs = ''

    _salary =0
    _bonificacion=0
    _hoursExtra=0
    Total=0;
    try:
        if request.method == "POST":
            _salary = salarytoool.validationInput(request.POST.get('salary'))
            _bonificacion =  salarytoool.validationInput(request.POST.get('bono'))
            _hoursExtra =  salarytoool.validationInput(request.POST.get('hours'))
            totalSalary =_salary+_bonificacion+_hoursExtra

            afp = salarytoool.AFP(totalSalary)
            sfs = salarytoool.SFS(totalSalary)
            isr = salarytoool.ISR(totalSalary-afp-sfs)
            Total=salarytoool.Total(totalSalary,afp,sfs,isr)
            
    except ValueError:
        print(ValueError)
        c = "Invalid calculator"
    return render(request, "calculator.html", {'isr': isr, 'afp': afp, 'sfs': sfs,'Total':Total})

