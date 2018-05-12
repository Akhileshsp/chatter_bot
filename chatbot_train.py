from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot=ChatBot('MyBot')
bot.set_trainer(ListTrainer)

for files in os.listdir('/home/akhilesh/chatterbot_example/chatterbot-corpus/chatterbot_corpus/data/akhilesh_convo/'):
	data=open('/home/akhilesh/chatterbot_example/chatterbot-corpus/chatterbot_corpus/data/akhilesh_convo/' + files , 'r').readlines()
	bot.train(data)

while True:
	message = input('You: ')
	if message.strip() != 'Bye':
		reply = bot.get_response(message)
		print('ChatBot: ',reply)

	if message.strip() == 'Bye':
		print('ChatBot: Bye')
		break

