from django.shortcuts import render
from django.views.generic import View


class IndexView(View):
    template_name = 'SampleCounter/index.html'

    # defines pictures for the landing page
    links = ["https://cdn.pixabay.com/photo/2015/03/26/10/07/young-690958_1280.jpg",
             "https://cdn.pixabay.com/photo/2018/03/06/22/57/portrait-3204843_960_720.jpg",
             "https://cdn.pixabay.com/photo/2016/11/23/15/26/fashion-1853507_960_720.jpg",
             "https://cdn.pixabay.com/photo/2017/07/31/14/55/black-and-white-2558273_960_720.jpg"
             ]

    def post(self, request):
        pass

    def get(self, request):
        return render(request, self.template_name, {'links': self.links})
