import pandas as pd
import http.client 
conn = http.client.HTTPSConnection("api.pagerduty.com")
df = pd.ExcelFile('./src/caseData.xlsx').parse('Sheet1') #you could add index_col=0 if there's an index
caseIdList=[]
caseIdList.append(df['CaseId'].values[...])
print(caseIdList);
pLoad = '{"incidents": ['
for caseId in caseIdList[0]:
    pLoad=pLoad + '{"id":"' +str(caseId)+ '","type": "incident_reference","status": "resolved"}'
    if caseIdList[0][-1] != caseId:
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