# Force all traffic through Radmin VPN
# This removes the default route through Wi-Fi and only uses VPN

Write-Host "=== Current Routes ==="
Get-NetRoute -DestinationPrefix '0.0.0.0/0' | Select-Object InterfaceAlias, NextHop, RouteMetric | Format-Table

Write-Host "`n=== Setting VPN as default gateway ==="

# Get VPN interface index
$vpnInterface = Get-NetAdapter | Where-Object { $_.Name -like '*Radmin*' }
if ($vpnInterface) {
    Write-Host "Radmin VPN Interface Index: $($vpnInterface.ifIndex)"
    
    # Remove existing default route
    Remove-NetRoute -DestinationPrefix '0.0.0.0/0' -Confirm:$false -ErrorAction SilentlyContinue
    Write-Host "Removed old default routes"
    
    # Add new default route via VPN (lower metric = preferred)
    New-NetRoute -DestinationPrefix '0.0.0.0/0' -InterfaceIndex $vpnInterface.ifIndex -RouteMetric 100 -ErrorAction SilentlyContinue
    Write-Host "Added new default route through VPN"
} else {
    Write-Host "Radmin VPN not found! Using alternative method..."
}

Write-Host "`n=== New Routes ==="
Get-NetRoute -DestinationPrefix '0.0.0.0/0' | Select-Object InterfaceAlias, NextHop, RouteMetric | Format-Table

Write-Host "`n=== Testing IP ==="
Start-Sleep -Seconds 2
try {
    $ip = (Invoke-WebRequest -Uri 'https://api.ipify.org' -UseBasicParsing -TimeoutSec 10).Content
    Write-Host "Your IP: $ip"
} catch {
    Write-Host "Could not reach ipify: $_"
}
