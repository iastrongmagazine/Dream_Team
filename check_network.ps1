# Check active network adapters
Get-NetAdapter | Where-Object { $_.Status -eq 'Up' } | Select-Object Name, InterfaceDescription

# Check for TAP adapters (VPN)
Get-NetAdapter | Where-Object { $_.Name -like '*TAP*' -or $_.Name -like '*Tun*' -or $_.Name -like '*VPN*' } | Select-Object Name, Status

# Check default route
$routes = Get-NetRoute -DestinationPrefix '0.0.0.0/0' | Select-Object InterfaceAlias, NextHop
$routes
