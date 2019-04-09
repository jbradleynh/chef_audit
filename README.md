# chef_audit
This is quick script to pull data from a Chef server and output to a file

The format of the data outputed is pipe delimited '|' in order to be easily imported into tools like excel, as the comma character can appear in surprising places

## Requirements
>##### This script interacts with the Chef server, a working knife environment is required

>##### This script is writen and tested with python 2.7, however YMMV with python 3

Its recommended this is run under a Python virtual enviroment to not conflict with system libraries

```
# create new python virtualenv
virtualenv chef_audit

# navigate into virtualenv directory
cd chef_audit

# activate environment
. bin/activate

# clone this repo

# navigate into repo
cd chef_audit

# install the required packages
pip install -r requirements.txt
```

# Usage

```
Usage: chef_audit.py [options]

Options:
  -h, --help            show this help message and exit
  -s SEARCH, --search=SEARCH
                        knife node search string
  -o OUTPUT, --output=OUTPUT
                        output file name
```

# Examples
> Note this only pulls data from a the current knife enviroment, use `knife block` to adjust

The search pattern takes a string in the standard solr query syntax

Assuming you want to pull details from class of systems you could do something like

```./chef_audit.py -s "name:foobar*" -o foobar_output.txt```

Assuming you want to pull the detail from every node in chef

```./chef_audit.py -s "name:*" -o all_node_`date +%F`.txt```
