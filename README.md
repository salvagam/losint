# L-OSINT · Recursos del manual *L-OSINT-IA*

Material complementario del libro **L-OSINT-IA. El arte de la ciberinvestigación y el OSINT en tiempos de IA**
(Salvador Gamero Casado, autor del método · Manuela Díaz Noa, coautora del marco jurídico). Primera edición, septiembre de 2026.

Este repositorio contiene la **skill compañera** que describe el Anexo I del manual: un conjunto de instrucciones
para que un agente de IA (Claude) ejecute la parte de fuentes abiertas de un encargo de investigación privada en España
dentro de los límites de la Ley 5/2014 de Seguridad Privada y del RGPD, y entregue cada hallazgo con URL, fecha y hora,
estado de atribución, fiabilidad y hash de integridad, para que el detective privado redacte y firme el informe.

## Contenido

```
osint-detective-legal/
├── SKILL.md                      # instrucciones de la skill (nombre, descripción, reglas duras, semáforo, fases, formato)
├── references/marco_legal.md     # referencia legal breve (LSP, RGPD, LEC, eIDAS) para justificar decisiones
└── scripts/sellar_evidencia.py   # hash SHA-256 + log CSV de cadena de custodia en el momento de la captura
osint-detective-legal.skill       # el mismo contenido empaquetado (zip) para subirlo a Claude
```

## Instalación

- **Claude (web, app de escritorio o Cowork):** Ajustes → Funciones → subir `osint-detective-legal.skill`.
  Requiere un plan con ejecución de código habilitada; queda instalada solo en tu cuenta.
- **Claude Code:** descomprime el paquete dentro de `~/.claude/skills/` (disponible en todos los proyectos)
  o de `.claude/skills/` de un proyecto concreto.

Una vez instalada no hace falta invocarla por su nombre: basta describir el encargo como a cualquier colaborador.

Para regenerar el paquete tras modificar la skill:

```bash
zip -r osint-detective-legal.skill osint-detective-legal/
```

## Qué no es

- No es una herramienta de scraping ni salta ninguna barrera técnica: la regla del semáforo obliga a parar ante cualquier señal de bloqueo.
- No redacta el informe de investigación ni califica la conducta de nadie: eso lo hace el detective bajo su habilitación.
- No sustituye a un sellado de tiempo cualificado bajo eIDAS: el script calcula un hash local de integridad y lo registra; el sellado por un prestador cualificado es otra cosa (Capítulo 27 del manual).
- Seguir este método **no es condición de validez** de ningún informe de investigación (Capítulo 28.4 del manual).

## Alcance y límites

El material se publica tal como se cerró en septiembre de 2026. Las plataformas, las herramientas de IA y la normativa
cambian; los autores mantendrán estos recursos mientras consideren que el contenido del manual sigue vigente, sin
garantizar su disponibilidad más allá de ese momento. Nada de lo aquí publicado es asesoramiento jurídico para un caso concreto.

Página de arranque: **http://losint.es** · Directorio de herramientas: https://start.me/p/w9XbpY/losint

Erratas, sugerencias y adaptaciones: abre un *issue* en este repositorio.

## Licencia

La skill (este repositorio) se publica bajo licencia [MIT](LICENSE): puedes usarla y adaptarla a la práctica de tu despacho
citando la autoría. El texto del manual *L-OSINT-IA* no forma parte de esta licencia y conserva todos los derechos reservados.
