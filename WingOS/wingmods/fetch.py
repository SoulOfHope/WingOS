def fetch():
    with open("log.txt","r") as f:
        console=f.read()
    if console == "alpha sudo fetch --help" or console == "alpha sudo fetch -h":
        print("""
/---------------------------------------------------------\\
|Fetch: The WingOS download system                        |
|                                                         |
|This works a bit like apt (run this as sudo)!            |
|                                                         |
|fetch -[ARGS]                                            |
|                                                         |
|Args:                                                    |
|    -d ------------ Location to fetch from               |
|    -s ------------ Location to save to                  |
|    --url --------- Alias for -d                        |
|    --save -------- Alias for -s                         |
|    -l ------------ List all files that are being fetched|
|    -e ------------ Check an exception code              |
|    --error ------- Alias for -e                         |
|    -y ------------ Don't ask when downloading           |
|    -h ------------ Displays this message                |
|    --help -------- Alias for -h                         |
\\---------------------------------------------------------/
""")
    else:
        print("Fetch Command Not Found. Please Try Again")