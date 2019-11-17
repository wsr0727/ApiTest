from operation_excel import OperationExcel
import data_config
from operation_json import OperationJson


class GetData:
    def __init__(self):
        self. opera_excel = OperationExcel()
        self.flag = None
        self.opera_json = OperationJson()
    # 用于获取excel行数，就是我们的case个数
    def get_case_lines(self):
        return self.opera_excel.get_lines()

    # 获取是否执行
    def get_is_run(self, row):
        # flag = None 试试在构造函数里新建flag变量
        col = int(data_config.get_run())
        run_model = self.opera_excel.get_cell_value(row, col)
        if run_model == 'yes':
            flag = True
        else:
            flag = False
        return flag

    # 是否携带header
    def is_header(self, row):
        col = int(data_config.get_header())
        header = self.opera_excel.get_cell_value(row, col)
        if header == 'yes':
            return 'header'
        else:
            return None

    # 获取请求方式
    def get_request_method(self, row):
        col = int(data_config.get_request_way())
        request_method = self.opera_excel.get_cell_value(row, col)
        return request_method

    # 获取URL
    def get_request_url(self, row):
        col = int(data_config.get_url())
        url = self.opera_excel.get_cell_value(row, col)
        return url

    # 获取请求数据
    def get_request_data(self, row):
        col = int(data_config.get_data())
        data = self.opera_excel.get_cell_value(row, col)
        if data == '':
            return '没有data'
        return data

    # 通过获取关键字拿到data数据
    def get_data_for_json(self,row):
        opera_json = OperationJson()
        id = self.get_request_data(row)
        request_data = opera_json.get_data(id)
        return request_data

    # 获取预期结果
    def get_expect_data(self, row):
        col = int(data_config.get_expect())
        expect = self.opera_excel.get_cell_value(row, col)
        if expect == '':
            return None
        return expect


