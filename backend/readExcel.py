import pandas as pd
def changeToDict(xlsxFile, totalSheets=1):
      
    resultDict = {}
    sheetNames = pd.ExcelFile(xlsxFile).sheet_names #Taking the sheet names from the XLSX file
    
    print(sheetNames)
    for i in range(0, totalSheets):
        dataframe = pd.read_excel(xlsxFile , skiprows=[0], sheet_name=i)#create dataframe from XLSX file
        #remove all the 'Unnamed' columns
        dataframe = dataframe.drop(columns=list(dataframe.filter(regex='Unnamed')))
        tempDict = dataframe.to_dict() #creating a tempDictionary to iterate
        
        dataframeDict = {} #dictionary to store key:value for each table(sheet)
        for key in tempDict:
            # values are stored as list for each table heading as key
            val = list(tempDict.get(key).values()) # values are stored as list for each table heading as key
            
            dataframeDict[key] = val
        # dictionary of dictionary key(sheetname): value(dictionary of table heading to value) 
        resultDict[sheetNames[i]] = dataframeDict 

    return(resultDict)
        
result = changeToDict('testxcl.xlsx', 3)
print(result)

