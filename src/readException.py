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
#     file = open(r'D:\lab\dist-packages\twisted\python\hook.py')
    while True:
        lines = file.readlines()
        if not lines:#line can't be null
            break
        lineRow = 0
        for line in lines:
            if line.strip() == "":
                lineRow = lineRow + 1; 
                continue
            lineStrip = line.strip()
            lineList = lineStrip.split(" ")
            if lineList[0] == "def":
                funcName = lineList[1].split("(")[0]
            elif lineList[0] == "raise":
                if len(lineList) >= 2:
                    if '(' in lineList[1]:
                        labelNum = 1;
                        
                        msgLeftBound = lineStrip.split("(")[1]
                        raiseTypeMore = lineStrip.split("(")[0]
                        raiseType = raiseTypeMore.split(" ")[-1]
                        
                        raiseMsg = msgLeftBound.strip().split(")")[0]
                        if ')' in line:
                            pass
                        else:
                            tempLineStart = lineRow
                            while True:
                                tempLineStart += 1
                                if(tempLineStart == len(lines)):
                                    break
                                labelLine = lines[tempLineStart].strip()
                                
                                for char in labelLine:
                                        if char == '(' :
                                            labelNum += 1
                                        elif char == ')':
                                            labelNum = labelNum - 1
                                        else:
                                            pass
                                        if labelNum == 0:
                                            break
                                        else:
                                            raiseMsg = raiseMsg + char          
                                if labelNum == 0:
                                    break
                    else:
                        raiseType = lineList[1]
                    if raiseMsg != "":
                        if len(raiseMsg) > 2:
                            if raiseMsg[0] == "'" and raiseMsg[-1] == "'":
                                raiseMsg = raiseMsg[1:-1]
                            if raiseMsg[0] == '"' and raiseMsg[-1] == '"':
                                raiseMsg = raiseMsg[1:-1]
                    if len(raiseMsg)>1200:
                        print "fileName:%s;lineRow:%s;functionname:%s; RaiseType:%s; RaiseMsg:%s" %(fileName, lineRow, funcName, raiseType, raiseMsg)
                    
                    if raiseMsg == "msg":
                        tempMsg = msgOrExpl("msg", lineRow, lines); 
                        if tempMsg !="":
                            raiseMsg =raiseMsg.replace("msg", tempMsg)
                            print raiseMsg                     
                    if raiseMsg.find("msg")!=-1:
                        print raiseMsg + ":::"
                        index = raiseMsg.find("msg")
                        if index >= 1:#msg不在首位  ,msg |=msg
                            if raiseMsg[index-1] == ',' or raiseMsg[index-1] == '=':
                                tempMsg = msgOrExpl("msg", lineRow, lines);
                                if tempMsg !="":
                                    raiseMsg =raiseMsg.replace("msg", tempMsg)
                                    print raiseMsg 
                        else:
                            if index+3 < len(raiseMsg): #msg, 
                                if raiseMsg[index+3] == ',':
                                    tempMsg = msgOrExpl("msg", lineRow, lines);
                                    if tempMsg !="":
                                        raiseMsg =raiseMsg.replace("msg,", tempMsg+",")
                                        print raiseMsg
                            elif index+3 == len(raiseMsg):#msg
                                tempMsg = msgOrExpl("msg", lineRow, lines);
                                if tempMsg !="":
                                    raiseMsg =raiseMsg.replace("msg", tempMsg)
                                    print raiseMsg                                
                        
                    if raiseMsg.find("explanation=expl")!=-1:
                        if raiseMsg[-5:] == "=expl":
                            tempExple = msgOrExpl("expl", lineRow, lines);  
                            raiseMsg = raiseMsg.replace("=expl", tempExple)
                            print raiseMsg 
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

def msgOrExpl(type, lineRow, lines):
    global msgNum, explNum
    
    if type == "msg":
        msgNum += 1
    elif type == "expl":
        explNum +=1
    else:
        return "";

    
    findMsgInfoStart = lineRow
    tempMsg = "" #临时msg信息
    while True:
        if lineRow - findMsgInfoStart > 10:#超过10行未找到 "msg = "
            break
        
        findMsgInfoStart -= 1
        if(findMsgInfoStart == len(lines)):
            break
        msgLabelLine = lines[findMsgInfoStart].strip()
        
        if msgLabelLine.find(type + " = ") != -1:#找到msg信息
            tempMsg = ""
            if(msgLabelLine == 'msg = (_("Unsupported backup metadata version (%s)") % (version))'):
                pass
            if msgLabelLine.find("(") != -1:
                findedMsgInfoStart = findMsgInfoStart
                msgLabelNum = 0  
                breakFlag = False  
                while True:
                    if findedMsgInfoStart - findMsgInfoStart > 10:#超过10行 停止寻找"msg = "
                        break
                    msgLabelLine = lines[findedMsgInfoStart].strip()
                    tempMsg +=  msgLabelLine
                    
                    for char in msgLabelLine:
                        if char == '(' :
                            msgLabelNum += 1
                        elif char == ')':
                            breakFlag = True
                            msgLabelNum -= 1
                        else:
                            pass
                        if msgLabelNum == 0:
                            if breakFlag:
                                break
                    if msgLabelNum == 0:
                        break                                                        
                    findedMsgInfoStart += 1
                    if(findedMsgInfoStart == len(lines)):
                        break
            else:
                tempMsg = msgLabelLine
            break
    return tempMsg[5:]                                        

def  writeExcel(targetData):
    print "writing excel"
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
        
    wb.save("D:\openstack服务异常统计1.xls".decode("utf-8"))    
    
            
if __name__ == "__main__":
    msgNum = 0
    explNum = 0
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
    print('msg:%d'%(msgNum))
    print('expl:%d'%(explNum))
    
    
    
    
    
    
    
    
