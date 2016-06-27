import requests
import json

count =0
access_token = 'EAAM39GiUIEwBAGZA88ZBSbamEy4WcxrjWMdEek2sl98WekVicuR2gULXVfRh9LYNhGfGW1aaP600ce4Xr6XmymDm5B2h3mttqqcuX09DvSliKeKrZCznOg2Ud9Jx6AVtkFZBwaMrHLQ2EmiCMSZCMTUWpojTaLjwZD'
  

def decline(burl_declined):
	results = requests.get(burl_declined)
	request_text = results.text
	results_json = json.loads(request_text)
	for item in results_json['data']:
		print item['name']
		print item['id']
		print ''
		global count
		count = count+1
	try:
		paging_object = results_json['paging']
		next_base_url = paging_object['next']
		search(next_base_url)
	except:
		print ''
	else:
		print ''
event_id='1742982225949209'
burl_declined='https://graph.facebook.com/v2.3/'+event_id+'/declined?access_token='+access_token
decline(burl_declined)
print 'These people declined it'
print count

def attend(burl_attending):
	results = requests.get(burl_attending)
	request_text = results.text
	results_json = json.loads(request_text)
	for item in results_json['data']:
		print item['name']
		print item['id']
		print ''
		global count
		count = count+1
	try:
		paging_object = results_json['paging']
		next_base_url = paging_object['next']
		search(next_base_url)
	except:
		print ''
	else:
		print ''
event_id='1742982225949209'
burl_attending='https://graph.facebook.com/v2.3/'+event_id+'/attending?access_token='+access_token
attend(burl_attending)
print 'These people attending it'
print count




def maybe_ppl(burl_maybe):
	results = requests.get(burl_maybe)
	request_text = results.text
	results_json = json.loads(request_text)
	for item in results_json['data']:
		#print item['name'] #name in special char causing unicode error
		print item['id']
		print ''
		global count
		count = count+1
	try:
		paging_object = results_json['paging']
		next_base_url = paging_object['next']
		search(next_base_url)
	except:
		print ''
	else:
		print ''
event_id='1742982225949209'
burl_maybe='https://graph.facebook.com/v2.3/'+event_id+'/maybe?access_token='+access_token
maybe_ppl(burl_maybe)
print 'These people may go'
print count


