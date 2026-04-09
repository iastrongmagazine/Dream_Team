# Check IP through different methods
Write-Host "=== IP Check ==="
try {
    $ip = (Invoke-WebRequest -Uri 'https://api.ipify.org' -UseBasicParsing -TimeoutSec 5).Content
    Write-Host "IP via ipify: $ip"
} catch {
    Write-Host "ipify failed"
}

Write-Host "`n=== DNS Check ==="
try {
    $dns = Resolve-DnsName -Name 'api.anthropic.com' -Type A -ErrorAction Stop
    $dns | Select-Object IPAddress, Name | Format-Table
} catch {
    Write-Host "DNS resolution failed: $_"
}

Write-Host "`n=== Route Table ==="
Get-NetRoute -DestinationPrefix '0.0.0.0/0' | Select-Object InterfaceAlias, NextHop, RouteMetric | Format-Table
