#!/bin/sh

if [ -z "$1" ]
then
    echo "Supply values for the following parameters:"
    echo -n "folder name: "
    read foldername
else
    foldername=$1
fi

# check if desired folder already exists
if [ -d $foldername ]
then
    echo "Workspace \"$foldername\" already exists"
    exit 0
fi

# copy files
echo "Creating Workspace \"$foldername\""
cp -r stubs $foldername/
cp make.py $foldername/
