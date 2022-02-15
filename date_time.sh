#!/bin/bash

0 * * * * echo $( date +'%m/%d/%Y - %H:%M:%S') >> date_time.txt
