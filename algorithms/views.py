from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Type, Algorithm
from algorithms.myclasses.mathematics import MyFibonacci

# def index(request):
#     return HttpResponse("You're looking at algorithm index " )

# def index(request):
#     latest_algorithm_list = Type.objects.order_by('-create_date')[:30]
#     output = ', '.join([x.type_text for x in latest_algorithm_list])
#     return HttpResponse(output)

# def index(request):
#     latest_algorithm_list = Type.objects.order_by('-create_date')[:5]
#     template = loader.get_template('algorithms/index.html')
#     context = {
#         'latest_algorithm_list': latest_algorithm_list,
#     }

#     # output = ', '.join([x.type_text for x in latest_algorithm_list])
#     # print(output)

#     return HttpResponse(template.render(context, request))

class IndexView(generic.ListView):
    template_name = 'algorithms/index.html'
    context_object_name = 'latest_algorithm_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Type.objects.order_by('-create_date')[:5]


# def detail(request, type_id):
#     return HttpResponse("You're looking at algorithm %s." % type_id)

# def detail(request, type_id):
#     try:
#         vm = Type.objects.get(pk=type_id)
#     except Type.DoesNotExist:
#         raise Http404("algorithm type does not exist")
#     return render(request, 'algorithms/detail.html', {'vm': vm})


def detail(request, type_id):
    vm = get_object_or_404(Type, pk=type_id)

    for x in vm.algorithm_set.all():
        print(x.algorithm_text)    

    output = ', '.join([x.algorithm_text for x in vm.algorithm_set.all()])
    print(output)

    return render(request, 'algorithms/detail.html', {'type': vm})

# class DetailView(generic.DetailView):
#     model = Type
#     template_name = 'algorithms/detail.html'


# def result(request, type_id):
#     # response = "You're looking at the results of algorithm %s."
#     # return HttpResponse(response % type_id)
#     vm = get_object_or_404(Type, pk=type_id)
#     return render(request, 'algorithms/result.html', {'vm': vm})

class ResultView(generic.DetailView):
    model = Type
    template_name = 'algorithms/result.html'


def execute(request, type_id):
    vm = get_object_or_404(Type, pk=type_id)

    try:
        selected_algorithm=vm.algorithm_set.get(pk=request.POST['algorithm'])
    #    return HttpResponse("You're executing on algorithm %s." % selected_algorithm.algorithm_text)

    except (KeyError, Algorithm.DoesNotExist):
         return render(request, 'algorithms/detail.html', {
            'vm': vm,
            'error_message': "You didn't select a algorithm.",
        })
    else:
        selected_algorithm.times += 1
        selected_algorithm.save()

        if selected_algorithm.algorithm_text == "Fibonacci":
            mf=MyFibonacci(10)
            selected_algorithm.result = mf.calculate()
            selected_algorithm.save()
        elif selected_algorithm.algorithm_text == "Stack":
            selected_algorithm.result = "Hello Stack"
            selected_algorithm.save()
        else:             
            selected_algorithm.result = "to be implemented"
            selected_algorithm.save()
        
        # Always return an HttpResponseRedirect after successfully dealing with POST data. 
        # This prevents data from being posted twice if a user hits the Back button.
        return HttpResponseRedirect(reverse('algorithms:result', args=(vm.id,)))
        