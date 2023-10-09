import wingmods.fetch

def sudocmds():
    print("Error on load, Sudo not designed yet")

def alphacmds():
    print("Warning you are about to execute an alpha command, these have not been tested.")
    with open("log.txt","r") as f:
        console=f.read()
    if console.startswith("alpha sudo fetch"):
        wingmods.fetch.fetch()