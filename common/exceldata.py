import xlrd,os
import sys
sys.path.append("../page_object")
from common.function import project_path
#读excel操作、所有数据存放字典中
#filename为文件名
#index为excel sheet工作簿索引
def read_excel(filename,index):
    xls = xlrd.open_workbook(filename)
    sheet = xls.sheet_by_index(index)
    dic={}
    for j in range(sheet.ncols):
        data=[]
        for i in range(sheet.nrows):
          data.append(sheet.row_values(i)[j])
        dic[j]=data
    return  dic

if __name__ == '__main__':
    #读取excel操作，返回字典
    data = read_excel(project_path()+"/data/testdata.xlsx",1)
    print(data)
    print(data.get(1))
    print(data[0][1],data[1][1])
