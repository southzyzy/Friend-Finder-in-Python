import click

def welcome():
    """
    Welcome to ICT1002 Dating app
    :return:
    """

@click.command()
@click.option('--users', help='Listing the profiles of all users')
@click.argument('option')
def hello(option):
    click.echo("You selected %s" % option)

if __name__ == '__main__':
    welcome()
