import boto3

# Create an AWS ECR client
ecr_client = boto3.client('ecr')

# Define the name for the ECR repository
repository_name = "my_monitoring_app_image"

# Create the ECR repository
response = ecr_client.create_repository(repositoryName=repository_name)

# Extract the repository URI from the response
repository_uri = response['repository']['repositoryUri']

# Print the repository URI
print(repository_uri)
