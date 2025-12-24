import sys, os

class Methods:
    def quit( self ) -> None:
        print( '\n--> Exiting...' )
        sys.exit( 1 )

methods: Methods = Methods()

def main() -> None:
    pass

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        methods.quit()
