# copier-python-fastapi

## Installation

```commandline
pipx install copier
```

## Usage

To generate a project, use the `copier copy` command.

```commandline
copier copy --vcs-ref=v0.1.0 url/to/project/template path/to/destination
```

If a template's tag ref is used in the `copy` command, 
this tag will be in the `_commit` variable in the generated `.copier-answers.yml` file.
Then it will be possible to update a project whenever the template has evolved.

[More info](https://copier.readthedocs.io/en/stable/generating/)

To update a project use the `copier update` command.

```commandline
cd ~/projects/my_new_project
copier update --vcs-ref=v0.1.0 .
```

[More info](https://copier.readthedocs.io/en/stable/updating/)

## Testing

The template can be tested with [`copier_template_tester`](https://pypi.org/project/copier_template_tester/)

```commandline
make test
```
