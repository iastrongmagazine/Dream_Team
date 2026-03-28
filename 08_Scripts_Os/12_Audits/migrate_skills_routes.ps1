# Script de MigraciÃ³n - EJECUTAR SOLO DESPUES DE APROBACION
# ==========================================================

$OLD_PATH = ".agent/02_Skills/"
$NEW_PATH = "01_Core/03_Skills/"

# Cambiar a $true para ejecutar
$DRY_RUN = $true

$files = @()

if ($DRY_RUN) {
    Write-Host "DRY RUN - No se.modifico nada" -ForegroundColor Yellow
} else {
    foreach ($file in $files) {
        $fullPath = Join-Path $ROOT $file
        if (Test-Path $fullPath) {
            (Get-Content $fullPath -Raw) -replace [regex]::Escape($OLD_PATH), $NEW_PATH | 
                Set-Content $fullPath -NoNewline
            Write-Host "Updated: $file" -ForegroundColor Green
        }
    }
}
