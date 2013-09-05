# -*- coding: utf-8 -*-

RX_POS = " at (\d+.\d+) (\d+.\d+)"

RX_SEAT_OCCUPIED = r"(.+):(.+)\((\d+)\) seat occupied by .+" + RX_POS
RX_WEAPONS_LOADED = r"(.+):(.+) loaded weapons \'(.+)\' fuel (\d+)%"
RX_KILLED = r"(.*):(.*)\((.*)\) was killed" + RX_POS
RX_SHOT_DOWN = r"(.*):(.*) shot down by (.*):(.*)" + RX_POS
RX_SELECTED_ARMY = r"(.*) selected army (.*)" + RX_POS
RX_WENT_TO_MENU = r"(.*) entered refly menu"
RX_DESTROYED = r"(.*) destroyed by (.*)" + RX_POS
