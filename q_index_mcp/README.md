# MCP Server using Amazon Q Business Cross App index

This is an MCP (Model Context Provider) server for Acme Company that uses Amazon Q Business' cross-app index.

## Prerequisites

### Upload Data to S3

Upload the files present in `synthetic_data` and `ticket_pdfs` directory to S3 and use this as data source for Q Business APP you create as part of instructions in TVM Set up.

### (Token Vending Machine) TVM Set up

Set up the `amzn-q-auth-tvm` from repository https://github.com/aws-samples/custom-ui-tvm-amazon-q-business 

Copy the contents of `cdk-outputs.json` generated after successful deployment of `amzn-q-auth-tvm` to `tvm_values.json` file of this repository. No need to configure QUI.


## Installing and Configuring Claude Desktop

Download and install [Claude Desktop](https://claude.ai/download)  for your operating system.
Complete the MCP Host setup by following the [For Claude Desktop Users](https://modelcontextprotocol.io/quickstart/user) guide.

Turn off Web Search for grounded responses to the data synced.
