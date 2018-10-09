def checkData(data):
# delete workclass,education,capital gain,capital loss,country
    figure = pl.figure(figsize=(50,300))

    for i, eachColumn in enumerate(data.columns):
        axData = figure.add_subplot(8,2,i+1)
        axData.set_title(eachColumn)
        for item in ([axData.title, axData.xaxis.label, axData.yaxis.label]+axData.get_xticklabels()+axData.get_yticklabels()):
            item.set_fontsize(60)
        
        if data.dtypes[eachColumn] == np.object:
            data[eachColumn].value_counts().plot(kind="bar", axes=axData)
        else:
            data[eachColumn].hist(axes=axData)
            pl.xticks(rotation="vertical")
    pl.subplots_adjust(hspace=0.7, wspace=0.2)
def deleteUselessColumn(data):
    del data["Workclass"]
    del data["Education"]
    del data["Capital Gain"]
    del data["Capital Loss"]
    del data["Country"]
    return data
def dataEncode(data):
    encodedData = {}
    data_copy = data.copy()
    for eachColumn in data_copy.columns:
        if data_copy.dtypes[eachColumn] == np.object:
            encodedData[eachColumn] = preprocessing.LabelEncoder()
            data_copy[eachColumn] = encodedData[eachColumn].fit_transform(data_copy[eachColumn])
    return data_copy
def checkNaN(data):
    print(np.sum(data.isnull()))
def deleteNaNRow(data):
    data = data.dropna()
    return data
# usage:
# a = deleteUselessColumn(df_train)
# b = deleteNaNRow(a)   
# c= dataEncode(b)
