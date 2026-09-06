# Marco legal de referencia (España/UE)

Consulta este documento solo cuando necesites justificar una decisión ante el
investigador o redactar la parte del informe que cita la norma aplicable. No
hace falta leerlo para ejecutar la investigación — las reglas ya están
traducidas a instrucciones operativas en SKILL.md.

## Ley 5/2014, de Seguridad Privada (LSP)

- **Art. 48** — Servicios de investigación privada: exige interés legítimo
  acreditado del solicitante, respeto a los principios de razonabilidad,
  necesidad, idoneidad y proporcionalidad, y prohíbe investigar la vida íntima
  en domicilios o lugares reservados.
- **Art. 25.1.a** — Obliga a formalizar por escrito un contrato por cada
  servicio de investigación.
- **Art. 25.1.g** — Obliga a archivar y conservar contratos, informes, libros
  y material de imagen/sonido de la actividad profesional.
- **Art. 49** — Informes de investigación: contenido obligatorio (número de
  registro, datos del contratante, objeto, medios utilizados, resultados,
  detectives intervinientes, actuaciones realizadas), minimización de datos
  especialmente protegidos, conservación mínima de 3 años, carácter reservado.
- **Art. 50** — Deber de reserva profesional: solo se facilita el contenido de
  la investigación a quien la encargó y a los órganos judiciales/policiales
  competentes.
- **Art. 10.2 y 37.4** — Prohíbe contratar la investigación de delitos
  perseguibles de oficio; obliga a denunciar de inmediato si aparecen.

## Reglamento General de Protección de Datos (RGPD)

- **Art. 6.1.f** — Base jurídica de interés legítimo: la más habitual para
  encajar la investigación privada; exige un juicio de ponderación
  documentado (LIA — Legitimate Interest Assessment).
- **Art. 9** — Régimen reforzado para categorías especiales de datos (salud,
  ideología, afiliación sindical, orientación sexual, datos biométricos,
  etc.): no se recogen salvo excepción aplicable y estrictamente necesaria.
- **Art. 35** — Evaluación de Impacto (EIPD) completa cuando el tratamiento
  supera ciertos umbrales de riesgo — más exigente que un LIA simple.

## Ley de Enjuiciamiento Civil (LEC) — valor del informe en juicio

- **Art. 380** — Cuando el informe no ha sido reconocido como cierto por
  todas las partes a quienes pudiera perjudicar, su autor debe ser
  interrogado como testigo y ratificarse en su contenido.
- **Art. 370.4** — Régimen del testigo-perito, cuando el informe incorpora
  valoraciones fundadas en conocimientos técnicos.
- **Art. 376** — La prueba testifical se valora según las reglas de la sana
  crítica: el tribunal, no un procedimiento técnico, decide su peso.
- **Art. 335** — Dictamen pericial: exige declaración de objetividad del
  perito (apdo. 2); es un medio de prueba distinto del testifical.

## Nota sobre el sellado de tiempo cualificado (eIDAS)

Un sellado de tiempo cualificado, emitido por un prestador de confianza
autorizado bajo el Reglamento eIDAS, acredita frente a cualquiera —no solo
frente a quien confía en la palabra del investigador— que un fichero
existía, con ese contenido exacto, en un momento dado. El hash SHA-256 que
calcula `scripts/sellar_evidencia.py` es un control de integridad local,
útil desde el primer minuto, pero no sustituye a ese sellado cuando el caso
lo requiera.
