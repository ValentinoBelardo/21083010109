#!/bin/bash

#deklarasi array compound assignment
distroLinuxDesktop=('Ha' 'Ha' 'He' 'He' 'He')
distroLinuxServer=('RiotServer' 'NasaServer' 'GoogleServer')

#cara mengambil nilai array
echo ${distroLinuxDesktop[*]}
echo ${distroLinuxServer[*]}
