#!/usr/bin/env python3
""" This script  collects standard metrics on a Ubuntu server using a module psutil. """
# -*- coding: UTF-8 -*-

import argparse
import psutil

def create_parser():
    """ The argparse module allows you to parse the arguments passed to the script
    when it is run from the command line."""
    pars = argparse.ArgumentParser()
    pars.add_argument('name_metric', choices=['cpu', 'mem', 'disks', 'network', 'process'])

    return pars

def prep_output(str_temp, str_inp):
    """Prepare string to print: removing characters outside of parentheses,
    replacing sequence ', ' on '\n' and adding a pattern at the begining of a lines"""
    return str_temp+str_inp[str_inp.find('(')+1 : str_inp.find(')')].replace(', ', '\n'+str_temp)


if __name__ == '__main__':
    PARSER = create_parser()
    NAMESPACE = PARSER.parse_args()

    print("Metric={0}\n-----------".format(NAMESPACE.name_metric))
    if NAMESPACE.name_metric == 'cpu':
        CPU = str(psutil.cpu_times())
        print(prep_output('system.cpu.', CPU))
    elif NAMESPACE.name_metric == 'mem':
        MEM_VIRT = str(psutil.virtual_memory())
        print(prep_output('virtual ', MEM_VIRT))
        MEM_SWAP = str(psutil.swap_memory())
        print(prep_output('swap ', MEM_SWAP))
    elif NAMESPACE.name_metric == 'disks':
        DISK = str(psutil.disk_usage('/'))
        print("For / filesystem")
        print(prep_output('', DISK))
        DISK_IO = str(psutil.disk_io_counters())
        print(prep_output('disk ', DISK_IO))
    elif NAMESPACE.name_metric == 'network':
        NETWORK = str(psutil.net_io_counters())
        print(prep_output('', NETWORK))
    else:
        print("  pid       name           username")
        for p in psutil.process_iter(['pid', 'name', 'username', 'uids']):
            print(" {:5d}  {:20s}  {:20s}  {}".format(p.info['pid'], p.info['name'], 
                p.info['username'], p.info['uids']))
