import subprocess

class Process:
    def create_process( self, commands: str ) -> None :
        # subprocess.run will run common commands and will kill a process after completion.
        self.completedProcess = subprocess.run( ["powershell", "-Command", commands ], capture_output=True )

        if( self.completedProcess.returncode != 0 ):
            print( f"{ commands } can't be executed!" )
            return

        self.print_stdout()
    
    def print_stdout( self ) -> None:
        print( self.completedProcess.stdout.decode( "utf-8" ) )