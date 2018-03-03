import xlrd
import sqlite3

conn = sqlite3.connect('C:\\Users\\cepl-pc\\Downloads\\svp.db')
c = conn.cursor()

book = xlrd.open_workbook("C:\\Users\\cepl-pc\\Desktop\\svp_database.xls")
first_sheet = book.sheet_by_index(0)
n = int(first_sheet.nrows)

for i in range(1,n):
    cell0 = first_sheet.cell(i,0).value
    
    c.execute('SELECT ID FROM sections where SECTION_NAME="' + cell0 + '"')
    data = c.fetchone()
    if data:
        section_id = data[0]
    else:
        c.execute('INSERT INTO sections ("SECTION_NAME") VALUES ("'+ cell0 +'")')
        c.execute('SELECT ID FROM sections where SECTION_NAME="' + cell0 + '"')
        section_id = c.fetchone()[0]
    
    cell0 = first_sheet.cell(i,1).value
    c.execute('SELECT ID FROM sub_section where SUB_SECTION_NAME="' + cell0 + '"')
    data = c.fetchone()
    if data:
        sub_section_id = data[0]
    else:
        c.execute('INSERT INTO sub_section ("SECTION_ID","SUB_SECTION_NAME") VALUES ({}, "{}")'.format(section_id, cell0))
        c.execute('SELECT ID FROM sub_section where SUB_SECTION_NAME="' + cell0 + '"')
        sub_section_id = c.fetchone()[0]
    
    cell1 = first_sheet.cell(i,2).value
    cell2 = first_sheet.cell(i,3).value
    c.execute('INSERT INTO questions ("QUESTION_DETAIL","DIFFICULTY_LEVEL","SECTION_ID","SUB_SECTION_ID") VALUES ("{}","{}",{},{})'.format(cell1, cell2, section_id, sub_section_id))
    
    c.execute('SELECT ID FROM questions where QUESTION_DETAIL="' + cell1 + '"')
    qid = c.fetchone()[0]
    
    cell1 = first_sheet.cell(i,4).value
    cell2 = first_sheet.cell(i,5).value
    cell3 = first_sheet.cell(i,6).value
    cell4 = first_sheet.cell(i,7).value
    
    c.execute('INSERT INTO options ("QUESTION_ID","OPTION1","OPTION2","OPTION3","OPTION4") VALUES ({},"{}","{}","{}","{}")'.format(qid, cell1, cell2, cell3, cell4))
    
    cell1 = int(first_sheet.cell(i,8).value)
    cell2 = first_sheet.cell(i,9).value
    
    c.execute('INSERT INTO answers ("ANSWER","ANSWER_DESCRIPTION","QUESTION_ID") VALUES ("{}","{}",{})'.format(cell1, cell2, qid))
    conn.commit()