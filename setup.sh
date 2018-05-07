#!/bin/bash

# ensure PIP in installed
if [ '/usr/bin/pip' ]; then
	# PIP is installed
	PIP='/usr/bin/pip'
	CMD='install -r requirements.txt'
	#statements
	$PIP $CMD
fi
elif [ !'/usr/bin/pip' ]; then
	#statements
	echo 'PIP not found'