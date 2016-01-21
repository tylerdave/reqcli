import click
import requests

@click.command()
@click.argument('url')
@click.option('--header', '-h', multiple=True, help='Add a colon-delimeted HTTP header to the request (eg. "Host: www.example.com")')
@click.option('--headers-json', metavar='JSON', help='Include headers when making the request')
@click.option('--show-headers', '-H', is_flag=True, default=False)
@click.option('--show-status', '-S', is_flag=True, default=False)
@click.option('--quiet', '-Q', is_flag=True, default=False)
@click.option('--allow-redirects/--no-allow-redirects', default=True)
@click.option('--verbose', '-v', is_flag=True, default=False)
def cli(url, header, headers_json, show_headers, show_status, quiet, allow_redirects, verbose):

    if header:
        click.echo(type(header))
        click.echo(header)

    if headers_json:
        click.echo(headers_json)

    # Make the request
    if verbose:
        click.secho('Making HTTP request to "{0}"...'.format(url), err=True, fg='white')
    try:
        response = requests.get(url, allow_redirects=allow_redirects)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        click.secho(str(e), err=True, fg='yellow' )
        raise click.Abort()
    except Exception as e:
        click.secho(str(e), err=True, fg='red' )
        raise click.Abort()

    status_colors = {
            2: 'green',
            3: 'blue',
            4: 'yellow',
            5: 'red',
            }

    # Show the response status
    if show_status:
        status_color = status_colors.get(int(response.status_code) / 100)
        click.secho('Status: {0}'.format(response.status_code), err=True, fg=status_color)

    # Show the response headers
    if show_headers:
        click.echo(format_headers(response.headers), err=True)

    # Show the response body
    if not quiet:
        click.echo(response.text)

if __name__ == '__main__':
    cli()

def format_headers(headers):
    formatted = ['{0}: {1}'.format(k, v) for k, v in headers.items()]
    return '\n'.join(formatted)
