# AUDITORÍA DE RUTAS DE SKILLS - DRY RUN
# ======================================
# Refactorizar: .agent/02_Skills/ -> 01_Core/03_Skills/
# 
# Ejecutar con: powershell -ExecutionPolicy Bypass -File audit_skills_routes.ps1
# 
# Este script hace DRY RUN - lista lo que cambiaría SIN modificar archivos

$ErrorActionPreference = "Continue"
$ROOT = "C:\Users\sebas\Downloads\01 Revisar\09 Versiones\00 Respaldo PC Sebas\01 Github\personal-os\Think_Different"

Write-Host "=" -NoNewline -ForegroundColor Cyan
Write-Host ("=" * 79) -ForegroundColor Cyan
Write-Host "AUDITORIA DE RUTAS DE SKILLS - DRY RUN" -ForegroundColor Cyan
Write-Host ("=" * 80) -ForegroundColor Cyan
Write-Host ""

$OLD_PATH = ".agent/02_Skills/"
$NEW_PATH = "01_Core/03_Skills/"

Write-Host "Ruta Antigua: $OLD_PATH" -ForegroundColor Yellow
Write-Host "Ruta Nueva:   $NEW_PATH" -ForegroundColor Yellow
Write-Host ""

# Buscar referencias usando Select-String (más rápido)
$results = Select-String -Path "$ROOT\*","$ROOT\*\*","$ROOT\*\*\*","$ROOT\*\*\*\*" -Pattern "\.agent/02_Skills/" -Recurse -ErrorAction SilentlyContinue |
    Where-Object { $_.Path -notmatch "\.git|node_modules|\.agent/02_Skills/" } |
    Select-Object Path, LineNumber, Line

$grouped = $results | Group-Object -Property Path

Write-Host "Total archivos con referencias: $($grouped.Count)" -ForegroundColor Cyan
Write-Host "Total-lineas a modificar: $($results.Count)" -ForegroundColor Cyan
Write-Host ""

# Agrupar por extensión
$byExt = @{}
foreach ($r in $results) {
    $ext = [System.IO.Path]::GetExtension($r.Path)
    if (-not $byExt[$ext]) { $byExt[$ext] = 0 }
    $byExt[$ext]++
}

Write-Host "--- Referencias por tipo de archivo ---" -ForegroundColor White
foreach ($e in $byExt.GetEnumerator() | Sort-Object Value -Descending) {
    Write-Host "  $($e.Key): $($e.Value)" 
}
Write-Host ""

# Mostrar primeros 30 archivos
Write-Host "--- Archivos afectados (primeros 30) ---" -ForegroundColor White
$count = 0
foreach ($g in $grouped | Sort-Object Count -Descending) {
    $count++
    if ($count -le 30) {
        $shortPath = $g.Name -replace [regex]::Escape($ROOT), ""
        Write-Host "$count. $shortPath" -ForegroundColor Green
        $g.Group | Select-Object -First 2 | ForEach-Object {
            Write-Host "     L$($_.LineNumber): $($_.Line.Substring(0, [Math]::Min(60, $_.Line.Length)))..." -ForegroundColor Gray
        }
    }
}

if ($grouped.Count -gt 30) {
    Write-Host ""
    Write-Host "... y $($grouped.Count - 30) archivos más" -ForegroundColor Yellow
}

Write-Host ""
Write-Host ("=" * 80) -ForegroundColor Cyan
Write-Host "RESUMEN DE IMPACTO" -ForegroundColor Cyan
Write-Host ("=" * 80) -ForegroundColor Cyan
Write-Host "Archivos a modificar: $($grouped.Count)" -ForegroundColor White
Write-Host "Reemplazos totales: $($results.Count)" -ForegroundColor White
Write-Host ""
Write-Host "RIESGO: La mayoría son DOCUMENTACION que referencia la estructura" -ForegroundColor Yellow
Write-Host "        NO código que llama las skills directamente." -ForegroundColor Yellow
Write-Host ""

# Generar lista para migración
$outputFile = "$ROOT\08_Scripts_Os\12_Audits\migrate_list.txt"
$grouped.Name | Out-File -FilePath $outputFile -Encoding UTF8
Write-Host "Lista de archivos guardada en: $outputFile" -ForegroundColor Cyan

# Generar script de migración
$scriptContent = @"
# Script de Migración - EJECUTAR SOLO DESPUES DE APROBACION
# ==========================================================

`$OLD_PATH = ".agent/02_Skills/"
`$NEW_PATH = "01_Core/03_Skills/"

# Cambiar a `$true para ejecutar
`$DRY_RUN = `$true

`$files = @(
"@

foreach ($f in $grouped.Name) {
    $shortPath = $f -replace [regex]::Escape($ROOT), ""
    $scriptContent += "    `"$shortPath`",`n"
}

$scriptContent += @"
)

if (`$DRY_RUN) {
    Write-Host "DRY RUN - No se.modifico nada" -ForegroundColor Yellow
} else {
    foreach (`$file in `$files) {
        `$fullPath = Join-Path `$ROOT `$file
        if (Test-Path `$fullPath) {
            (Get-Content `$fullPath -Raw) -replace [regex]::Escape(`$OLD_PATH), `$NEW_PATH | 
                Set-Content `$fullPath -NoNewline
            Write-Host "Updated: `$file" -ForegroundColor Green
        }
    }
}
"@

$scriptFile = "$ROOT\08_Scripts_Os\12_Audits\migrate_skills_routes.ps1"
$scriptContent | Out-File -FilePath $scriptFile -Encoding UTF8
Write-Host "Script de migracion guardado en: $scriptFile" -ForegroundColor Cyan
Write-Host ""
Write-Host "EJECUTAR: Editar `$DRY_RUN = `$false y ejecutar el script" -ForegroundColor Yellow
