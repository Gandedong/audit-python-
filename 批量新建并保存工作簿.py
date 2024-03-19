import xlwings as xw
app = xw.App(visible = True, add_book = False)
for i in range(6):
    workbook = app.books.add()
    workbook.save(f'e:\\file\\test{i}.xlsx')
