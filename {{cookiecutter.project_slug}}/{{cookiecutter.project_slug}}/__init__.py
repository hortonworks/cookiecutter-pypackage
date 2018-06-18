"""Top-level package for {{ cookiecutter.project_name }}."""
import pbr.version

__author__ = '{{ cookiecutter.full_name }}'
__email__ = '{{ cookiecutter.email }}'

version_info = pbr.version.VersionInfo('{{ cookiecutter.project_slug }}')
__version__ = version_info.release_string()
