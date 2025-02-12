# basic-nlp-testing
Space to test some basic NLP models and their speeds on various compute configurations. 

## Overview

This code supports some basic NLP pipelines to test how well they work in different compute configurations. 

## Usage

* Notebooks should be able to run individually. If missing, place a `config.py` file into your `src` folder that contains a `data_path` variable, as well as any required variables to import data into the Azure storage blob (a `blob_service_sas_url`). 

## Structure

Code for this project is structured as follows:

* `notebooks` contains example notebooks of pipelines
* `src` contains code to support these pipelines 
* `models` stores models that have been built. Should not be sent to github. 

## Requirements

* This project is built in python. Use `pip install -r requirements.txt` to get all the required packages. I am not currently focused on setting up tidy virtual environments, but this should at least get any missing packages installed into the VMs. 
* To update the `requirements.txt` file, make sure you have pipreqs installed and then run `pipreqs ./ --scan-notebooks --force` from the command line. This will make sure that all utilized packages are included in the requirements file. 
* Note you might need to separately install transformers to make sure that proper version installs: `pip install transformers[torch]`. This sets it up so that you can use the Training class, which is a lightweight way to easily produce training pipelines. 
    
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
