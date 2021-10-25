#!/usr/bin/python3
# coding=utf-8
import xlrd
from Lib.PyLib3 import Base

class Excel:

    # 传入参数是Excel的文件路径
    def __init__(self, filepath):
        self.sheet = None
        self.base = Base()

        if not self.base.is_file_exist(filepath):
            raise Exception('file not found.')
        try:
            self.xlsdata = xlrd.open_workbook(filepath)
            self.sheets = self.xlsdata.sheets()
        except Exception as e:
            raise e

    # 传入sheets和工作簿的名称
    # 返回指定工作簿
    @staticmethod
    def get_sheet_by_name(self, sheetname):
        for s in self.sheets:
            if s.name == sheetname:
                self.sheet = s
                return self.sheet
        return self.sheet

    # 传入sheets和工作簿的索引位置, 从0开始
    # 返回指定工作簿
    @staticmethod
    def get_sheet_by_index(self, index):
        sheet = self.sheets[index]
        if sheet:
            return sheet
        else:
            raise Exception('工作簿未找到')

    # 传入sheet和要获取的行的值
    # 返回指定sheet内, 某行的值
    @staticmethod
    def get_row_data_from_sheet(sheet, rownumber):
        rowdata = sheet.row_values(rownumber)
        if rowdata:
            return rowdata
        else:
            # raise Exception('行数据未找到')
            rowdata = None
            return rowdata

    # 传入sheet和要获取的列的值
    # 返回指定sheet内, 某列的值
    @staticmethod
    def get_col_data_from_sheet(sheet, colnumber):
        coldata = sheet.col_values(colnumber)
        if coldata:
            return coldata
        else:
            raise Exception('行数据未找到')

    # 输入sheet
    # 返回sheet的行数
    @staticmethod
    def get_sheet_row_numer(sheet):
        nrows = sheet.nrows
        return nrows

    # 输入sheet
    # 返回sheet的列数
    @staticmethod
    def get_sheet_col_numer(sheet):
        ncols = sheet.ncols
        return ncols

    # 输入sheet, cell的行坐标与列坐标
    # 返回cell的值
    @staticmethod
    def get_cell_value(sheet, m, n):
        try:
            cellvalue = sheet.cell(m, n).value
            # sheet.cell(1,0).value.encode('utf-8')
            # sheet.cell_value(1,0).encode('utf-8')
            # sheet.row(1)[0].value.encode('utf-8')
            return cellvalue
        except Exception as e:
            raise e
