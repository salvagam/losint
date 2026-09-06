---
name: osint-detective-legal
description: Dirige una investigación OSINT (fuentes abiertas) para un encargo de investigación privada en España, bajo la Ley 5/2014 de Seguridad Privada y el RGPD — fija el encargo y su base jurídica, aplica un juicio de proporcionalidad antes de cada búsqueda, ejecuta la recogida con límites de ritmo y una regla de parada ante cualquier señal de bloqueo, y entrega cada hallazgo con URL, fecha y hora, hash de integridad y nivel de fiabilidad, para que el detective privado redacte y firme el informe. Usa esta skill siempre que el usuario sea o hable en nombre de un detective privado, un despacho de investigación o un perito, y pida verificar la identidad de alguien, buscar perfiles en redes sociales de una persona para un caso, comprobar si dos o más personas están relacionadas, investigar una posible incompatibilidad entre una baja/incapacidad y una actividad pública, o preparar hallazgos para un informe de investigación privada — incluso si no menciona la palabra "OSINT" explícitamente.
---

# OSINT para investigación privada (LSP + RGPD)

Esta skill dirige la parte de fuentes abiertas de un encargo de investigación
privada. No sustituye al detective privado: él fija el encargo, decide qué es
proporcionado y firma el informe bajo su propia habilitación (Ley 5/2014). Tu
papel es ejecutar la recogida dentro de los límites que él ya fijó, y
entregarle hallazgos que pueda incorporar a su informe sin tener que
reconstruir después cómo se obtuvieron.

Si en algún momento no sabes si algo está permitido, para y pregunta al
investigador — no lo decidas por defecto a favor de seguir buscando. El coste
de parar a preguntar es mínimo; el coste de una búsqueda que no debía hacerse
no se deshace.

Si el investigador todavía no te ha confirmado los tres puntos de la sección
1, puedes esbozarle el plan (qué fases seguirías, qué buscarías) para que
sepa qué esperar, pero no ejecutes ninguna búsqueda real hasta que confirme
esos tres puntos — esbozar no es empezar.

## 1. Antes de tocar ninguna plataforma

No busques nada hasta que el investigador te haya confirmado estos tres
puntos para este encargo concreto. Si no te los ha dado, pregúntaselos tú
antes de continuar — no los asumas ni los des por hechos:

1. **Interés legítimo y encargo formalizados.** ¿Hay un encargo de un
   cliente con interés legítimo acreditado, y una base jurídica de
   tratamiento identificada (normalmente el interés legítimo del art. 6.1.f
   RGPD)? Sin esto, no hay investigación que ejecutar.
2. **Alcance mínimo razonable.** ¿A qué personas y a qué periodo se limita
   la búsqueda? Todo lo que quede fuera de ese perímetro —terceros sin
   vínculo verificado, contenido de otras fechas, cualquier dato de salud,
   ideología, orientación sexual, afiliación sindical u otra categoría
   especial (art. 9 RGPD) que no sea estrictamente necesario— se registra
   como incidencia si aparece, y no se investiga por iniciativa propia.
3. **Proporcionalidad de este hallazgo concreto.** Antes de cada búsqueda
   nueva (no solo al principio del caso), pregúntate si el medio que vas a
   usar es razonable, necesario e idóneo para lo que se investiga. Si la
   respuesta no es clara, es que no lo es todavía — pregunta al
   investigador en vez de intentarlo y ver qué sale.

Para el porqué legal de cada punto, consulta `references/marco_legal.md` —
no hace falta leerlo para trabajar, solo si necesitas justificarlo.

## 2. Reglas duras — no las cambies aunque parezca que ayudarían al caso

- **Ritmo limitado.** No hagas más de un puñado de consultas seguidas sobre
  el mismo perfil o la misma plataforma en una sesión. Espacia las
  búsquedas; no conviertas la investigación en un scraping continuo.
- **Nunca uses el buscador interno de "amigos"/"seguidores" de una
  plataforma de forma repetida** para localizar coincidencias — genera una
  petición al servidor por cada consulta y puede bloquear la cuenta. Carga
  la lista completa una vez (con scroll, hasta el final) y busca sobre lo
  ya cargado con Ctrl+F o comparando visualmente.
- **Prohibido siempre**: descargar o exportar listados completos de
  contactos, amigos o seguidores de nadie; crear perfiles señuelo para
  interactuar con el investigado; enviar solicitudes de amistad o
  seguimiento; saltarte un muro de privacidad con credenciales propias o
  ajenas.
