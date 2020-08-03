#!/usr/bin/env
# -*- coding: utf-8 -*-
from Zettel import Zettel

zettel = Zettel()
list = zettel.new_zettel_cards()
for f in list:
    card_id = zettel.make_id(f)
    zettel.rename(f, card_id)
