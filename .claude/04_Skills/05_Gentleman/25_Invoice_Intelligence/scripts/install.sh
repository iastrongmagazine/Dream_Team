#!/bin/bash

# Script de Instalación Automática
# Sistema de Procesamiento de Facturas con OCR

set -e

echo "========================================"
echo "📦 Instalación del Sistema de Facturas"
echo "========================================"
echo ""

# Detectar sistema operativo
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    OS="linux"
    echo "🐧 Sistema detectado: Linux"
elif [[ "$OSTYPE" == "darwin"* ]]; then
    OS="macos"
    echo "🍎 Sistema detectado: macOS"
else
    OS="unknown"
    echo "⚠️ Sistema operativo no soportado automáticamente"
    echo "Por favor instala manualmente:"
    echo "  - Tesseract OCR"
    echo "  - Poppler utils"
    exit 1
fi

echo ""

# Instalar dependencias del sistema
echo "📥 Instalando dependencias del sistema..."
echo ""

if [ "$OS" = "linux" ]; then
    echo "Ejecutando: sudo apt-get install..."
    sudo apt-get update
    sudo apt-get install -y \
        tesseract-ocr \
        tesseract-ocr-spa \
        tesseract-ocr-eng \
        poppler-utils \
        python3-pip \
        python3-dev

elif [ "$OS" = "macos" ]; then
    echo "Verificando Homebrew..."
    if ! command -v brew &> /dev/null; then
        echo "❌ Homebrew no encontrado. Por favor instala Homebrew primero:"
        echo "   /bin/bash -c \"\$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\""
        exit 1
    fi

    echo "Instalando con Homebrew..."
    brew install tesseract tesseract-lang poppler
fi

echo ""
echo "✅ Dependencias del sistema instaladas"
echo ""

# Verificar instalación de Tesseract
echo "🔍 Verificando Tesseract..."
if command -v tesseract &> /dev/null; then
    TESSERACT_VERSION=$(tesseract --version | head -n 1)
    echo "✅ $TESSERACT_VERSION"

    echo "Idiomas disponibles:"
    tesseract --list-langs | grep -E "(spa|eng)" || echo "⚠️ Idiomas español/inglés no encontrados"
else
    echo "❌ Tesseract no encontrado"
    exit 1
fi

echo ""

# Instalar dependencias de Python
echo "🐍 Instalando dependencias de Python..."
echo ""

if [ -f "requirements.txt" ]; then
    pip3 install -r requirements.txt --break-system-packages || \
    pip3 install -r requirements.txt --user
else
    echo "⚠️ requirements.txt no encontrado"
    echo "Instalando paquetes manualmente..."
    pip3 install \
        pypdf==4.0.1 \
        pdfplumber==0.11.0 \
        pytesseract==0.3.10 \
        pdf2image==1.17.0 \
        Pillow==10.2.0 \
        pandas==2.2.0 \
        openpyxl==3.1.2 \
        --break-system-packages || \
    pip3 install \
        pypdf \
        pdfplumber \
        pytesseract \
        pdf2image \
        Pillow \
        pandas \
        openpyxl \
        --user
fi

echo ""
echo "✅ Dependencias de Python instaladas"
echo ""

# Verificar instalación
echo "🧪 Verificando instalación..."
echo ""

python3 -c "import pypdf; print('✅ pypdf')" 2>/dev/null || echo "❌ pypdf"
python3 -c "import pdfplumber; print('✅ pdfplumber')" 2>/dev/null || echo "❌ pdfplumber"
python3 -c "import pytesseract; print('✅ pytesseract')" 2>/dev/null || echo "❌ pytesseract"
python3 -c "import pdf2image; print('✅ pdf2image')" 2>/dev/null || echo "❌ pdf2image"
python3 -c "import pandas; print('✅ pandas')" 2>/dev/null || echo "❌ pandas"

echo ""

# Hacer scripts ejecutables
if [ -f "invoice_processor.py" ]; then
    chmod +x invoice_processor.py
    echo "✅ invoice_processor.py configurado"
fi

if [ -f "test_invoice_system.py" ]; then
    chmod +x test_invoice_system.py
    echo "✅ test_invoice_system.py configurado"
fi

echo ""
echo "========================================="
echo "✅ INSTALACIÓN COMPLETADA"
echo "========================================="
echo ""
echo "🚀 Para empezar:"
echo ""
echo "1. Generar facturas de prueba:"
echo "   python3 test_invoice_system.py generate 10"
echo ""
echo "2. Ejecutar prueba completa:"
echo "   python3 test_invoice_system.py test"
echo ""
echo "3. Procesar tus facturas:"
echo "   python3 invoice_processor.py ./ruta/a/facturas"
echo ""
echo "📖 Documentación completa en README.md"
echo ""
