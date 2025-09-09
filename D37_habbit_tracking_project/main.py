import requests
import datetime as dt

pixela_endpoint="https://pixe.la/v1/users"

USERNAME="joy666"
TOKEN="fafjdf3regnfkvnosdjffe"
GRAPH_ID="graph1"
# parameters={
#     "token":TOKEN,
#     "username":USERNAME,
#     "agreeTermsOfService":"yes",
#     "notMinor":"yes"
# }
# # Create your user account
# response=requests.post(pixela_endpoint,json=parameters)

#Create a graph definition
headers={
    "X-USER-TOKEN":TOKEN,
}
graph_param={
    "id":GRAPH_ID,
    "name":"my graph",
    "unit":"commit",
    "type":"int",
    "color":"sora"
}
# graph_response=requests.post(f"{pixela_endpoint}/{USERNAME}/graphs",json=graph_param,headers=headers)

# Get the graph!
graph1_response=requests.post(f"{pixela_endpoint}/{USERNAME}/graphs",json=graph_param,headers=headers)

# Post value to the graph
yesterday=dt.datetime(year=2025, month=9, day=8).strftime('%Y%m%d')
current_day=dt.datetime.today().strftime('%Y%m%d') #format date into 20250909

pixel_param={
 "date":yesterday,
"quantity":"10"
}
pixel_create_response=requests.post(f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}", json=pixel_param, headers=headers)
# print(pixel_create_response.text)

#update graph
# update_graph_param={
#     "name":"habit tracking",
#     "color":"momiji"
# }
# update_graph_response=requests.put(url=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}", json=update_graph_param, headers=headers)
# print(update_graph_response.text)

#delete pixel

delete_pixel_response=requests.delete(url=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{current_day}", headers=headers)
print(delete_pixel_response.text)