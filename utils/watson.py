#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests, csv
from requests.auth import HTTPBasicAuth

link = 'https://gateway.watsonplatform.net/tone-analyzer/api/v3/tone?version=2017-09-21&text='

#Example for testing
urltext = '''
In recent days the UK’s standing in the world has further diminished as the impacts of Brexit become more tangible. Earlier this week the relocation of two EU agencies currently based in London was announced. The European Medicines Agency will move to Amsterdam, while the European Banking Authority will be lost to Paris, which narrowly pipped Dublin to host this prestigious organisation (London loses EU agencies to Paris and Amsterdam in Brexit relocation, 21 November). Between them, the two agencies employ 1,150 people, as well as attracting thousands of visiting researchers and staff members to London. This is despite Brexit secretary David Davis previously voicing his hope that the agencies could remain in London, or at least form part of the negotiations. To add insult to injury, the UK will have to pay for the relocation. In addition, the UK has withdrawn its candidate from election to the UN international court of justice (Report, 21 November). Britain will not have a judge on the UN’s most powerful court for the first time in its 71-year history. Last week, after five rounds of voting by the security council and the general assembly in New York, four judges from Brazil, Lebanon, France and Somalia were chosen for the bench ahead of the UK’s candidate, Christopher Greenwood. The UK’s failure to guarantee a place on the court of an organisation it helped to found is clearly a further sign of its increasing irrelevance on the world stage following the decision to leave the EU. As the UK turns inwards following the Brexit vote, it is hardly a surprise that it is no longer able to command the global influence it once did. Alex Orr Edinburgh • The loss of the EMA and EBA will be keenly felt in Tower Hamlets, east London, as thousands of jobs leave the area. What no one seems to be talking about, though, is who will pick up the bill for the premises both organisations need to exit early. The two are in offices in Canary Wharf – not cheap real estate – and signed long leases before the referendum was called. These will have exit clauses that carry significant cost, possibly millions, that will need to be carried by the taxpayer. It was ludicrous of David Davis to suggest these agencies could stay in London after Brexit. He probably hasn’t even realised that he’s got two extra bills to pick up now that these agencies are leaving, and two sets of regulatory frameworks to replace. Elaine Bagshaw London • Jonathan Powell portrays a bitterly divided country, facing self-inflicted impoverishment and the rapid loss of its remaining influence in the world (Brexit Britain has rendered itself irrelevant, 13 November). This is doubtless an accurate picture of our prospects – though the idea that Britain is less politically stable than Italy might be hard to swallow. But it also poses the question: who cares? Seventeen months after the referendum, and despite the growing mountain of evidence showing the scale of the disaster, the people who voted to leave the EU still want to leave. Their only complaint is that Brexit isn’t coming quick enough. It seems that Powell’s dread that Britain faces international irrelevance doesn’t bother them at all. It also seems that Britain’s history as a beacon of democracy through two world wars and our ability, much prized by the nation’s political elite, “to punch above our weight”, means little to people who feel ignored and deserted by the world. For them it’s what the American sociologist Arlie Russell Hochschild has called “deep history” that matters; not statistics or lectures from experts, but a feeling for what seems right and true. And that may well be a vision of Britain as a quiet little country, without global significance or aspirations, content to bob along on the ocean of history, putting what energy it has into keeping its head above water. Peter Lyth Southwell, Nottinghamshire • The EU divorce bill seems large because it attempts to quantify the present value of the cost of contingent liabilities on arbitrary assumptions about what liabilities might arise in the distant future (May seeks to unite cabinet behind higher divorce bill, 20 November). This would be a non-issue if Britain simply agreed to accept the jurisdiction of the European court of justice, as some non-EU members already do, to settle disputes if they occur in future about these liabilities. SP Chakravarty Bangor, Gwynedd • Otto Inglis’s letter listing Chinese overseas investments (21 November) points to yet another inconsistency of Tory party thinking. They boast about overseas investment in the UK as a sign of our strength. Yet China, and our own history, shows that it is the strong who invest in the weak for both economic return and political influence, and the weak who have to accept the interest of the strong. And all the time our flag-waving foreign secretary is widely regarded as a laughingstock. Norman Gowar London • Like most of your readers, I voted against Brexit. But when I read the silly class prejudice and self-regard of many of the writers you chose to reflect on our leaving the EU (End of the affair, Review, 18 November), I’m afraid it becomes ever more clear why it might have happened. Andrew Hadfield Hove, Sussex • Join the debate – email guardian.letters@theguardian.com • Read more Guardian letters – click here to visit gu.com/letters


'''

#Opening user/passw from CVS to protect API token
user=''
passw=''

if __name__ == "__main__":
   csvDataFile = open('cred.csv')
else:
   csvDataFile = open('utils/cred.csv')
csvReader = csv.reader(csvDataFile)
for row in csvReader:
   user = row[0]
   passw = row[1]

def sanatizeText(text):
	text.replace("&nbsp;"," ")
	return text

#ret value
# ret['tones'], ret['scores']
def mainEmotion(url):
	url = sanatizeText(url)
	content = requests.get(link+url, auth=HTTPBasicAuth(user, passw))
	content = content.json()
	ret ={}
	tonenames = []
	tonescore = []
	for each in content['document_tone']['tones']:
		tonenames.append(each['tone_name'])
		tonescore.append(each['score'])
	ret['tones']=tonenames
	ret['scores'] = tonescore
	return ret

def sentEmotion(url):
	url = sanatizeText(url)
	ret =[]
	content = requests.get(link+url, auth=HTTPBasicAuth(user, passw))
	content = content.json()
	wanted = content["sentences_tone"]
	for sentence in wanted:
		tempDict = {}
		tempDict["text"] = sentence["text"]
		tempTones = {}
		if len(sentence["tones"]) == 0:
			tempTones["Neutral"] = 0
		else:
			for tone in sentence["tones"]:
				tempTones[tone["tone_name"]] = tone["score"]
		tempDict["tones"] = tempTones
		ret.append(tempDict)
	return ret
