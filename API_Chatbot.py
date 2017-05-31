import scrapy
from api.ai import Agent
import json
from scrapy.contrib.spiders import CrawlSpider
import urlparse



#initialize the agent 
agent = Agent(
     '<subscription-key>',
     '<client-access-token>',
     '<developer-access-token>',
)

class GenericSpider(CrawlSpider):
    """a generic spider, uses type() to make new spider classes for each domain"""
    name = 'generic'
    allowed_domains = []
    start_urls = []

    @classmethod
    def crawl(cls, link):
        domain = urlparse.urlparse(link).netloc.lower()
        # generate a class name such that domain www.google.com results in class name GoogleComGenericSpider
        class_name = (domain if not domain.startswith('www.') else domain[4:]).title().replace('.', '') + cls.__name__
        return type(class_name, (cls,), {
            'allowed_domains': [domain],
            'start_urls': [link],
            'name': domain
        })
# actions defined in the API.AI console that fire locally when an intent is
# recognized
def actionOne(intentOne):
	print 'do something here'

def actionTwo(intentTwo):
	print 'do something here'

def actionThree(intentThree):
	print 'do something here'

	
def main():
	user_input = ''

	#loop the queries to API.AI so we can have a conversation client-side
	while user_input != 'exit':

		#parse the user input
		user_input  = raw_input("me: ")
		#query the console with the user input, retrieve the response
		response = agent.query(user_input)
		#parse the response
		result = response['result']
		fulfillment = result['fulfillment']

		print 'bot: ' + fulfillment['speech']

		#if an action is detected, fire the appropriate function
		if result['action'] == 'actionOne':
			saveType(user_input)
		if result['action'] == 'actionTwo':
			saveColor(user_input)
		if result['action'] == 'actionThree':
			createOrder(user_input)
		if result['action'] == 'crawl':
                        createOrder(user_input)


if __name__ == "__main__":
    main()
