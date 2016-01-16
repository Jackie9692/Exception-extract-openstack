# -*- coding:utf-8 -*-
import os
import time
import xlwt

def change_file(path):
    if not os.path.isdir(path) and not os.path.isfile(path):
        return False
    if os.path.isfile(path):
        file_path = os.path.split(path) 
        lists = file_path[1].split('.') 
        
        file_ext = lists[-1] 
        py_ext = ['py']
        if file_ext in py_ext:
            searchFile(path)

    elif os.path.isdir(path):
        for x in os.listdir(path):
            change_file(os.path.join(path,x))




def searchFile(filePath):
    #needed message
    fileName = filePath[20:]
#     fileName = ''.join(fileName)
    
    global resultListEach
    global resultList    
    funcName = ""
    raiseType = ""
    raiseMsg = ""
    global raiseNum
    file = open(filePath)
    while True:
        lines = file.readlines()
        
        if not lines:#line can't be null
            break
         
        lineRow = 0
        for line in lines:
            
            if line.strip() == "":
                continue
            lineStrip = line.strip()
            lineList = lineStrip.split(" ")
            if lineList[0] == "def":
                funcName = lineList[1].split("(")[0]
            elif lineList[0] == "raise":
                if len(lineList) >= 2:
                    if '(' in lineList[1]:
                        msgLeftBound = lineStrip.split("(")[1]
                        raiseTypeMore = lineStrip.split("(")[0]
                        raiseType = raiseTypeMore.split(" ")[-1]
                        if ')' in line:
                            raiseMsg = msgLeftBound.strip().split(")")[0]
                        else:
                            raiseMsg = ""
                            
                            tempLineStart = lineRow + 1
                            while True:
                                if(tempLineStart == len(lines)):
                                    break
                                if ")" in lines[tempLineStart]:
                                    raiseMsg = raiseMsg + lines[tempLineStart].strip().split(")")[0]
                                    break
                                else:
                                    raiseMsg = raiseMsg + lines[tempLineStart].strip()
                                    tempLineStart = tempLineStart + 1
                                    
                    else:
                        raiseType = lineList[1]
                    if raiseMsg != "":
                        if raiseMsg[0] == "'" or raiseMsg[0] == '"':
                            raiseMsg = raiseMsg[1:-1]
#                     print "fileName:%s;lineRow:%s;functionname:%s; RaiseType:%s; RaiseMsg:%s" %(fileName, lineRow, funcName, raiseType, raiseMsg)
                    resultListEach.append(raiseType)
                    resultListEach.append(raiseMsg)
                    resultListEach.append(fileName)
                    resultListEach.append(funcName)
                    resultList.append(resultListEach)
                    resultListEach = []
                    raiseType = ""
                    raiseMsg = ""
                    raiseNum = raiseNum + 1;   
            else:
                pass
            lineRow = lineRow + 1; 
            
    file.close()

def  writeExcel(targetData):
    style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on', num_format_str='#,##0.00')
    style1 = xlwt.easyxf('font: name Times New Roman, color-index black, bold on', num_format_str='#,##0.00')
    wb = xlwt.Workbook()
    ws = wb.add_sheet('Exception 1')
    
    row = 0
    ws.write(row, 0, "异常类型".decode("utf-8"), style0)
    ws.write(row, 1, "异常具体描述".decode("utf-8"), style0)
    ws.write(row, 2, "异常所在文件".decode("utf-8"), style0)
    ws.write(row, 3, "异常所在函数".decode("utf-8"), style0)
    row = row + 1
    for targetRow in targetData:
        col = 0
        for targetCell in targetRow:
#             print "row:%s ; col:%s" %(row, col)
            ws.write(row, col, targetCell.decode("utf-8"), style1)
            col = col + 1
        row = row + 1;
        
    wb.save("D:\openstack服务端错误行为特征1.xls".decode("utf-8"))    
    


    
    
            
if __name__ == "__main__":
    raiseNum = 0 
    resultListEach = []
    resultList = []            
    py_dir = 'D:\lab\dist-packages'
    start = time.time()
    change_file(py_dir)
    writeExcel(resultList)
    c = time.time() - start
    print('所用时间:%0.2f'%(c))
    print('总计异常数量:%d'%(raiseNum))
    
    
    
    
    
    
    
    
