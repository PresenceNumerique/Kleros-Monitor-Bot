#!/usr/bin/python3

import getopt
import sys
from datetime import datetime
sys.path.extend(('lib', 'db'))

import os
from kleros_db_schema import db, Dispute, Round, Vote, Kleroscan, Court
from kleros import Kleros, KlerosDispute, KlerosVote

k = Kleros(os.environ["ETH_NODE_URL"])

jurorlist = k.get_juror_stakes()


print(jurorlist)