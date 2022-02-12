import xlrd


class ExcelUtil():
    def __init__(self, excel_path=None, index=None) -> None:
        if excel_path == None:
            excel_path = r'\\mac\Home\Documents\SeleniumPractice\config\case.xls'
        if index == None:
            index = 0
        self.book = xlrd.open_workbook(excel_path)
        self.table = self.book.sheets()[index]
        self.rows=self.table.nrows

    def get_data(self):
        case=[]
        for i in range(self.rows):
            col=self.table.row_values(i)
            case.append(col)
        # print(case)
        return case

# if __name__=='__main__':
#     exc=ExcelUtil()
#     exc.get_data()