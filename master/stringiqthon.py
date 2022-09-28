#!/usr/bin/env python3
# (c) https://t.me/ArmanthonChat/37677
# This Source Code Form is subject to the terms of the GNU
# General Public License, v.3.0. If a copy of the GPL was not distributed with this
# file, You can obtain one at https://www.gnu.org/licenses/gpl-3.0.en.html.

from Armanthon.sessions import StringSession
from Armanthon.sync import TelegramClient

print("- Code Armanthon For ch : @iqthon")
APP_ID = int(input("APP ID here: "))
API_HASH = input("API HASH here: ")

with TelegramClient(StringSession(), APP_ID, API_HASH) as client:
    print(client.session.save())
    client.send_message("me", client.session.save())
