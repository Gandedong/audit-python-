import xlwings as xw
app = xw.App(visible = False, add_book = False)
workbook = app.books.open('e:\\table\\统计表.xlsx')
worksheets = workbook.sheets
for i in range(len(worksheets))[:5]:
    worksheets[i].name = worksheets[i].name.replace('销售', '')
workbook.save('e:\\table\\统计表1.xlsx')
app.quit()