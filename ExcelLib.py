import xlrd
import xlwt

def open_file(path):

    book = xlrd.open_workbook(path)

    # print number of sheets
    print (book.nsheets)

    # print sheet names
    print (book.sheet_names())

    # get the first worksheet
    first_sheet = book.sheet_by_index(0)

    # read a row
    print (first_sheet.row_values(0))

    # read a cell
    cell = first_sheet.cell(0, 0)
    print (cell)
    print (cell.value)

    # read a row slice
    print (first_sheet.row_slice(rowx=0,
                          start_colx=0,
                          end_colx=2))

def write_file(path):
    wb = xlwt.Workbook(encoding="utf-8")
    ws1 = wb.add_sheet('Sheet 1',cell_overwrite_ok=True)
    ws2 = wb.add_sheet('Sheet 2',cell_overwrite_ok=True)
    ws3 = wb.add_sheet('Sheet 3',cell_overwrite_ok=True)
    ws1.row(0).write(0, 'Data written in first cell of first sheet')
    ws1.write(0, 0, 'Data overwritten in the first cell of first sheet')
    ws2.write(0, 0, 'Data written in first cell of second sheet')
    ws3.write(0, 0, 'Data written in first cell of third sheet')
    ws1.write(0, 1, 'Data written in first row,second column of first sheet')
    ws1.row(1).write(1, 'Data written in second row,second column of first sheet')
    var = "Data from variable written in third row,second column of first sheet"
    ws1.row(2).write(1,var)
    wb.save('C:\\Capturas\\' + path +'.xls')




# ----------------------------------------------------------------------
if __name__ == "__main__":
    path = "LIBRO1.xls"
    open_file(path)