from lunar_policy import Check

with Check("readme-exists", "Repository should have a README.md file") as c:
    c.assert_true(c.get(".repo.readme_exists"), "README.md file not found")
