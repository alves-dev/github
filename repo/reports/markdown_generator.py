class MarkdownGenerator:
    @classmethod
    def build(cls, repos):
        items = ''.join(
            f'**ID:** {repo.id} **name:** {repo.name} **stars:** {repo.stars}\n'
            for repo in repos)
        return f'## REPOS \n\n{items}'

# Dica: talvez usar uma interface para garantir a def build
