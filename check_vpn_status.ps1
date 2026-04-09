# Check what Radmin VPN is actually doing
Write-Host "=== Radmin VPN Status ==="
$vpn = Get-NetAdapter | Where-Object { $_.Name -like '*Radmin*' }
$vpn | Format-List *

Write-Host "`n=== VPN IP Configuration ==="
Get-NetIPAddress -InterfaceIndex $vpn.ifIndex -AddressFamily IPv4 | Select-Object IPAddress, PrefixLength

Write-Host "`n=== Ping test through VPN ==="
Test-NetConnection -ComputerName 8.8.8.8 -InterfaceIndex $vpn.ifIndex -InformationLevel Detailed | Select-Object ComputerName, RemoteAddress, InterfaceAlias, TcpTestSucceeded

Write-Host "`n=== Check if VPN has actual internet access ==="
Test-NetConnection -ComputerName google.com -InterfaceIndex $vpn.ifIndex -InformationLevel Detailed
