import sys
sys.path.append(r'C:\Users\Gatorix\Documents\SeleniumPractice')
sys.path.append(r'\\mac\Home\Documents\SeleniumPractice')
from key_words.action_method import ActionMethod
from util.excel_util import ExcelUtil
from pprint import isreadable


class KeyWordsCase():
    def run_main(self):
        self.action_method = ActionMethod()
        handle_excel = ExcelUtil()
        case_lines = handle_excel.get_lines()
        if case_lines:
            for i in range(1, case_lines):
                is_run = handle_excel.get_col_value(i, 3)
                if is_run == 'yes':
                    method = handle_excel.get_col_value(i, 4)
                    send_value = handle_excel.get_col_value(i, 5)
                    op_element = handle_excel.get_col_value(i, 6)
                    except_result_method = handle_excel.get_col_value(i, 7)
                    except_result = handle_excel.get_col_value(i, 8)
                    self.run_method(method,send_value,op_element)
                    if except_result!='':
                        except_value=self.get_except_result_value(except_result)
                        if except_value[0]=='text':
                            result=self.run_method(except_result_method)
                            if except_value[1] in result:
                                handle_excel.write_vlaue(i,'pass')
                            else:
                                handle_excel.write_value(i,'fail')
                        elif except_value[0]=='element':
                            self.run_method(except_result_method,except_value[1])
                            if result:
                                handle_excel.write_vlaue(i,'pass')
                            else:
                                handle_excel.write_value(i,'fail')

    def get_except_result_value(self,data):
        return data.split('=')
    def run_method(self, method, send_value='', handle_value=''):
        method_value = getattr(self.action_method, method)
        if send_value:
            method_value(send_value, handle_value)
        elif send_value=='' and handle_value!='':
            method_value(handle_value)
        else:
            method_value()


if __name__ == '__main__':
    test = KeyWordsCase()
    test.run_main()
