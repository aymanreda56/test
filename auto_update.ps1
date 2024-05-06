#then do:
curl https://api.github.com/repos/aymanreda56/test/commits/main -H @{"Accept"= "application/json"} 2>&1 | sls "date"
# $RESPONSE = curl -v https://api.github.com/repos/aymanreda56/test/commits/main 2>&1 | grep '"date"'

# Write-Host $RESPONSE