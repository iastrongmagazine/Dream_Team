# Mapa de Normalización de Carpetas

## Carpetas Raíz (CRÍTICAS - No Modificar Numeración)

- `00_Core`
- `01_Brain`
- `04_Operations`
- `03_Knowledge`
- `04_Operations`
- `05_System`
- `06_Archive`
- `07_Projects`

## Subcarpetas (Análisis de Redundancias)

### En `00_Core`: OK (Sin conflictos)

### En `01_Brain`: OK (Sin conflictos)

### En `04_Operations`: OK (Sin conflictos)

### En `03_Knowledge`: **Redundancias Detectadas**
  - Conflicto en prefijo `09_`:
    - `09_Archive_Recovery`
    - `09_Strategic_Plans`

### En `04_Operations`: **Redundancias Detectadas**
  - Conflicto en prefijo `01_`:
    - `01_Brain`
    - `01_Brain_Engine`
    - `01_Validation`
  - Conflicto en prefijo `09_`:
    - `09_Backups`
    - `09_Integrations`

### En `05_System`: OK (Sin conflictos)

### En `06_Archive`: OK (Sin conflictos)

### En `07_Projects`: OK (Sin conflictos)


## Propuesta de Renombramiento Seguro

Se moverán las carpetas redundantes al final de la secuencia numérica de su padre para **no afectar las carpetas críticas intermedias** (ej. `08_Scripts_Os`).

- Rename: `03_Knowledge/13_Strategic_Plans`  -->  `03_Knowledge/13_Strategic_Plans`
- Rename: `04_Operations/11_Brain_Engine`  -->  `04_Operations/11_Brain_Engine`
- Rename: `04_Operations/12_Validation`  -->  `04_Operations/12_Validation`
- Rename: `04_Operations/13_Integrations`  -->  `04_Operations/13_Integrations`
