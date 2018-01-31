
import logging as log
import os
import urllib

import credentials


atk_dur_template = " {atk}/{dur}"
subtype_template = " {subType}"
desc_template = " - {desc}"
extDesc_template = "[{text}]  \n"
#card_template = ("* **[{name}]({cdn})** {class} {type} {rarity} {set} {std}"
#                    "^[HP](http://www.hearthpwn.com/cards/{hpwn}), "
#                    "^[HH](http://www.hearthhead.com/cards/{head}), "
#                    "^[Wiki](http://hearthstone.gamepedia.com/{wiki})  \n"
#                "{cost} Mana{atk_dur}{subtype}{desc}  \n{extDesc}")
card_template = ("{name} {rarity} {type} {description}")
signature = ("\n^(Call/)^[PM](https://www.reddit.com/message/compose/?to={bot})"
            " ^( me with up to 7 [[cardname]]. )"
            "^[About.](https://www.reddit.com/message/compose/"
            "?to={bot}&message=Tell%20me%20more%20[[info]]&subject=hi)") \
            .format(bot=credentials.username)

duplicate_header_templ = ("You've posted a comment reply in [{title}]({url}) "
                            "containing cards I already explained. "
                            "To reduce duplicates, your cards are here:\n\n")

def createCardText(card):
    """ formats a single card to text """

    local_card = {
        'name' : card['Name'],
        'rarity' : card['Rarity'],
        'type' : card['Type'],
        'energy' : card['Energy'],
        'description' : card['Description'],
    }

    return card_template.format(**local_card)


def createAnswer(cardDB, cards):
    """gets card formatted card text and signature and joins them"""
    comment_text = ''

    for card in cards:
        if card in cardDB:
            log.debug('adding card to text: %s', card)
            comment_text += cardDB[card]

    if comment_text:
        comment_text += signature
    return comment_text


def createDuplicateMsg(title, url):
    """message header for duplicate comment requests"""
    return duplicate_header_templ.format(title=title, url=url)


def loadInfoTempl(specials=[], alts=[], tokens=[], *, infoMsgTmpl='data/info_msg.templ'):
    """ reads and prepares [[info]] template,
    {user} will remain for later formatting
    """

    if not os.path.isfile(infoMsgTmpl):
        return ''

    rawTemplate = ''
    with open(infoMsgTmpl, 'r', encoding="utf8") as file:
        rawTemplate = file.read()

    # sets to list and sort them all
    specials = list(specials)
    specials.sort()
    alts = list(alts)
    alts.sort()
    tokens = list(tokens)
    tokens.sort()
    # join lists together
    comma = ', '
    specialText = comma.join(specials)
    altsText = comma.join(alts)
    tokensText = comma.join(tokens)

    return rawTemplate.format(user='{user}',
                                alts=altsText,
                                tokens=tokensText,
                                special=specialText)
