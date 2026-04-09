# Alternative approach - Change interface metric to prefer VPN
Write-Host "=== Method 2: Changing Interface Metric ==="

# Get both interfaces
$wifi = Get-NetAdapter | Where-Object { $_.Name -like '*Wi-Fi*' }
$vpn = Get-NetAdapter | Where-Object { $_.Name -like '*Radmin*' }

Write-Host "Wi-Fi: $($wifi.Name) - Index: $($wifi.ifIndex)"
Write-Host "VPN: $($vpn.Name) - Index: $($vpn.ifIndex)"

# Set interface metric (lower = more preferred)
# Wi-Fi should have higher metric (less preferred)
Set-NetIPInterface -InterfaceIndex $wifi.ifIndex -InterfaceMetric 100 -ErrorAction SilentlyContinue
Set-NetIPInterface -InterfaceIndex $vpn.ifIndex -InterfaceMetric 10 -ErrorAction SilentlyContinue

Write-Host "`n=== New metrics ==="
Get-NetIPInterface | Where-Object { $_.AddressFamily -eq 'IPv4' } | Select-Object InterfaceAlias, InterfaceMetric, ConnectionState | Format-Table

Write-Host "`n=== Test IP ==="
$ip = (Invoke-WebRequest -Uri 'https://api.ipify.org' -UseBasicParsing -TimeoutSec 10).Content
Write-Host "Your IP: $ip"
