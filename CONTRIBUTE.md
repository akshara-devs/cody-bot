# Conventional Commit

The [conventional commit](https://www.conventionalcommits.org/en/v1.0.0/) message should be structured as follows:


```
<type>([optional scope]): <description>

[optional body]

[optional footer(s)]
```

These are common `type`:

- `fix` -> patches a bug in your codebase
- `feat` -> introduces a new feature to the codebase
- `style` -> UI/UX related changes
- `docs` -> Edit/Improving the documentation like `.md` files
- `chore` -> Not directly affecting the production code / small changes like removing `print` statement

- `!` -> BREAKING CHANGES COMMIT

Examples:

- `feat(projects): add a new capabilities to each user for creating their own project using "/project new <args>" command`
- `fix(currencies): validate enum type and improve the error handling when user were not registered`
- `chore: removing unused variable and debugging print statement for several feature`
- `fix(user)!: prevent the user to ruin my server`

# Contributing Flow

You must create a new branch and pull the latest changes from the `main` branch.

```
git checkout -b <type>/<description>
```

The `type` is the same as Conventional commit type.
