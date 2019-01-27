import click


class Config(object):
    def __init__(self):
        self.verbose = False


pass_config = click.make_pass_decorator(Config)

@click.group()
@click.option('--verbose', is_flag=True)
@click.option('--home-dir', type=click.Path())
@pass_config
def cli(config, verbose, home_dir):
    config.verbose = verbose
    if home_dir is None:
        home_dir = '.'
    config.home_dir = home_dir

@cli.command()
@click.option('--string', default='World', help='This is the option to greet you')
@click.option('--repeat', default=1, help='How many times you should be greeted')
@click.argument('out', type=click.File('r'), default='-', required=False)

@pass_config
def say(config, string, repeat, out):
    """This script greets you"""
    if config.verbose:
        click.echo('We are in verbose mode')
    click.echo('Home Directory is %s' % config.home_dir)






if __name__ == "__main__":
    say()