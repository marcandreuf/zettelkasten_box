import logging
import os
import string
import re

logger = logging.getLogger(__name__)


class Zettel:
    ZETTELKASTEN_FOLDER = '../zettelkasten'
    ZETTEL_FOLDER = '../zettel'
    PNG_EXTENSION = '.png'

    _zettel_cards = []
    _zettelkasten_cards = []

    def __init__(self):
        pass

    def all_zettel_cards(self):
        if len(self._zettelkasten_cards) == 0:
            all_cards = os.listdir(self.ZETTELKASTEN_FOLDER) + os.listdir(self.ZETTEL_FOLDER)
            self._zettelkasten_cards = self._filter_cards(all_cards)
        return self._zettelkasten_cards

    def new_zettel_cards(self):
        if len(self._zettel_cards) == 0:
            zettel_cards = os.listdir(self.ZETTEL_FOLDER)
            zettel_cards = self._filter_cards(zettel_cards)
            self._zettel_cards = self._filter_new_cards(zettel_cards)
        return self._zettel_cards

    def _filter_cards(self, cards):
        return list(filter(lambda f: f.endswith(self.PNG_EXTENSION), cards))

    def _filter_new_cards(self, cards):
        return list(filter(lambda f: re.match('^\d{6}[ ]{1}', f), cards))

    def idExists(self, card_id):
        zettel_cards = self.all_zettel_cards()
        r = list(filter(lambda f: f.startswith(card_id), zettel_cards))
        return True if len(r) > 0 else False

    def make_id(self, card_id):
        for letter in string.ascii_lowercase:
            if not self.idExists(card_id[:6] + letter):
                return card_id[:6] + letter + card_id[6:]

    def rename(self, old_id, new_id):
        os.rename(self.ZETTEL_FOLDER + '/' + old_id,
                  self.ZETTEL_FOLDER + '/' + new_id)
