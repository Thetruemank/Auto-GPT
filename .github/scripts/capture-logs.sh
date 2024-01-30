#!/bin/bash

# Capture system logs
journalctl > action-logs.txt

# Capture Docker container logs if Docker is present
if command -v docker &> /dev/null; then
    docker ps -aq | xargs -I {} sh -c 'echo "Container {} logs:" >> action-logs.txt; docker logs {} >> action-logs.txt'
fi

# Capture application-specific logs
cat /path/to/application/log/file.log >> action-logs.txt

# Output the location of the logs
echo "Logs captured in action-logs.txt"
