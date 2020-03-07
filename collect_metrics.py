#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sys
import argparse
import psutil

def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument('name_metric', choices=['cpu','mem','disks','network','process'])

    return parser

if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])

#    print (namespace)

    print ("Metric= {} ".format (namespace.name_metric) )
    if namespace.name_metric == 'cpu':
        cpu = psutil.cpu_times()
        print("system.cpu.user:    {:12.2f}".format (cpu.user))
        print("system.cpu.system:  {:12.2f}".format (cpu.system))
        print("system.cpu.idle:    {:12.2f}".format (cpu.idle))
        print("system.cpu.guest:   {:12.2f}".format (cpu.guest))
        print("system.cpu.iowait:  {:12.2f}".format (cpu.iowait))
        print("system.cpu.steal:   {:12.2f}".format (cpu.steal))
    elif namespace.name_metric == 'mem':
        mem_virt = psutil.virtual_memory()
        print("virtual total:  {:14.2f}".format (mem_virt.total))
        print("virtual used:   {:14.2f}".format (mem_virt.used))
        print("virtual free:   {:14.2f}".format (mem_virt.free))
        print("virtual shared: {:14.2f}".format (mem_virt.shared))
        mem_swap = psutil.swap_memory()        
        print("swap total:     {:14.2f}".format (mem_swap.total))
        print("swap used:      {:14.2f}".format (mem_swap.used))
        print("swap free:      {:14.2f}".format (mem_swap.free))
    elif namespace.name_metric == 'disks':
        disk = psutil.disk_usage('/')
        print("For / filesystem")
        print("total:            {:14.2f}".format (disk.total))
        print("used:             {:14.2f}".format (disk.used))
        print("free:             {:14.2f}".format (disk.free))
        print("percent usage:    {:14.2f}".format (disk.percent))
        disk_io = psutil.disk_io_counters()
        print("disk read_count:  {:14.2f}".format (disk_io.read_count))
        print("disk write_count: {:14.2f}".format (disk_io.write_count))
        print("disk read_bytes:  {:14.2f}".format (disk_io.read_bytes))
        print("disk write_bytes: {:14.2f}".format (disk_io.write_bytes))
    elif namespace.name_metric == 'network':
        network = psutil.net_io_counters()
        print("bytes_sent:   {:14.2f}".format (network.bytes_sent))
        print("bytes_recv:   {:14.2f}".format (network.bytes_recv))
        print("packets_sent: {:14.2f}".format (network.packets_sent))
        print("packets_recv: {:14.2f}".format (network.packets_recv))
        print("errin:        {:14.2f}".format (network.errin))
        print("errout:       {:14.2f}".format (network.errout))
        print("dropin:       {:14.2f}".format (network.dropin))
        print("dropout:      {:14.2f}".format (network.dropout))
    else:
        print("  pid       name           username")
        for p in psutil.process_iter(['pid', 'name', 'username', 'uids']):
#            print(p.info)
            print(" {:5d}  {:20s}  {:20s}  {} ".format(p.info['pid'],p.info['name'],p.info['username'],p.info['uids'])) 

