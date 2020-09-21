#!/bin/bash

cd drive
cd My Drive
if [ ! -d 'N-BEATS' ]
then
	git clone https://github.com/deeptavker/N-BEATS.git
fi
cd N-BEATS
git pull


