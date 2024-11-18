
FROM gitpod/workspace-full:latest

# Install project-specific dependencies
RUN apt-get update && apt-get install -y python3 python3-pip
