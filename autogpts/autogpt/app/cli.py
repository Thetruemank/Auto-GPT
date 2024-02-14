import click
import requests


def validate_github_token(access_token):
    headers = {"Authorization": f"token {access_token}"}
    response = requests.get("https://api.github.com/user", headers=headers)
    if response.status_code == 200:
        scopes = response.headers.get("X-OAuth-Scopes", "").split(", ")
        required_scopes = {"public_repo", "repo"}
        if not required_scopes.intersection(set(scopes)):
            missing_scopes = required_scopes.difference(set(scopes))
            click.echo(click.style(f"❌ GitHub access token is missing required scopes: {', '.join(missing_scopes)}. Present scopes: {', '.join(scopes)}. Please ensure it has 'public_repo' or 'repo' scope.", fg="red"))
            return False
        click.echo(click.style("✅ GitHub access token has the required permissions.", fg="green"))
        return True
    else:
        click.echo(click.style("❌ Failed to validate GitHub access token. Please ensure it is correct.", fg="red"))
        return False
