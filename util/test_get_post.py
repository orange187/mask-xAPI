import requests

#封装post、get方法
class Runmain:

    def send_post(self,url,data,headers,verify):
        response = requests.request("post",url=url,data=data,headers=headers).json()
        return response
        # return json.dumps(response,sort_keys=True,indent=4)

    def send_get(self,url,params,headers,verify):
        response = requests.get(url=url,params=params,headers=headers).json()
        return response
        # return json.dumps(response,sort_keys=True,indent=4)

    def send_put(self,url,data,headers,verify):
        response = requests.request("put", url=url, data=data, headers=headers).json()
        return response
        # return json.dumps(response,sort_keys=True,indent=4)

    def send_del(self,url,data,headers,verify):
        response = requests.request("DELETE", url=url,data=data, headers=headers).json()
        return response
        # return json.dumps(response,sort_keys=True,indent=4



    def run_main(self,url,params,data,headers,method):
        respose = None
        if method == 'GET':
            respose = self.send_get(url,params,headers)
        elif method == 'POST':
            respose = self.send_post(url,data,headers)
        elif method == 'PUT':
            respose = self.send_put(url, data, headers)
        else:
            respose = self.send_del(url,data,headers)
        return respose


