import sys, os

class Methods:
    def __init__( self ) -> None:
        self.menu: str = '\t-< q: quit | a: entrer l\'annee | c: clear screen >-'

    def quit( self ) -> None:
        print( '\n--> Exiting...' )
        sys.exit( 1 )

    def clear( self ) -> None:
        os.system( 'cls' if os.name == 'nt' else 'clear' )
        print( self.menu )

        return

    def command_not_found( self, command: str ) -> None:
        print( f'--> { command } is not found...' )

        return

    def value_error( self ) -> None:
        print( '--> Please enter a number...' )

        return

methods: Methods = Methods()

def main() -> None:
    methods.clear()

    while True:
        choice: str = input( '=> ' ).replace( ' ', '' ).lower()

        if choice == 'q':
            methods.quit()
        elif choice == 'c':
            methods.clear()
        elif choice == 'a':
            try:
                annee: int = int( input( '>-> Annee: ' ).replace( ' ', '' ) )
            except ValueError:
                methods.value_error()
        else:
            methods.command_not_found( choice )

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        methods.quit()
