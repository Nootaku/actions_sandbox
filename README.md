# Actions Sandbox

This repo has the purpose of learning the GitHub Actions tool to create CI/CD pipelines. I'll be tinkering with a few concepts and you're welcome to follow along.

In this sandbox, I want to achieve the following objectives:
1. Create a simple `python` script and lint it.
2. Create a unit test with `pytest` and validate that the tests pass.
3. Create a simple `VueJS` webpage and build it.
4. From the previously builded SPA, I want to make a Docker image and push it to `ghcr.io`
5. Fuze everything together to create multiple images (one python API, one VueJS client) and push them to `ghcr.io`

Let's go !

## Getting started

First of, you can find all the documentation [here](https://docs.github.com/en/actions).

### Creating our first action

Github Actions use the `yaml` syntax to run. The actions files should be created in `.github/workflows` directory. So, our first step is to make that directory.

```bash
mkdir .github
cd .github
mkdir workflows
cd workflows
touch first_action.yml
```
