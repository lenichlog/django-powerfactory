from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from buses.backend.pf import PowerFactory


class IndexView(View):
    template_name = 'buses/index.html'
    context_object_name = 'latest_table'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class TableView(PowerFactory, View):

    def find_buses(self):
        pf_app, _ = self.pf_app()

        wanted_buses = []
        buses = [t for t in pf_app.GetCalcRelevantObjects('ElmTerm') if t.iUsage == 0]
        for bus in buses:
            if len([e for e in bus.GetConnectedElements(1, 1, 0) if e.GetClassName() == 'ElmLne']) > 1:
                # wanted_buses.append(bus.loc_name)
                wanted_buses.append(
                    [bus.loc_name,
                     bus.uknom,
                     [
                      L.loc_name
                      for L in bus.GetConnectedElements(1, 1, 0)
                      if L.GetClassName() == 'ElmLne']
                     ]
                )
        return wanted_buses

    def get(self, request, *args, **kwargs):
        my_data = {}
        elements = self.find_buses()

        my_data['rows'] = [
            {
                'id': i,
                'data': [
                    {'value': el[0], 'image': 'folder.gif'},
                    str(el[1])
                ],
                'rows': [
                    {
                        'id': '{}_{}'.format(i, index),
                        'data': [L, '---']
                    }
                    for index, L in enumerate(el[2])]
            }
            for i, el in enumerate(elements, start=1)
        ]

        return JsonResponse(my_data)
