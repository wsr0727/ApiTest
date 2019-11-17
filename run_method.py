import requests
import json


class RunMethod:
    def post_main(self, url, data, header=None):
        res = None # 接口最开始等于none

        if header != None:
            res = requests.post(url=url, data=data, header=header).json()
        else:
            res = requests.post(url=url, data=data).json()
        return res.json()

    def get_main(self, url, data=None, header=None):

        res = None
        if header != None:
            res = requests.get(url=url, data=data, headers=header). json()
        else:
            res = requests.get(url=url, data=data).json()
        return res.json()

    def run_main(self, method, url, data, header):
        res = None
        if method == 'POST':
            res = self.post_main(url, data, header)
        else:
            res = self.get_main(url, data, header)
        return json.dumps(res, ensure_ascit=False, sort_key=True, indent=2)