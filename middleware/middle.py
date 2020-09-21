from django.utils.deprecation import MiddlewareMixin


class middle(MiddlewareMixin):
    # def process_request(self, request):
    # ip = request.META.get("REMOTE_ADDR")
    # print(ip)
    # tuple_dict = request.META.items()  # 将字典转换成可遍历的元组。
    # for k, v in tuple_dict:
    #         print(k,v)
    # print(settings)
    # if request.path != '/work2/login/' and request.path !='/work2/check_name/' and request.path !='/work2/register/' and request.path !='/work2/check_login/':
    #     if request.session.get('username',None):
    #         pass
    #     else:
    #         return HttpResponseRedirect('/work2/login/')

    def process_respose(self, request, response):
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "*"
        # if request.path == '/work2/logout/':
        #     request['sess']
