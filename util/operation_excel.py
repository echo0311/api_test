# -*- coding: utf-8 -*-
import xlrd
from xlutils.copy import copy


class OperationExcel:
    def __init__(self, file_name=None, sheet_id=None):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            self.file_name = '../dataconfig/interface.xls'
            self.sheet_id = 0
        self.table = self.get_tables()

    # 获取表格
    def get_tables(self):
        workbook = xlrd.open_workbook(self.file_name)
        tables = workbook.sheets()[self.sheet_id]
        return tables

    # 获取行数
    def get_lines(self):
        table = self.table
        return table.nrows

    # 获取单元格
    def get_cell_value(self, rowx, colx):
        table = self.table
        return table.cell_value(rowx, colx)

    # 获取某一列的内容
    def get_cols_values(self, col_id=None):
        table = self.table
        if col_id is not None:
            col_value = table.col_values(col_id)
        else:
            col_value = table.col_values(0)
        return col_value

    # 根据行号，找到该行的内容
    def get_row_values(self, rowx):
        table = self.table
        row_value = table.row_values(rowx)
        return row_value

    # 写入数据
    def write_value(self, rowx, colx, value):
        read_data = xlrd.open_workbook(self.file_name)
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(rowx, colx, value)
        write_data.save(self.file_name)

    # 根据对应的caseid 找到对应行的内容
    def get_rows_data(self, case_id):
        row_num = self.get_row_num(case_id)
        row_data = self.get_row_values(row_num)
        return row_data

    # 根据对应的caseid找到对应的行号
    def get_row_num(self, case_id):
        num = 0
        cols_data = self.get_cols_values()   # 默认获取id列
        for col in cols_data:
            if case_id == col:
                return num
            else:
                num += 1


if __name__ == '__main__':
    tables = OperationExcel()
    print(tables.get_cell_value(1, 11))
