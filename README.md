# lunar-config-template

This is your Earthly Lunar configuration repository.

Please refer to the [Earthly Lunar documentation](https://docs-lunar.earthly.dev/) to get started.

Here is a quick cheat sheet for local development of collectors and policies:

```bash
# Run a collector locally. This outputs the component JSON delta(s).
lunar collector dev readme --component github.com/example/repo

# Run a policy locally.
echo '{"repo": {"readme_exists": true}}' | lunar policy dev readme --component-json -

# Run a collector locally, then feed the result into a policy locally.
# (The jq command is needed to merge multiple component JSON deltas into a single JSON object)
lunar collector dev readme --component github.com/example/repo | \
    jq -n 'reduce inputs as $item ({}; . * $item)' | \
    lunar policy dev readme --component-json -

# Fetch the component JSON from Lunar Hub.
lunar component get-json github.com/example/repo

# Run a policy locally with the component JSON from Lunar Hub.
lunar policy dev readme --component github.com/example/repo
```
