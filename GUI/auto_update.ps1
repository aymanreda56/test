#then do:
$RESPONSE = curl "https://api.github.com/repos/aymanreda56/test/commits" -H @{"Accept" = "application/json"} | Select-String 'date'

Write-Host $RESPONSE
# $RESPONSE = curl -v https://api.github.com/repos/aymanreda56/test/commits/main 2>&1 | grep '"date"'

# Write-Host $RESPONSE