
import logging as log
import os
import urllib

import credentials


card_template = ("{name} - {rarity} - {type}\n\nEnergy: {energy}\n\n{description}")
curse_status_template = ("{name} - {type}\n\n{description}")
relic_template = ("{name} - {rarity} - {type}\n\n{description}")
signature = ("\n\n^[PM](https://www.reddit.com/message/compose/?to={bot})"
            " ^( me with up to 7 [[cardname]] or [[relicname]]. )"
            "^[About.](https://github.com/psulkava/slaythespire-bot)") \
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
    if card['Rarity'] == "":
        return curse_status_template.format(**local_card)
    elif card['Energy'] == "":
        return relic_template.format(**local_card)
    else:
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
