"""
******************************************
Starting file for the application
******************************************
"""

from myapp import create_app

app = create_app()

if __name__ == '__main__':
    app.run( port=1234, debug=True )






