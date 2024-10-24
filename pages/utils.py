from github import Github
import asyncio

async def get_total_stars_and_repos_in_org(org_name):
    # Initialize PyGitHub
    g = Github()

    # Get the organization
    org = g.get_organization(org_name)

    # Get all repositories
    repos = org.get_repos()

    total_stars = 0
    total_repos = 0
    for repo in repos:
        total_stars += repo.stargazers_count
        total_repos += 1

    return total_stars, total_repos


from project.models import Category
from training.models import Category as ProjectCategory
from .models import Partners
def get_nav():
    categories = Category.objects.all()
    project_categories = ProjectCategory.objects.all()[::-1]
    partners = Partners.objects.all()

    context = {
        "categories":categories,
        "project_categories":project_categories,
        "partners":partners
    }

    return context