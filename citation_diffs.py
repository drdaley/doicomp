import sys
import re
import itertools

REGEX = r"(?:DOI\:)([A-z0-9\/\.\\]+)(?:\s)"

def getgroup(regexpresult):
    return regexpresult.group(1)

if __name__ == '__main__':
    pattern = re.compile(REGEX)
    r = dict()
    
    for index, filename in enumerate(sys.argv[1:]):
        with open(filename, "r") as f:
            data = f.read()    
            result = pattern.finditer(data)
            r[index] = set(map(getgroup, result))
 
    citations_all = set.intersection(*list(r.values()))
    
    print("Citations that occur in all files:")
    for entry in sorted(citations_all):
        print(entry)
        
    if len(sys.argv[1:]) > 2:
        print("")
        print("Citations that occur in at least two files: ")
        citations_some = set.union(*[set.intersection(r[a], r[b]) 
                                    for a, b in itertools.combinations(range(len(sys.argv[1:])), 2)])
        for c in sorted(citations_some):
            print(c)
        
        