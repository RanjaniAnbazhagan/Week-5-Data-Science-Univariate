class Univariate():
    def quanqual(dataset):
        qual=[]
        quan=[]
        for columnName in dataset.columns:
            if (dataset[columnName].dtype=='O'):
                qual.append(columnName)
            else:
                quan.append(columnName)
        return quan,qual
    def centraltendency(columnName,dataset):
        quanqual(dataset)
        descriptive=pd.DataFrame(index=["mean","median","mode"],columns=quan)
        for columnName in quan:
            descriptive[columnName]["mean"]=dataset[columnName].mean()
            descriptive[columnName]["median"]=dataset[columnName].median()
            descriptive[columnName]["mode"]=dataset[columnName].mode()[0]
        return descriptive
    def percentile(columnName,dataset):
        quanqual(dataset)
        descriptive=pd.DataFrame(index=["mean","median","mode","Q1:25%","Q2:50%","Q3:75%","99","Q4:100%"],columns=quan)
        for columnName in quan:
            descriptive[columnName]["mean"]=dataset[columnName].mean()
            descriptive[columnName]["median"]=dataset[columnName].median()
            descriptive[columnName]["mode"]=dataset[columnName].mode()[0]
            descriptive[columnName]["Q1:25%"]=dataset.describe()[columnName]["25%"]
            descriptive[columnName]["Q2:50%"]=dataset.describe()[columnName]["50%"]
            descriptive[columnName]["Q3:75%"]=dataset.describe()[columnName]["75%"]
            descriptive[columnName]["99"]=np.percentile(dataset[columnName],99)
            descriptive[columnName]["Q4:100%"]=dataset.describe()[columnName]["max"]
        return descriptive
    def iqr(columnName,dataset): 
        descriptive=pd.DataFrame(index=["mean","median","mode","Q1:25%","Q2:50%","Q3:75%","99","Q4:100%","IQR","1.5rule","Lesser","Greater","Min","Max"],columns=quan)
        for columnName in quan:
            descriptive[columnName]["mean"]=dataset[columnName].mean()
            descriptive[columnName]["median"]=dataset[columnName].median()
            descriptive[columnName]["mode"]=dataset[columnName].mode()[0]
            descriptive[columnName]["Q1:25%"]=dataset.describe()[columnName]["25%"]
            descriptive[columnName]["Q2:50%"]=dataset.describe()[columnName]["50%"]
            descriptive[columnName]["Q3:75%"]=dataset.describe()[columnName]["75%"]
            descriptive[columnName]["99"]=np.percentile(dataset[columnName],99)
            descriptive[columnName]["Q4:100%"]=dataset.describe()[columnName]["max"]
            descriptive[columnName]["IQR"]=descriptive[columnName]["Q3:75%"]-descriptive[columnName]["Q1:25%"]
            descriptive[columnName]["1.5rule"]=1.5*descriptive[columnName]["IQR"]
            descriptive[columnName]["Lesser"]=descriptive[columnName]["Q1:25%"]-1.5*descriptive[columnName]["IQR"]
            descriptive[columnName]["Greater"]=descriptive[columnName]["Q3:75%"]+1.5*descriptive[columnName]["IQR"]
            descriptive[columnName]["Min"]=dataset[columnName].min()
            descriptive[columnName]["Max"]=dataset[columnName].max()
        return descriptive
    
    def freqTable(columnName,dataset):
        freqTable=pd.DataFrame(columns=["unique_values","Frequency","RelativeFrequency","Cumsum"])
        freqTable["unique_values"]=dataset[columnName].value_counts().index
        freqTable["Frequency"]=dataset[columnName].value_counts().values
        freqTable["RelativeFrequency"]=freqTable["Frequency"]/103
        freqTable["Cumsum"]=freqTable["RelativeFrequency"].cumsum()
        return freqTable
    
    def findoutlier(columnName,dataset):
        lesser=[]
        greater=[]
        quanqual(dataset)
        for colunName in quan:
            if(descriptive[colunName]["Min"]<descriptive[colunName]["Lesser"]):
                lesser.append(colunName)
            if(descriptive[colunName]["Max"]>descriptive[colunName]["Greater"]):
                greater.append(colunName)
        return lesser,greater
    
    def replacingoutlier(columnName,dataset):
        findoutlier(columnName,dataset)
        for columnName in lesser:
            dataset[columnName][dataset[columnName]<descriptive[columnName]["Lesser"]]=descriptive[columnName]["Lesser"]
        for columnName in greater:
            dataset[columnName][dataset[columnName]>descriptive[columnName]["Greater"]]=descriptive[columnName]["Greater"]
        return dataset
    