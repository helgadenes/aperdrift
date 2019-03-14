# functions: useful things that I pulled out of the make_*_sched.py to make things less messy.
# K.M.Hess 19/02/2019 (hess@astro.rug.nl)

__author__ = "Kelley M. Hess"
__date__ = "$08-mar-2019 16:00:00$"
__version__ = "0.1"

import datetime

from .calibrators import *

_int, priority, lo, sub1, _type, weight, beam, sub2, freq1, freq2, freqcent, intent, person, switch_type = \
     '30', 'A', '4800', '64', 'T', 'compound', '0', '320', '1250.000', '1450.000', '1350.000', 'compound', 'KH', '-'

###################################################################
# Required functions for observing and writing observations to csv file.


def write_to_csv(writer, source_name, source_pos, start_datetime, end_datetime):
    # scan='{}{:03d}'.format(start_datetime.strftime('%Y%m%d'),i)
    # source='{}_{}'.format(source_name.split('_')[0],start_datetime.strftime('%Y%m%d'))
    source = '{}'.format(source_name.split('_')[0])
    ra = str(source_pos.to_string('hmsdms').split(' ')[0]).replace('h', ':').replace('m', ':').replace('s', '')
    dec = str(source_pos.to_string('hmsdms').split(' ')[1]).replace('d', ':').replace('m', ':').replace('s', '')
    date1, time1 = start_datetime.strftime('%Y-%m-%d'), start_datetime.strftime('%H:%M:%S')
    date2, time2 = end_datetime.strftime('%Y-%m-%d'), end_datetime.strftime('%H:%M:%S')
    if source_name in names:
        all_cols=[source, ra, dec, date1, time1, date2, time2, _int, 'S*', weight, beam, 'system']
    else:
        all_cols = [source, ra, dec, date1, time1, date2, time2, _int, _type, weight, beam, switch_type]
    writer.writerow(all_cols)

def write_commands(writer, source_name, source_ha, start_datetime, end_datetime):
    source = '{}'.format(source_name.split('_')[0])
    ha = str(source_ha.deg)
    date1, time1 = start_datetime.strftime('%Y-%m-%d'), start_datetime.strftime('%H:%M:%S')
    date2, time2 = end_datetime.strftime('%Y-%m-%d'), end_datetime.strftime('%H:%M:%S')
    if source_name in names:
        all_cols=[source, ha, date1, time1, date2, time2, _int, 'S*', weight, beam, 'system']
    else:
        all_cols = [source, ha, date1, time1, date2, time2, _int, _type, weight, beam, switch_type]
    writer.writerow(all_cols)
