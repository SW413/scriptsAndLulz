#/bin/bash
cat mark.dinner| cut -c7-99 | sed 's/[ \t]*$//' | sort | uniq -c | sort -r

