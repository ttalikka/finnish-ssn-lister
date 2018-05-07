# finnish-ssn-lister
A simple Python script that lists all available Finnish SSNs (henkilötunnus, HETU) of a single date of birth.

Works with Python 3. Usage: python3 ssn.py ddmmyyyy gender, for example: python3 ssn.py 01012001 m

You must specify a gender, since that affects the generation of the SSN identification code. The year of birth must be specified as it affects the century identificator (+, - or A). Works for all dates between 1800-2099. 
