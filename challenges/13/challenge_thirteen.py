from xmlrpc.client import ServerProxy, Error
# View source for some hints, call <remote /> (like RPC?)
# Gather the URL from the source and initate a phonecall to evil
call_url = 'http://www.pythonchallenge.com/pc/phonebook.php'

with ServerProxy(call_url) as proxy:
    try:
        # In case we want to confirm the method to use, we can
        # print(proxy.system.listMethods())
        print(proxy.phone('Bert'))
    except Error as v:
        print("ERROR", v)
