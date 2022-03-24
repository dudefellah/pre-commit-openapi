# pre-commit-openapi

A simple pre-commit hook for validating your Swagger and/or OpenAPI spec.
document using Python.

Another project which does the same thing with Node is here:
https://github.com/APIDevTools/swagger-cli

I created this one because I don't want to install Node/npm just for this
small bit of functionality.

# Usage

Add this to your `.pre-commit-config.yaml`

```yaml
- repo: https://github.com/dudefellah/pre-commit-openapi
  rev: "v0.0.2"
  hooks:
    - id: check-openapi
```

# Tools Used

This project creates a simple hook which takes advantage of the
[openapi-spec-validator](https://pypi.org/project/openapi-spec-validator/)
project.

# Hook Author(s)

Dan - github.com/dudefellah
