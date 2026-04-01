#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
67_Retry_Decorator.py
======================
Decorador de retry con exponential backoff para auto-remediation.

Uso:
    from 67_Retry_Decorator import retry_on_failure

    @retry_on_failure(max_retries=3, backoff=2)
    def mi_funcion():
        ...
"""

import time
import functools
from typing import Callable, Optional, Tuple
import sys

# ============================================================
# CONFIGURACIÓN
# ============================================================

if sys.stdout.encoding != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except:
        pass


# ============================================================
# DECORADOR
# ============================================================


def retry_on_failure(
    max_retries: int = 3,
    backoff: float = 2.0,
    exceptions: Tuple = (Exception,),
    on_retry: Optional[Callable] = None,
):
    """
    Decorador que reintenta una función si falla.

    Args:
        max_retries: Número máximo de reintentos (default: 3)
        backoff: Factor de exponential backoff (default: 2.0)
        exceptions: Tupla de excepciones que disparan retry
        on_retry: Callback opcional called en cada retry

    Returns:
        Función decorada

    Example:
        @retry_on_failure(max_retries=3, backoff=2)
        def fetch_data():
            return requests.get(url)
    """

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None

            for attempt in range(max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e

                    if attempt < max_retries:
                        wait_time = backoff**attempt
                        print(
                            f"[RETRY] {func.__name__} falló (intento {attempt + 1}/{max_retries + 1})"
                        )
                        print(f"        Reintentando en {wait_time}s... Error: {e}")

                        if on_retry:
                            on_retry(func, attempt, e)

                        time.sleep(wait_time)
                    else:
                        print(
                            f"[ERROR] {func.__name__} falló definitivamente después de {max_retries + 1} intentos"
                        )
                        print(f"        Último error: {e}")

            raise last_exception

        return wrapper

    return decorator


# ============================================================
# AUTO-REMEDIATION HELPERS
# ============================================================


def auto_remediate_script(script_path: str, max_retries: int = 2) -> bool:
    """
    Intenta remediar un script ejecutándolo múltiples veces.

    Args:
        script_path: Path al script
        max_retries: Número de reintentos

    Returns:
        True si exitoso, False si falló
    """
    import subprocess

    @retry_on_failure(max_retries=max_retries, backoff=1.5)
    def run_script():
        result = subprocess.run(
            [sys.executable, script_path], capture_output=True, text=True
        )
        if result.returncode != 0:
            raise RuntimeError(result.stderr)
        return result

    try:
        run_script()
        return True
    except Exception as e:
        print(f"[AUTO-REMEDIATION] Falló para {script_path}: {e}")
        return False


# ============================================================
# CLI
# ============================================================


def main():
    """Test del decorator."""
    print("Testing Retry Decorator...")

    # Test 1: Función que falla y luego succeed
    call_count = [0]

    @retry_on_failure(max_retries=3, backoff=0.1)
    def flaky_function():
        call_count[0] += 1
        if call_count[0] < 3:
            raise ValueError(f"Intento {call_count[0]} falló")
        return "SUCCESS"

    result = flaky_function()
    print(f"Test 1: {result} (llamadas: {call_count[0]})")
    assert result == "SUCCESS"

    # Test 2: Función que siempre falla
    @retry_on_failure(max_retries=2, backoff=0.1)
    def always_fails():
        raise RuntimeError("Siempre falla")

    try:
        always_fails()
        assert False, "Debería haber fallado"
    except RuntimeError:
        print("Test 2: Correctamente lanzó excepción después de retries")

    print("\n[OK] Todos los tests pasaron!")


if __name__ == "__main__":
    main()
