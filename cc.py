import json
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import datetime


def data():
    today = datetime.datetime.today()
    heroes = []
    heroes_wr = []
    win_rates = []
    win_win = []
    VERSION = '0.5.5'
    name = ['abaddon', 'alchemist', 'ancient-apparition', 'anti-mage', 'arc-warden', 'axe', 'bane', 'batrider',
            'beastmaster', 'bloodseeker', 'bounty-hunter', 'brewmaster', 'bristleback', 'broodmother',
            'centaur-warrunner', 'chaos-knight', 'chen', 'clinkz', 'clockwerk', 'crystal-maiden', 'dark-seer',
            'dark-willow', 'dawnbreaker', 'dazzle', 'death-prophet', 'disruptor', 'doom', 'dragon-knight',
            'drow-ranger', 'earth-spirit', 'earthshaker', 'elder-titan', 'ember-spirit', 'enchantress', 'enigma',
            'faceless-void', 'grimstroke', 'gyrocopter', 'hoodwink', 'huskar', 'invoker', 'io', 'jakiro', 'juggernaut',
            'keeper-of-the-light', 'kunkka', 'legion-commander', 'leshrac', 'lich', 'lifestealer', 'lina', 'lion',
            'lone-druid', 'luna', 'lycan', 'magnus','marci', 'mars', 'medusa', 'meepo', 'mirana', 'monkey-king', 'morphling',
            'naga-siren', "natures-prophet", 'necrophos', 'night-stalker', 'nyx-assassin', 'ogre-magi', 'omniknight',
            'oracle', 'outworld-destroyer', 'pangolier', 'phantom-assassin', 'phantom-lancer', 'phoenix', 'puck',
            'pudge', 'pugna', 'queen-of-pain', 'razor', 'riki', 'rubick', 'sand-king', 'shadow-demon', 'shadow-fiend',
            'shadow-shaman', 'silencer', 'skywrath-mage', 'slardar', 'slark', 'snapfire', 'sniper', 'spectre',
            'spirit-breaker', 'storm-spirit', 'sven', 'techies', 'templar-assassin', 'terrorblade', 'tidehunter',
            'timbersaw', 'tinker', 'tiny', 'treant-protector', 'troll-warlord', 'tusk', 'underlord', 'undying', 'ursa',
            'vengeful-spirit', 'venomancer', 'viper', 'visage', 'void-spirit', 'warlock', 'weaver', 'windranger',
            'winter-wyvern', 'witch-doctor', 'wraith-king', 'zeus']
    for nick in name:
            heroes.append(nick)
    # print(heroes)
    with open('date.js', 'a') as f:
        f.write("var heroes = "+"[")
        for hero in heroes:
            if hero == 'zeus':
                f.write('"'+'%s' % hero+'"')
            else:
                f.write('"' + '%s' % hero + '"' + ",")
        f.write("],")
    with open('date.js', 'a') as f:
        f.write("heroes_bg = "+"[")
        for hero in heroes:
            if hero == 'zeus':
                f.write('"'+'/assets/heroes/%s' % hero+'.jpg"')
            else:
                f.write('"' + '/assets/heroes/%s' % hero + '.jpg"' + ",")
        f.write("],")

    elem = 0
    for nick in name:
        try:
            url = 'https://www.dotabuff.com/heroes/%s/counters' % nick
            r = requests.get(url, headers={'User-agent': 'your bot 0.1'})
            soup = BeautifulSoup(r.text, 'lxml')
            tables = soup.find_all('span', {'class': 'won'})

            if tables:
                for item in tables:
                        split_string = item.text.rsplit("%", 1)
                        substring = split_string[0]
                        print(nick +'---'+ substring)
                        heroes_wr.append(substring)
                        elem += 1
            else:
                    tables = soup.find_all('span', {'class': 'lost'})
                    for item in tables:
                            split_string = item.text.rsplit("%", 1)
                            substring = split_string[0]
                            print(nick + '---' + substring)
                            heroes_wr.append(substring)
                            elem += 1
        except:
            pass

    elem = 0
    for nick in name:
        try:
            url = 'https://www.dotabuff.com/heroes/%s/counters' % nick
            r = requests.get(url, headers={'User-agent': 'your bot 0.1'})
            soup = BeautifulSoup(r.text, 'lxml')
            for cnt in name:
                tables = soup.find_all('tr', {'data-link-to':'/heroes/%s' % cnt})
                if tables:
                    for item in tables:
                        mystring = re.sub(",", "", item.text)
                        temp = re.findall(r'[-+]?\d*\.\d+|\d+', mystring)
                        res = list(map(str, temp))
                        win_win.append(res)

                        print(nick + '<<<--->>>'+ cnt + '==='+ str(res))
                        # heroes_wr.append(substring)
                        elem += 1
                else:
                    print(nick + '--->>>' + 'same')
                    win_win.append(None)
            win_rates.append(win_win.copy())
            win_win.clear()
        except:
            pass
    print(win_rates)
    with open('date.js', 'a') as f:
        f.write("heroes_wr = " + "[")
        for wr in heroes_wr:
            f.write('"' + '%s' % wr + '"' + ",")
        f.write("],")
    with open('date.js', 'a') as f:
        f.write("win_rates = "+"[")
        for item in win_rates:
            f.write('%s' % item+',')
        f.write("],")
    with open('date.js', 'a') as f:
        f.write("update_time = "+'"'+today.strftime("%Y-%m-%d")+'"'+';')
data()
