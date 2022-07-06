import pandas as pd
import http.client 
conn = http.client.HTTPSConnection("api.pagerduty.com")
df = pd.ExcelFile('./src/caseData.xlsx').parse('Sheet1') #you could add index_col=0 if there's an index
caseIdList=[]
caseIdList.append(df['CaseId'].values[...])
print(caseIdList);
print(abs(int(len(caseIdList[0])/3)))
start = 0;
end = 3;
multiplier = 0;
for count in range(0,int(len(caseIdList[0])/3)+1, 1):
    pLoad = '{"incidents": ['
    #start = int(len(caseIdList[0])/250)
    if end > int(len(caseIdList[0])):
        end = int(len(caseIdList[0]))
    multipler = multiplier+1;
    print(start, end);
    for caseId in range(start, end, 1):
        pLoad=pLoad + '{"id":"' +str(caseIdList[0][caseId])+ '","type": "incident_reference","status": "resolved"}'
        if caseIdList[0][end-1] != caseIdList[0][caseId]:
            pLoad=pLoad + ','
            #pLoad = pLoad + str(caseId) + ','
    pLoad = pLoad + ']}'
    print(pLoad);
    conn = http.client.HTTPSConnection("api.pagerduty.com")
    payload = pLoad 
    headers = {
        'Content-Type': "application/json",
        'Accept': "application/vnd.pagerduty+json;version=2",
        'From': "jnarayan@salesforce.com",
        'Authorization': "Token token=u+Cx2dQFumdMPTAaAbUg"
        }
    conn.request("PUT", "/incidents", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))
    start = end
    end = end+3
    
