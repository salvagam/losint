#!/usr/bin/env python3
"""
sellar_evidencia.py — calcula el hash SHA-256 de un fichero de evidencia (captura,
PDF, etc.) en el momento de su observación, y registra la línea en un log de
cadena de custodia en formato CSV (una fila por evidencia, de solo-añadir).

Uso:
    python3 sellar_evidencia.py <ruta_al_fichero> [--expediente EXPEDIENTE] [--nota "texto libre"]

No sustituye a un sellado de tiempo cualificado bajo eIDAS emitido por un
tercero de confianza (ver references/marco_legal.md) — es la comprobación de
integridad local que se hace en el momento de la captura, antes de incorporar
la evidencia al informe.
"""
import argparse
import csv
import hashlib
import os
import sys
from datetime import datetime, timezone

LOG_NAME = "log_cadena_custodia.csv"


def sha256_de(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    ap = argparse.ArgumentParser(description="Sella una evidencia con hash SHA-256 y fecha/hora, y la registra en el log de cadena de custodia.")
    ap.add_argument("fichero", help="Ruta al fichero de evidencia (captura, PDF, etc.)")
    ap.add_argument("--expediente", default="", help="Referencia del expediente (opcional)")
    ap.add_argument("--nota", default="", help="Nota breve sobre qué es esta evidencia (opcional)")
    ap.add_argument("--log-dir", default=".", help="Carpeta donde vive/se crea el log CSV (por defecto, la actual)")
    args = ap.parse_args()

    if not os.path.isfile(args.fichero):
        print(f"ERROR: no existe el fichero '{args.fichero}'", file=sys.stderr)
        sys.exit(1)

    hash_valor = sha256_de(args.fichero)
    momento = datetime.now(timezone.utc).isoformat(timespec="seconds")
    tamano = os.path.getsize(args.fichero)
    log_path = os.path.join(args.log_dir, LOG_NAME)
    existe = os.path.isfile(log_path)

    with open(log_path, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if not existe:
            w.writerow(["fecha_hora_utc", "expediente", "fichero", "tamano_bytes", "sha256", "nota"])
        w.writerow([momento, args.expediente, os.path.basename(args.fichero), tamano, hash_valor, args.nota])

    print(f"Fichero:      {args.fichero}")
    print(f"Fecha/hora:   {momento} (UTC)")
    print(f"SHA-256:      {hash_valor}")
    print(f"Registrado en: {log_path}")
    print()
    print("Este hash certifica la integridad del fichero comparado a partir de este")
    print("momento. Por sí solo NO acredita quién lo creó, ni la fecha frente a un")
    print("tercero que impugne la integridad de buena fe — para eso hace falta un")
    print("sellado de tiempo cualificado bajo eIDAS emitido por un prestador de")
    print("confianza (ver references/marco_legal.md).")


if __name__ == "__main__":
    main()
