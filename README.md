# basic-nlp-testing

Space to test some basic NLP models and their speeds on various compute configurations.

## Overview

This code supports some basic NLP pipelines to test how well they work in different compute configurations.

## Usage

* Notebooks should be able to run individually.
* If missing, place a `config.py` file into your `src` folder that contains a `data_path` variable.  
* To run `local_to_blob`:
  * You must make a SAS for the associated storage account and data container in Azure. Copy the `blob_service_sas_url` into your `config.py` file after creating the SAS. Note that when the SAS expires this will no longer work - a new SAS and url will be required.
  * You will also need the name of the `container` you are trying to access. Save this in your `config.py` file.
* To run `blob_to_vm`:
  * You can use the `connection_string` associated with one of the access keys. Save the connection string into your `config.py` file. Note that as keys get rotated, this access will need updating as well.
  * You will also need the name of the `container`, as well as the storage `account` you are trying to access. Save this in your `config.py` file.

## Structure

Code for this project is structured as follows:

* `notebooks` contains example notebooks of pipelines. It also contains two notebooks for pulling data into a DSVM (one for loading it from your local->Azure blob, and one for Azure blob -> DSVM).
* `src` contains code to support these pipelines
* `models` stores models that have been built. Should not be sent to github.

## Requirements

* This project is built in python. Use `pip install -r requirements.txt` to get all the required packages. I am not currently focused on setting up tidy virtual environments, but this should at least get any missing packages installed into the VMs.
* To update the `requirements.txt` file, make sure you have pipreqs installed and then run `pipreqs ./ --scan-notebooks --force` from the command line. This will make sure that all utilized packages are included in the requirements file.
* Note you might need to separately install transformers to make sure that proper version installs: `pip install transformers[torch]`. This sets it up so that you can use the Training class, which is a lightweight way to easily produce training pipelines.
* If you're having troubles with the umap-learn package, try installing llvmlite and numba separately first before installing umap. `pip install --upgrade llvmlite numba` followed by `pip install umap-learn`.

## Project Status

This project is currently in development and experimental.

## Getting Help or Reporting an Issue

To report bugs/issues/feature requests, please file an [issue](https://github.com/lindsay-fredrick/basic-nlp-testing/issues/).

## How to Contribute

If you would like to contribute, please see our [CONTRIBUTING](CONTRIBUTING.md) guidelines.

Please note that this project is released with a [Contributor Code of Conduct](CODE_OF_CONDUCT.md). By participating in this project you agree to abide by its terms.

## License

```
Copyright 2025 Province of British Columbia

Licensed under the Apache License, Version 2.0 (the &quot;License&quot;);
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an &quot;AS IS&quot; BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
```
