import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
dotenv_path = Path(__file__).parent.parent / '.env'
load_dotenv(dotenv_path)

# AWS region - loaded from .env
REGION = os.getenv('REGION', 'us-east-1')

# File path for TVM values
TVM_VALUES_FILE = 'tvm_values.json'

# Email address for credentials
DEFAULT_EMAIL = "john_doe@email.com"

# Base model ARN for Bedrock
BASE_MODEL_ARN = "arn:aws:bedrock:us-east-1::foundation-model/amazon.nova-pro-v1:0"

# Tags for inference profile
INFERENCE_PROFILE_TAGS = [{'key': 'dept', 'value': 'supportengineering'}]

# Inference profile name
INFERENCE_PROFILE_NAME = "nova_pro_profile"

# System prompt for IT ticket questions
SYSTEM_PROMPT = """
You are a helpful AI assistant who answers question correctly and accurately about a AcmeCompany's IT tickets. 
You answer in the format as follows:
<response>
    <datasource> 
    </datasource>
    <generalknowledge> 
    </generalknowledge>
</response>

** For datasource section: **
    Do not makeup answers and only answer from the provided knowledge. 
    If the query doesn't has any Info about IT Tickets, you must acknowledge that. 
** For  generalknowledge section: **
    Provide info you generally aware of on addressing the query.
"""

# Default query
DEFAULT_QUERY = "What is the typical reason of company keyboards not working?"

# Max results for search
MAX_SEARCH_RESULTS = 5

# Q Business application name - loaded from .env
Q_BUSINESS_APP_NAME = os.getenv('Q_BUSINESS_APP_NAME', 'q-business-1')