# lunar-config-template

This is your Earthly Lunar configuration repository.

Please refer to the [Earthly Lunar documentation](https://docs-lunar.earthly.dev/) to get started.

Here is a quick cheat sheet for local development of collectors and policies:

```bash
# Run a collector locally. This outputs the component JSON delta(s).
lunar collector dev readme --verbose --component github.com/example/repo

# Run a policy locally.
echo '{"repo": {"readme_exists": true}}' | lunar policy dev readme --verbose --component-json -

# Run a collector locally, then feed the result into a policy locally.
lunar collector dev readme --verbose --component github.com/example/repo | \
    lunar policy dev readme --verbose --component-json -

# Fetch the component JSON from Lunar Hub.
lunar component get-json github.com/example/repo

# Run a policy locally with the component JSON from Lunar Hub.
lunar policy dev readme --verbose --component github.com/example/repo
```
