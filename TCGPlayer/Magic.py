from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen
from urllib import quote
from re import compile

class Set:
    'Simple class for getting sets from the tcgplayer'
    
    def __init__(self):
        self.url = 'http://magic.tcgplayer.com/all_magic_sets.asp'
        self.__request()
        self.__sets()
    
    def __request(self):
        'Request the set page from tcgplayer'
        self.page = urlopen(self.url).read()
        
    def __sets(self):
        'Use regular expression to get sets'
        expr = '<a class=default_9 href="/db/search_result.asp\?Set_Name=(.*)">(.*)</a>'
        self.sets = compile(expr).findall(self.page)

    def getSets(self):
        'Return a dict of sets found'
        return dict(self.sets)
        
class Card:
    'Get a complete set'
    
    def __init__(self, set):
        url = 'http://magic.tcgplayer.com/db/search_result.asp?Set_Name=%s'
        self.url = url % quote(set)
        self.__request()
        self.__table()
        self.__card_trs()
        self.__cards()
        
    def __request(self):
        'Request the set from magiccards.info'
        self.page = urlopen(self.url).read()
        
    def __table(self):
        'Use BeautifulSoup to get all card tr blocks'
        soup = BeautifulSoup(self.page)
        self.table = soup.findAll('table', {'width': '540', 'align': 'center',
                                  'cellpadding': '1'})
        if len(self.table) != 1:
            raise Exception('Found more than one table block matching our pattern')
        
    def __card_trs(self):
        'Extract data from the card tr blocks'
        self.trs = self.table[0].findAll('tr')
        
    def __cards(self):
        'Get card data from the trs'
        self.cards = {}
        for tr in self.trs:
            tds = tr.findAll('td')
            card_name = tds[0].text.replace('&nbsp;', '')
            cost = tds[1].text
            set = tds[2].text.replace('&nbsp;', '')
            rarity = tds[3].text
            low = tds[4].text.lstrip('$')
            avg = tds[5].text.lstrip('$')
            high = tds[6].text.lstrip('$')
            
            if rarity != 'L': # skip basic lands
                self.cards[card_name] = (dict(card_name=card_name, cost=cost,
                                              set=set, rarity=rarity, low=low,
                                              avg=avg, high=high))
    
    def getCards(self):
        'Return a dict of cards in the set'
        return self.cards

    def getCard(self, card):
        'Return a single card'
        return self.cards[card]

    
