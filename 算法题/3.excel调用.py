import  os
pwd = os.path.split(os.path.abspath(__file__))[0] #获取当前文件夹
print(pwd)
import xlwings as xw
app=xw.App(visible=True,add_book=False)
wb=app.books.add()
# wb就是新建的工作簿(workbook)，下面则对wb的sheet1的A1单元格赋值
rng = wb.sheets['sheet1'].range('A1:C3')
rng.value = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rng.color = (255,0,0) #红色
rng1 = wb.sheets['sheet1'].range('C4')
rng1.formula = '=sum(A1:C3)'
wb.save(f'{pwd}/homework-3.xlsx')
wb.close()
app.quit()