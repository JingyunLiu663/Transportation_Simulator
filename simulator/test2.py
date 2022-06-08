# # from utilities import *
# import sys
#
# import numpy as np
# import pandas as pd
#
# import pickle
#
# records = pickle.load(open('dataset.pickle','rb'))
#
# for time in records.keys():
#     for order in records[time]:
#             print(order)
#             sys.exit()
#
#
# pickle.dump(records,open('dataset.pickle','wb'))

from azureml.opendatasets import NycTlcYellow

from datetime import datetime
from dateutil import parser


end_date = parser.parse('2015-05-02')
start_date = parser.parse('2015-05-01')
nyc_tlc = NycTlcYellow(start_date=start_date, end_date=end_date)
print(nyc_tlc)
nyc_tlc_df = nyc_tlc.to_pandas_dataframe()

nyc_tlc_df.info()
print(nyc_tlc_df)