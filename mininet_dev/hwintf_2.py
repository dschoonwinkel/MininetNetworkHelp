#!/usr/bin/python

"""
This example shows how to add an interface (for example a real
hardware interface) to a network after the network is created.
"""

import re
import sys

from mininet.cli import CLI
from mininet.log import setLogLevel, info, error
from mininet.net import Mininet
from mininet.link import Intf
from mininet.topolib import TreeTopo
from mininet.util import quietRun
from mininet.node import Controller, RemoteController

def checkIntf( intf ):
    "Make sure intf exists and is not configured."
    if ( ' %s:' % intf ) not in quietRun( 'ip link show' ):
        error( 'Error:', intf, 'does not exist!\n' )
        exit( 1 )
    ips = re.findall( r'\d+\.\d+\.\d+\.\d+', quietRun( 'ifconfig ' + intf ) )
    if ips:
        error( 'Error:', intf, 'has an IP address,'
               'and is probably in use!\n' )
        exit( 1 )

if __name__ == '__main__':
    setLogLevel( 'info' )

    # try to get hw intf from the command line; by default, use eth1
    intfName = sys.argv[ 1 ] if len( sys.argv ) > 1 else 'eth0'
    info( '*** Connecting to hw intf: %s' % intfName )

    info( '*** Checking', intfName, '\n' )
    checkIntf( intfName )

    info( '*** Creating network\n' )
    net = Mininet( topo=TreeTopo( depth=1, fanout=2 ), controller=RemoteController )

    switch = net.switches[ 0 ]
    info( '*** Adding hardware interface', intfName, 'to switch',
          switch.name, '\n' )
    h1 = net.hosts[0]
    _intf = Intf( intfName, node=switch )

    info( '*** Note: you may need to reconfigure the interfaces for '
          'the Mininet hosts:\n', net.hosts, '\n' )

    net.start()
    CLI( net )
    net.stop()
