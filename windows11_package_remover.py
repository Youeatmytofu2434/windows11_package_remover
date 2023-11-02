import sys
from process import Process

FILE_PATH = "packages.txt"

def read_file( fileName: str ) -> list[ str ]:
    try:
        # Keeps track of all packages' IDs.
        packageList: list[ str ] = []
        
        with open( fileName ) as file:
            lines = file.readlines()

            # Get rid of leading and trailing white spaces and "\n" char in each line.
            for line in lines:
                line = line.strip()
                packageList.append( line.strip( "\n" ) )
        
        # Exit the program if "packages.txt" is empty.
        if( len( packageList ) == 0 ):
            sys.exit( f'{ FILE_PATH } is empty. Please add a package into "{ FILE_PATH }".' )

        return packageList
            
    except FileNotFoundError:
        sys.exit( f"{ fileName } not found!" )
    
if __name__ == "__main__":

    packageList = read_file( FILE_PATH )
    newProcess = Process()

    # Loop thru each package and delete each individual package listed in "packages.txt".
    for pkg in packageList:
        tempCmd = f'winget uninstall --id "{ pkg }"'
        newProcess.create_process( tempCmd )

    