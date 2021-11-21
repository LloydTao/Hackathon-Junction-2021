
# data_science

## Build Setup Server

```bash
# install jupyter_kernel_gateway
$pip install jupyter_kernel_gateway
$jupyter kernelgateway --generate-config
# to allow access from other machines edit file
$ ~/.jupyter/jupyter_kernel_gateway_config.py 
# such that 
$ c.KernelGatewayApp.ip = '127.0.0.1'
# is now
$ KernelGatewayApp.ip = '*'
$ jupyter kernelgateway --KernelGatewayApp.api='kernel_gateway.notebook_http' --KernelGatewayApp.seed_uri='/PATHOFAPI/.ipynb'
# setup server
```

### `API.ipynb`

Jupyter notebook, containing python script, containing the machine learning model and functions to train and update the model along with the API routes.

### `clean_words.csv`

Dataset of clean words, to be used to replace detected hate speech.

### `labeled_data_original_csv`

Dataset of labeled tweets, labelled 0 for hate speech, 1 for offensive and 2 for neither. 