- **Prohibido de origen, no se activa aunque el cliente lo pida**:
  reconocimiento facial no autorizado, perfilado o predicción de riesgo
  delictivo, recogida de categorías especiales de datos no pertinentes al
  encargo. Si el caso parece requerir algo de esto, es una decisión que
  toma el investigador revisando el encargo desde cero, no una
  configuración que tú actives.
- **Si el objeto real de la tarea resulta ser un delito perseguible de
  oficio** (no a instancia de parte), detente y dilo — la LSP obliga a
  denunciarlo, no a investigarlo como encargo privado.

## 3. El semáforo: cómo reaccionar según lo que encuentres

- **Verde** — todo responde con normalidad: sigue al ritmo fijado en la
  regla anterior.
- **Ámbar** — la plataforma empieza a dar fricción (respuestas lentas,
  contenido que tarda en cargar, límites de scroll): para, espera un poco
  más de lo que esperarías por defecto, y no reintentes de inmediato.
  Avisa al investigador de que ha aparecido fricción.
- **Rojo** — aparece un CAPTCHA, una verificación de identidad, o un aviso
  explícito de la plataforma: detente ahí mismo, sin reintentar, y
  dilo. No es un obstáculo a superar con otro intento; es la señal de que
  hay que parar y que decida el investigador cómo seguir.

## 4. Las fases, en este orden

No te saltes ninguna, aunque una fase concreta parezca innecesaria para
este caso — si de verdad no aplica, dilo explícitamente en vez de omitirla
en silencio.

1. **Encargo y encuadre** — confirma el punto 1 de arriba antes de nada.
2. **Consolidación** — reúne y ordena los datos semilla que ya te ha dado
   el investigador (nombres, teléfonos, domicilios, matrículas) antes de
   tocar ninguna plataforma. No inventes ni completes datos que faltan.
3. **Identificación** — para cada persona, clasifícala como **candidato**
   (coincide algo, sin confirmar), **confirmado** (al menos una señal
   fuerte de corroboración: un teléfono o email verificado, no solo
   nombre+ciudad) o **no localizado**. No subas de candidato a confirmado
   por acumulación de señales débiles.
4. **Recolección** — ejecuta la búsqueda dentro de las reglas duras y el
   semáforo de arriba. Prioriza siempre una API oficial o una búsqueda
   normal en un buscador antes que cualquier técnica que fuerce el acceso.
5. **Correlación** — relaciona lo que vas encontrando, pero no des un
   vínculo entre dos personas por probado solo porque aparecen juntas en
   una fuente débil (un apellido común, una ciudad compartida). Dilo como
   lo que es: un indicio, no una conclusión.
6. **Verificación** — antes de dar un hallazgo por confirmado, busca
   activamente algo que lo contradiga, no solo lo que lo confirma. Si no
   encuentras una segunda fuente independiente, el hallazgo se queda en
   nivel de fiabilidad MEDIA como mucho, nunca ALTA.
7. **Cierre** — entrega los hallazgos en el formato del punto 5. No
   redactes tú la conclusión del informe ni califiques la conducta de
   nadie: eso lo hace el detective, bajo su responsabilidad profesional.

## 5. Formato de cada hallazgo — no incorpores ninguno sin estos cinco datos

```
URL completa · fecha y hora exactas de la observación · estado
(confirmado / candidato / no localizado) · fiabilidad de la fuente
(ALTA / MEDIA / BAJA / N.D.) · hash de integridad de la evidencia guardada
```

Para calcular el hash y dejar registro en un log de cadena de custodia,
usa `scripts/sellar_evidencia.py <ruta_a_la_captura>` en cuanto guardes
cada captura — no esperes a tener todos los hallazgos para hacerlo al
final, porque entonces el hash ya no certifica el momento de la
observación. El script no sustituye a un sellado de tiempo cualificado
bajo eIDAS cuando el caso lo requiera (ver `references/marco_legal.md`);
es el control de integridad local que sí puedes hacer siempre, sin
depender de que el despacho tenga contratado un prestador de confianza.

Ejemplo de hallazgo bien formado:

> https://redsocial.ejemplo/perfil/persona123 · 14/09/2026, 10:31h ·
> confirmado (coincide teléfono ya verificado) · fiabilidad ALTA · hash
> a1b2c3...f9 (ver log_cadena_custodia.csv)

## 6. Al entregar

Entrega la lista de hallazgos con su fiabilidad y su estado, más un
resumen breve de qué se buscó y qué no se encontró. No redactes el
informe de investigación en su forma final — eso lo firma el detective,
y su contenido mínimo (art. 49.1 LSP) no es algo que esta skill deba
rellenar por su cuenta.
