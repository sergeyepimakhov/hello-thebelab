# hello-thebelab

Basic example of ThebeLab https://github.com/minrk/thebelab

## Create Conda

    conda create -n hello-thebelab jupyter

## Convert Notebook to HTML

### Install

```bash
    pip install nbconvert
    # OR
    conda install nbconvert
```

### Command Line

Full HTML

  jupyter nbconvert notebook.ipynb

Without headers

  jupyter nbconvert notebook.ipynb --template basic



## Enable ThebeLab

```HTML
<script type="text/x-thebe-config">
      {
        bootstrap: true,
        selector: "pre",
        binderOptions: {
          repo: "binder-examples/requirements",
        },
        kernelOptions: {
          name: "python3",
        },
      }
</script>
<script type="text/javascript" src="https://unpkg.com/thebelab@^0.4.0"></script>
```

## Using nbconvert as Library

https://nbconvert.readthedocs.io/en/latest/nbconvert_library.html