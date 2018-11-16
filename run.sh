#!/bin/bash

prog=('Bash' 'C' 'Js' 'PHP' 'Python')
port=(6656 6657 6658 6659 6670)

for index in ${!prog[*]} ; do
    path="`pwd`/${prog[$index]}"
    cmd="docker build -t prob/${prog[$index],,} ${path}"
    $cmd
    runner="docker run -d -p ${port[$index]}:2222 prob/${prog[$index],,}"
    $runner
done