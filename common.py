class CommonUtil:
    def is_contain(self, str_one, str_two):
        '''
        判断一个字符串是否再另一个字符串中
        str_one:查找的字符串
        str_two:被查找的字符串
        '''
        if str_one in str_two:
            return True