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

#### Step 1 - Creating the files

Github Actions use the `yaml` syntax to run. The actions files should be created in `.github/workflows` directory. So, our first step is to make that directory.

```bash
# Python file we will use
touch hello_world.py

# Actions directory
mkdir .github
cd .github
mkdir workflows
cd workflows
touch first_action.yml
```

#### Step 2 - Writing the python

Now, let's write our python code in a new document located at `./hello_world.py`

```python
def function_1(a, b):
    """Make sum of a and b."""
    return a + b

def function_2(a, b):
  """Difference of a and b."""
  return a - b
```

In this example I made 2 linter mistakes:

1. There should be 2 lines between `function_1` and `function_2`
2. I used tabs for the spacing of `function_1` and spaces for `function_2`

#### Step 3 - Writing the GitHub Action

```yaml
name: My first action

on: [push]
jobs:
```

> Each Action file has<br>
> A `name`<br>
> A `on` event statement that defines when the action should be triggered<br> > `jobs` that indicate what should happen
>
> Each job has the `run-on` statement that indicates which runner (os) should be used and a collection of `steps` that represent the workflow of a job.
