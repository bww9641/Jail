#!/bin/bash

prog=('Bash' 'C' 'Go' 'Js' 'Perl' 'PHP' 'Python' 'Ruby')
port=(6656 6657 6658 6659 6666 6667 6668 6669)

for index in ${!prog[*]} ; do
    path="`pwd`/jail/${prog[$index]}"
    cmd="docker build -t prob/${prog[$index]} ${path}"
    echo $cmd
    runner="docker run -d -p ${port[$index]}:2222 prob/${prog[$index]}"
    echo $runner
done