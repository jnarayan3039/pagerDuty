import pandas as pd
import http.client 
conn = http.client.HTTPSConnection("api.pagerduty.com")
df = pd.ExcelFile('./src/caseData.xlsx').parse('Sheet1') #you could add index_col=0 if there's an index
caseIdList=[]
caseIdList.append(df['CaseId'].values[...])
print(caseIdList);
pLoad = "{'incidents': ["
for caseId in caseIdList[0]:
    pLoad=pLoad + "{'id':" +str(caseId)+ "'status': 'closed'},"
    #pLoad = pLoad + str(caseId) + ','
pLoad = pLoad + "]}"
print(pLoad);
conn = http.client.HTTPSConnection("api.pagerduty.com")
payload = "{\n  \"incidents\": [\n    {\n      \"id\": \"PT4KHLK\",\n      \"type\": \"incident_reference\",\n      \"status\": \"acknowledged\"\n    },\n    {\n      \"id\": \"PQMF62U\",\n      \"type\": \"incident_reference\",\n      \"priority\": {\n        \"id\": \"P53ZZH5\",\n        \"type\": \"priority_reference\"\n      }\n    },\n    {\n      \"id\": \"PPVZH9X\",\n      \"type\": \"incident_reference\",\n      \"status\": \"resolved\"\n    },\n    {\n      \"id\": \"P8JOGX7\",\n      \"type\": \"incident_reference\",\n      \"assignments\": [\n        {\n          \"assignee\": {\n            \"id\": \"PXPGF42\",\n            \"type\": \"user_reference\"\n          }\n        }\n      ]\n    }\n  ]\n}"
headers = {
    'Content-Type': "application/json",
    'Accept': "application/vnd.pagerduty+json;version=2",
    'From': "",
    'Authorization': "Token token=y_NbAkKc66ryYTWUXYEu"
    }
conn.request("PUT", "/incidents", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))