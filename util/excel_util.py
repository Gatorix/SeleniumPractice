import xlrd
from xlutils.copy import copy


class ExcelUtil():
    def __init__(self, excel_path=None, index=None) -> None:
        if excel_path == None:
            excel_path = r'\\mac\Home\Documents\SeleniumPractice\config\case.xls'
        if index == None:
            index = 0
        self.book = xlrd.open_workbook(excel_path)
        self.table = self.book.sheets()[index]
        # self.rows = self.table.nrows

    def get_data(self):
        case = []
        rows = self.get_lines()
        if rows != None:
            for i in range(rows):
                col = self.table.row_values(i)
                case.append(col)
            return case
        return None

    # 获取行数
    def get_lines(self):
        if self.table.nrows >= 1:
            return self.table.nrows
        else:
            return None

    # 获取单元格数据
    def get_col_value(self, row, col):
        if self.get_lines() > row:
            return self.table.cell(row, col).value
        return None
    # 写入数据

    def write_value(self, row, col, value):
        read_value = self.book
        write_data = copy(read_value)
        print(type(write_data))
        write_data.get_sheet(0).write(row, col, value)
        write_data.save(
            r'\\mac\Home\Documents\SeleniumPractice\config\case.xls')


if __name__ == '__main__':
    exc = ExcelUtil()
    # exc.get_data()
    print(exc.get_col_value(999,1))
    # exc.write_value(8,8,'test')
