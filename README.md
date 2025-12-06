# copier-python-fastapi

## Installation

```commandline
pipx install copier
```

## Usage

To generate a project, use the `copier copy` command.

```commandline
copier copy url/to/project/template/tag/ref path/to/destination
```

If a template's tag ref is used in the `copy` command, 
this tag will be in the `_src_path` variable in the generated `.copier-answers.yml` file.
Then it will be possible to update a project whenever the template has evolved.

[More info](https://copier.readthedocs.io/en/stable/generating/)

```commandline
cd ~/projects/my_new_project
copier update --vcs-ref=HEAD
```

[More info](https://copier.readthedocs.io/en/stable/updating/)
