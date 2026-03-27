### Workflow Platzi

1. Chat Gpt + Prompt Inicial
2. Perplexity - Resultado Anterior
3. Warp
4. Deepwiki
5. Supabase
6. MCP
7. Reglas
8. Memorias
9. Workflow
10. Skills - Como hacerlo Bien
11. Devinreview - Code Review - https://app.devin.ai/review
12. Coderabbit - Review - https://www.coderabbit.ai
13. Vercel - Deploy

---

**IA en desarrollo: de la planificación al deploy

Resumen

Construir un proyecto de software completo integrando inteligencia artificial en cada etapa ya no es una idea futurista, es una práctica que está redefiniendo la productividad de los equipos de desarrollo. Aquí se presenta un enfoque práctico para crear una web desde cero —en este caso, para un club de fútbol— utilizando herramientas de IA que se conectan directamente con el editor, la terminal y la base de datos.

¿Qué conocimientos previos necesitas para trabajar con IA en desarrollo?

Antes de integrar IA en un flujo de trabajo profesional, es fundamental contar con una base sólida. Los requisitos mínimos incluyen:

- **Desarrollo de software básico:** comprensión de estructuras, lógica y buenas prácticas.
- **Manejo de la terminal:** ejecución de comandos, navegación de archivos y automatización.
- **Git y GitHub:** control de versiones, ramas, _commits_ y colaboración remota.
- **Fundamentos de inteligencia artificial:** entender qué puede y qué no puede hacer la IA como asistente de desarrollo.

Sin estos pilares, las herramientas de IA pierden su verdadero potencial. No se trata de copiar y pegar respuestas generadas, sino de **sumar herramientas que se integren con tu flujo de trabajo real** [0:38]. Tener criterio técnico es lo que marca la diferencia entre usar IA de forma eficiente y depender ciegamente de ella.

¿Por qué la IA en desarrollo ya es obligatoria y no opcional?

Se establece una analogía muy clara: la adopción de la IA sigue el mismo patrón que siguió **Git** [1:03]. Al principio parecía algo raro y prescindible, después se convirtió en una recomendación para equipos profesionales, y hoy es un requisito indispensable en cualquier oferta laboral de desarrollo. Con la inteligencia artificial está ocurriendo exactamente lo mismo.

La diferencia entre alguien que **usa bien la IA** y alguien que no ya impacta directamente en la velocidad de entrega, la calidad del código y la capacidad de iterar. Ignorar estas herramientas hoy equivale a haber ignorado el control de versiones hace una década.

¿Qué herramientas de IA se utilizan en cada fase del proyecto?

El flujo cubre desde la planificación hasta el despliegue, y cada etapa incorpora herramientas específicas:

- **Planificación:** se utilizan _Perplexity_ y _Claude_ para investigar, estructurar ideas y definir el alcance del proyecto [1:11].
- **Generación de código:** herramientas como _Claude Code_, _Windsurf_ y _Cursor_ permiten escribir y refactorizar código directamente desde el editor [1:18].
- **Conexión a base de datos:** integración con _Supabase_ sin salir del entorno de desarrollo [1:27].
- **Code review automático:** revisiones de código asistidas por IA con _Devin Review_ y _CodeRabbit_ [1:33].
- **Deploy:** despliegue final del proyecto utilizando _Vercel_ [1:40].

Cada una de estas herramientas cumple un rol concreto. Algunas son gratuitas, otras de pago, pero todas comparten un objetivo: **ahorrar tiempo sin sacrificar calidad**.

¿Cómo se estructura un proyecto real con estas herramientas?

El proyecto consiste en desarrollar una **web para Platzi Fútbol Club** [0:08], un caso práctico que permite mostrar decisiones reales de arquitectura, diseño y despliegue. La propuesta es transparente: ver cada paso, cada decisión técnica y cada herramienta en acción.

Esto significa que no se trata de un ejercicio teórico. Es un flujo completo que va desde la primera conversación con el "cliente" hasta que el sitio está en producción. El enfoque permite entender **cuándo y por qué** usar cada herramienta, no solo el cómo.

¿Cuál es el verdadero valor de integrar IA en tu flujo de desarrollo?

El valor no está en reemplazar al desarrollador, sino en **potenciar cada decisión técnica** con asistencia inteligente. Planificar más rápido, escribir código con menos fricción, revisar _pull requests_ de forma automática y desplegar con confianza son ventajas tangibles que impactan la productividad diaria.

Si ya tienes la base técnica, el siguiente paso es incorporar estas herramientas a tu práctica cotidiana. ¿Cuál de estas herramientas ya conoces o cuál te gustaría probar primero? Comparte tu experiencia.

---

Resumen

Planificar un proyecto de software solía consumir horas de documentación, diagramas y reuniones interminables. Hoy, herramientas como **Perplexity**, **ChatGPT** y **Claude** permiten generar planes detallados, estructuras de sitio y modelos de datos en cuestión de minutos. Aquí se explora paso a paso cómo estas tres plataformas abordan la planificación de un sitio web profesional para un equipo de fútbol ficticio, qué diferencias ofrecen y cuál conviene según el contexto.

¿Cómo preparar el prompt ideal para planificar un proyecto?

Todo comienza con un **prompt bien construido** [0:52]. En lugar de improvisar, se utilizó ChatGPT para generar la instrucción que luego se llevaría a Perplexity. Esa técnica de encadenar herramientas resulta muy práctica: una IA ayuda a formular lo que otra ejecutará mejor.

El prompt incluía un **rol específico**: actuar como _product manager_ y como arquitecto de experiencia de usuario especializado en sitios web de fútbol profesional [1:38]. Definir ese rol desde la primera línea marca la diferencia en la calidad de la respuesta.


Además, se establecieron restricciones claras para mantener el foco:

- Entregar el _site map_ o mapa de sitio con jerarquía de páginas.
- Incluir propósito, público objetivo y modelos de datos sugeridos.
- Separar funcionalidades en fases: **MVP**, versión uno y versión dos.
- No incluir cronograma, _backlog_, tipografías ni contenido ficticio.

Estas restricciones evitan respuestas genéricas y obligan a la IA a concentrarse en la **estructura y especificación** del proyecto.

¿Qué entrega Perplexity como herramienta de planificación?

Perplexity destaca por su capacidad de **búsqueda en internet en tiempo real** [1:05]. Al recibir el prompt, no solo generó el plan, sino que incluyó **fuentes y referencias** de sitios web de clubes profesionales reales. Cada ítem de la respuesta venía acompañado de un número que indica cuántas referencias respaldan ese resultado.

¿Qué elementos específicos generó Perplexity?

La respuesta fue bastante completa [2:46]:

- **Site map completo**: home, secciones principales, árbol de contenidos con niveles jerárquicos.
- **Estructura por página**: detalle de qué contenido va en home, noticias, partidos y cada sección.
- **Modelos de datos mínimos**: campos sugeridos pensados para un CMS con relaciones entre entidades como equipo, plantilla, jugador y _staff_.
- **Navegación**: ítems del _header_ y del _footer_ diferenciados.
- **Funcionalidades por fase**: el MVP incluía bloques dinámicos de noticias, calendario de partidos y fichas simplificadas de jugadores [4:02]. La versión uno agregaba estadísticas, filtros avanzados, multiidioma y sección de socio con _login_. La versión dos proponía estadísticas extendidas, personalización, membresías avanzadas y _video on demand_ [4:45].

Perplexity también recomendó buenas prácticas de accesibilidad, SEO técnico, rendimiento e internacionalización. Introdujo el concepto de contenido **evergreen**, que se refiere a publicaciones que mantienen relevancia incluso cuando el equipo no está en competencia activa [5:13]. Además sugirió un CMS _headless_, un sistema de gestión de contenidos flexible y desacoplado que soporte múltiples tipos de contenido y relaciones entre ellos [5:30].

¿Cómo se comparan ChatGPT y Claude trabajando en paralelo?

Para hacer la comparación más dinámica, se ejecutó el mismo prompt en **Claude** con el modelo Opus 4.6 y en **ChatGPT** con el modelo _Thinking_ 5.2, lado a lado [6:06].

¿Qué diferencias clave aparecieron entre ambos?

**ChatGPT** comenzó a mostrar resultados de inmediato gracias a su modo _Thinking_, que permite ver el proceso de razonamiento mientras genera la respuesta [6:40]. Entregó una especificación por sección detallada, modelos de datos con nombres en inglés entre paréntesis para la base de datos, y separó las funcionalidades en fases con descripciones orientadas al negocio. Se detectó un detalle técnico importante: incluyó acentos en identificadores de base de datos como "competición", algo **no recomendable** en la práctica [7:47]. En la versión dos mencionó _fan engagement_, automatización y un panel editorial con _workflows_ y contenido relacionado automático [8:21].

**Claude**, por su parte, procesó toda la información internamente antes de devolver la respuesta [7:00]. Después de unos minutos generó un **archivo en formato DOC** de veinticuatro páginas sin que se lo pidieran [8:48]. Este documento incluía índice, resumen ejecutivo, trece modelos de datos, navegación completa y separación por fases. Lo más valioso es que ese archivo se puede **descargar directamente o enlazar a Google Drive** con un solo clic [9:35], lo que facilita compartirlo con el equipo por correo, chat o cualquier otro canal.

El modelo de datos de Claude resultó especialmente útil para planificar la base de datos, con nombres de campos listos para implementar [9:53].

¿Cuál herramienta elegir para planificar proyectos?

La comparativa final arroja que cada herramienta tiene su fortaleza [10:10]:

- **Perplexity**: ideal para planes técnicos rápidos con referencias web verificables.
- **Claude**: sobresale al generar documentos descargables y compartibles, listos para revisión en equipo.
- **ChatGPT**: ofrece respuestas detalladas con visibilidad del proceso de razonamiento y especificaciones orientadas a implementación.

No existe una herramienta que sea siempre la mejor. La recomendación es **probar varias** según el proyecto y la etapa del flujo de trabajo en la que te encuentres. Si conoces alguna otra herramienta de planificación que complemente estas tres, compártela en los comentarios para construir un banco de recursos entre todos.


---

Resumen

Convertir un documento de requerimientos en un **plan de ejecución técnico** es uno de los pasos más estratégicos al construir un proyecto con inteligencia artificial. En lugar de generar código directamente desde un chat, existe un camino más eficiente: exportar el plan como archivo Markdown y llevarlo a un editor de código que ofrezca **modo de planificación**. Así se comparan resultados, se elige el mejor y se mantiene el control total del proyecto.

¿Cómo se prepara el archivo de requerimientos para los editores?

Todo parte de una carpeta de trabajo —en este caso llamada _AI Tools_— que contiene un único archivo: el resultado de la sesión anterior con inteligencia artificial, guardado como **Platzi FC requerimiento.md** [01:00]. Ese documento funciona como el requerimiento del cliente e incluye la estructura completa y las limitantes del proyecto. Cualquiera de las herramientas de chat utilizadas previamente puede exportar su resultado en formato Markdown, y ese archivo será la única entrada que necesitan los tres editores.

¿Qué ofrece cada editor en su modo plan?

¿Cómo funciona el modo plan en Claude Code?

Al abrir **Claude Code** desde la terminal, se selecciona el modelo —en este caso _Opus 4.6_ de Anthropic— y se activa el _plan mode_ con el atajo **Shift + Tab** [01:30]. El prompt se escribe en lenguaje natural: se pide crear el plan de ejecución y _stack_ técnico, se referencia el archivo con el símbolo **@** para enlazarlo directamente y se indica que lo guarde como `plan-cc.md` en la carpeta actual.

Cloud Code primero revisa el proyecto, identifica que es nuevo y contiene solo el documento de requerimientos. Luego hace preguntas de contexto —como si se desea usar algún proyecto de referencia— antes de diseñar el plan [02:48]. El resultado es un archivo extenso de **472 líneas** que incluye:

- Estrategia de _branching_ para equipos grandes.
- Estrategia de _testing_ detallada.
- Arquitectura de la **capa de datos** con estructura recomendada para el CMS.
- Recomendaciones de _performance_.
- _Scaffolding_ completo del proyecto.

El archivo se genera inicialmente en el directorio raíz de Cloud Code, por lo que se debe indicar explícitamente que lo mueva a la carpeta del proyecto [04:15].

¿Qué diferencia aporta Cursor con su modo plan?

Dentro de **Cursor**, el directorio ya muestra los archivos existentes. Se cambia del _Agent Mode_ al modo plan también con **Shift + Tab** y se escribe un prompt similar, referenciando el archivo con **@** y solicitando que guarde el resultado como `plan-cursor.md` [05:20].

Cursor lee el archivo de requerimientos y, además, toma como referencia el plan de Cloud Code que ya existe en la carpeta. Su resultado incluye:

- Resumen del requerimiento.
- _Stack_ recomendado para _front-end_, CMS, datos deportivos e infraestructura.
- _Unit tests_ y **Storybook** como catálogo de componentes.
- Estructura de rutas basada en el requerimiento original.
- Fases con entregables y estimación de seis a ocho semanas para el MVP.

Un detalle importante: Cursor primero almacena el plan en su carpeta interna `.cursor/plans` para poder reutilizarlo en otros proyectos [06:40]. Si se desea un archivo Markdown en la raíz, se debe cambiar al **modo agente** y pedirlo explícitamente. El archivo final tiene solo **94 líneas**, el más corto de los tres.

¿Cómo se comporta Windsurf en modo plan?

**Windsurf** introduce su propio flujo a través de _Cascade_. Se activa el modo plan, se selecciona el modelo _Opus 4.6_ y se agrega una instrucción clave: **"Ignora los otros archivos de plan que existen actualmente"** para evitar contaminación cruzada [08:20].

Windsurf genera el plan dentro de su estructura interna `.windsurf` y ofrece botones de _Implement_ para ejecutarlo directamente. Para exportarlo como archivo Markdown, se cambia al **modo code** y se solicita guardarlo en la raíz [10:05]. El resultado tiene **257 líneas** y destaca por:

- Estructura de proyecto muy detallada con cada archivo descrito.
- Indicaciones de _features_ por componente, como el _root layout_.
- Recomendaciones de _backend_ e infraestructura.
- Herramientas de desarrollo sugeridas.

Un punto crítico: en Windsurf, si no se selecciona el **modo code**, el editor no escribe, modifica ni borra ningún archivo del proyecto.

¿Cuál editor generó el mejor plan técnico?

Con los cuatro archivos listos —requerimiento original más tres planes— la comparación revela diferencias claras [11:25].

- **Claude Code** gana en profundidad con 472 líneas, estrategia de _branching_, _testing_ y recomendaciones de _performance_.
- **Windsurf** ocupa el segundo lugar con 257 líneas y un _scaffolding_ muy descriptivo.
- **Cursor** queda en tercer lugar con 94 líneas, posiblemente porque se dejó en **modo auto** y el modelo seleccionado automáticamente produjo menos detalle.

La diferencia entre Claude Code y Windsurf frente a Cursor puede explicarse porque a los dos primeros se les asignó manualmente el modelo _Opus 4.6_, mientras que Cursor eligió el suyo. Esto demuestra que **la selección del modelo influye directamente en la calidad del plan generado**.

Cada archivo es portable: el plan de Claude Code se puede usar en Cursor, el de Cursor en Windsurf y viceversa. Esa interoperabilidad es una ventaja enorme cuando se trabaja con distintas herramientas.

Por último, vale mencionar que existen herramientas **low code** como **Vercel v0** y **Lovable**, pensadas para trabajar desde el navegador, además de **Kilo Code**, una opción adicional que se explorará más adelante [13:00].

Si ya probaste alguno de estos editores en modo plan, comparte cuál te dio mejores resultados y qué modelo utilizaste.

---

Resumen

Si alguna vez olvidaste un comando en la terminal y perdiste minutos buscando en Google, existe una solución que integra **inteligencia artificial directamente en tu línea de comandos**. Warp es una terminal moderna que permite interactuar con un asistente de IA usando lenguaje natural, y lo mejor es que ofrece una capa gratuita bastante funcional para el día a día.

¿Cómo funciona la IA dentro de Warp?

Warp incorpora un asistente de inteligencia artificial al que puedes hablarle escribiendo un **hash (#)** seguido de tu pregunta en lenguaje natural [01:07]. Por ejemplo, si olvidaste cómo crear una carpeta en Linux, basta con escribir algo como "cómo se crea una carpeta" y el asistente responde con el comando exacto: **mkdir** seguido del nombre que desees.

Esta funcionalidad no se limita a operaciones básicas del sistema de archivos. También puedes preguntarle sobre comandos de **Git**, como guardar un _commit_ con un mensaje específico [01:47] o ejecutar un **cherry pick** [02:09], que es una operación para aplicar un _commit_ puntual de una rama a otra. Cada pregunta consume un crédito del plan que tengas activo.

¿Qué es el historial de comandos y cómo aprovecharlo?

Otra característica útil es el **historial de comandos** [00:38]. Usando las flechas arriba y abajo del teclado, puedes navegar por los comandos que ejecutaste previamente. Del lado derecho, Warp muestra hace cuánto tiempo los usaste. Esto elimina la necesidad de reescribir comandos repetitivos dentro de un mismo proyecto.

Para limpiar la pantalla y empezar desde cero, el comando **clear** borra todo el contenido visible y deja la ventana lista [00:24].

¿Cuánto cuesta Warp y qué incluye la versión gratuita?

En la página **warp.dev/pricing** puedes consultar los planes disponibles [02:38]. La capa gratuita incluye:

- Acceso limitado a modelos de **OpenAI**, **Anthropic** y **Google** [03:00].
- Acceso ilimitado a agentes en la nube.
- Indexación limitada de repositorios de código.
- Configuración de **cero retención de datos** (_zero data retention_) para proteger tu información.
- Almacenamiento limitado de conversaciones en la nube.

En cuanto a créditos, la versión gratuita entrega **300 créditos por mes durante los primeros dos meses** [03:32]. A partir del tercer mes, se reducen a **75 créditos mensuales**. Cada crédito equivale a un mensaje o consulta al asistente, lo que da aproximadamente diez consultas diarias con el plan inicial.

Si necesitas mayor capacidad, el plan _Build_ cuesta **20 dólares al mes** y ofrece **1,500 créditos mensuales** [04:00].

¿Con qué sistemas operativos es compatible?

Cuando Warp se lanzó, solo funcionaba en **Mac**. Actualmente es compatible con **Linux** y **Windows** también [04:50]. Desde la página principal detecta automáticamente tu sistema operativo y ofrece la descarga correspondiente. En Mac puedes instalarlo con el comando **brew install** o descargarlo directamente.

¿Qué es el modo agente de Warp?

Una de las funciones más potentes es el **modo agente** [05:05]. Al escribir **/agent** y presionar enter, toda la terminal se transforma en un agente conversacional similar a lo que ofrecen editores como **Windsurf** con _Cascade_ o **Cursor** con su propio agente.

Dentro del modo agente puedes:

- Seleccionar entre distintos **modelos de lenguaje**, como GPT-5, dependiendo de tu plan [05:22].
- Cambiar de modelo escribiendo **/model**, lo que muestra un _benchmark_ comparativo con métricas de inteligencia, velocidad y costo [05:35].
- Enviar comandos por voz.
- Agregar imágenes como contexto para tus preguntas.
- Aumentar el tamaño del texto directamente desde la conversación.

Para salir del modo agente, solo presiona **escape** y vuelves al modo terminal convencional [06:01].

Warp se posiciona como una herramienta que combina la potencia de una terminal clásica con la comodidad de un asistente inteligente. Si ya la usas o tienes otra terminal favorita, comparte tu experiencia para seguir ampliando la lista de herramientas útiles.

---
Resumen

Cuando necesitas entender qué hace un proyecto en GitHub, la documentación puede estar desactualizada o simplemente no existir. **Cognition** desarrolló una herramienta gratuita llamada **DeepWiki** que, potenciada por su agente **Devin**, permite chatear con cualquier repositorio, leer su código y documentación, y obtener respuestas en lenguaje natural. Esto reduce drásticamente el tiempo de evaluación de librerías y acelera la toma de decisiones técnicas.

¿Qué es DeepWiki y por qué resuelve el problema de la documentación?

Uno de los mayores riesgos al adoptar una librería o proyecto _open source_ es que su documentación esté incompleta o desactualizada [0:10]. La realidad es que a nadie le gusta documentar, y eso genera incertidumbre sobre el tiempo invertido en integrar una solución.

**DeepWiki** (deepwiki.com) es una plataforma creada por Cognition que indexa repositorios de GitHub y permite interactuar con ellos a través de un chat impulsado por Devin [0:30]. Al ingresar, se muestra un listado de repositorios ya indexados y un _call to action_ para agregar nuevos repos.

El flujo es simple:

- Busca el repositorio que te interesa en deepwiki.com.
- El agente de Devin lee toda la documentación y el código fuente.
- Haces preguntas en **lenguaje natural**, en cualquier idioma.
- Recibes respuestas con enlaces directos a archivos relevantes del proyecto.

¿Cómo funciona la búsqueda semántica dentro de un repositorio?

Cuando le haces una pregunta a Devin, el agente primero revisa la documentación disponible y luego lee el código fuente [1:07]. Si el proyecto está bien documentado, las respuestas son más precisas. Por ejemplo, al preguntar "¿qué hace este proyecto?" sobre **Supabase**, Devin responde que es una plataforma _open source_ que ofrece un _backend as a service_ construido sobre **Postgres** [1:30].

Un detalle técnico importante es que la **búsqueda semántica** se implementa con la extensión **PGVector** y métodos de _embeddings_ [1:53], lo que permite que las respuestas sean contextualmente relevantes y no simples coincidencias de texto.

¿Por qué Supabase fue recomendado para un proyecto de Next.js?

Al preguntarle a Devin cuál sería el beneficio de usar Supabase en un proyecto de **Next.js**, el agente identifica documentación específica como un _getting started_ con inicios rápidos para Next.js [2:15]. Los beneficios clave que menciona incluyen:

- **Integración profunda** con el ecosistema de Next.js.
- Autenticación sin fricción (_auth_ integrado).
- Datos en _server components_ y _server actions_ para mutaciones.
- Soporte para **Server Side Rendering** y _app router_ mediante cookies.
- **TypeScript** de extremo a extremo.
- SDKs específicos para facilitar la migración e implementación de la base de datos [2:50].

¿Cómo indexar tu propio repositorio en DeepWiki?

Existe un atajo muy práctico para acceder a DeepWiki desde cualquier repositorio de GitHub: simplemente reemplaza `github.com` por `deepwiki.com` en la URL del navegador [3:18]. Si el repositorio ya está indexado, llegarás directamente a la página con toda la documentación y el chat de Devin.

En una demostración con un proyecto personal creado para una _meetup_ de Supabase, Devin identificó correctamente que se trataba de un proyecto de Next.js creado con **Create Next App**, con _app router_, optimización de fuentes y una única página con el logo de Next.js [3:42].

¿Qué pasa si el repositorio no está indexado?

Cuando un repositorio no ha sido procesado aún, DeepWiki lo indica y ofrece la opción de indexarlo [4:15]. Solo necesitas proporcionar el correo electrónico del dueño del repositorio. El proceso de indexación tarda entre **dos y diez minutos** [5:00], después de los cuales el repositorio queda disponible con toda la funcionalidad del chat.

¿Cómo comparar librerías con DeepWiki para tomar mejores decisiones?

Una de las aplicaciones más poderosas es la **comparación entre herramientas**. Imagina que debes decidir entre dos librerías para tu _backend_ [4:40]. Puedes chatear con ambos repositorios en DeepWiki, analizar sus características y preparar un informe fundamentado sobre cuál implementar.

Esto transforma un proceso que podría tomar horas de lectura de documentación en una conversación directa con el código. ¿Ya probaste DeepWiki con tu proyecto? Indexa tu repositorio y comparte el enlace en los comentarios.

---

Resumen

Cuando necesitas entender qué hace un proyecto en GitHub, la documentación puede estar desactualizada o simplemente no existir. **Cognition** desarrolló una herramienta gratuita llamada **DeepWiki** que, potenciada por su agente **Devin**, permite chatear con cualquier repositorio, leer su código y documentación, y obtener respuestas en lenguaje natural. Esto reduce drásticamente el tiempo de evaluación de librerías y acelera la toma de decisiones técnicas.

¿Qué es DeepWiki y por qué resuelve el problema de la documentación?

Uno de los mayores riesgos al adoptar una librería o proyecto _open source_ es que su documentación esté incompleta o desactualizada [0:10]. La realidad es que a nadie le gusta documentar, y eso genera incertidumbre sobre el tiempo invertido en integrar una solución.

**DeepWiki** (deepwiki.com) es una plataforma creada por Cognition que indexa repositorios de GitHub y permite interactuar con ellos a través de un chat impulsado por Devin [0:30]. Al ingresar, se muestra un listado de repositorios ya indexados y un _call to action_ para agregar nuevos repos.

El flujo es simple:

- Busca el repositorio que te interesa en deepwiki.com.
- El agente de Devin lee toda la documentación y el código fuente.
- Haces preguntas en **lenguaje natural**, en cualquier idioma.
- Recibes respuestas con enlaces directos a archivos relevantes del proyecto.

¿Cómo funciona la búsqueda semántica dentro de un repositorio?

Cuando le haces una pregunta a Devin, el agente primero revisa la documentación disponible y luego lee el código fuente [1:07]. Si el proyecto está bien documentado, las respuestas son más precisas. Por ejemplo, al preguntar "¿qué hace este proyecto?" sobre **Supabase**, Devin responde que es una plataforma _open source_ que ofrece un _backend as a service_ construido sobre **Postgres** [1:30].

Un detalle técnico importante es que la **búsqueda semántica** se implementa con la extensión **PGVector** y métodos de _embeddings_ [1:53], lo que permite que las respuestas sean contextualmente relevantes y no simples coincidencias de texto.

¿Por qué Supabase fue recomendado para un proyecto de Next.js?

Al preguntarle a Devin cuál sería el beneficio de usar Supabase en un proyecto de **Next.js**, el agente identifica documentación específica como un _getting started_ con inicios rápidos para Next.js [2:15]. Los beneficios clave que menciona incluyen:

- **Integración profunda** con el ecosistema de Next.js.
- Autenticación sin fricción (_auth_ integrado).
- Datos en _server components_ y _server actions_ para mutaciones.
- Soporte para **Server Side Rendering** y _app router_ mediante cookies.
- **TypeScript** de extremo a extremo.
- SDKs específicos para facilitar la migración e implementación de la base de datos [2:50].

¿Cómo indexar tu propio repositorio en DeepWiki?

Existe un atajo muy práctico para acceder a DeepWiki desde cualquier repositorio de GitHub: simplemente reemplaza `github.com` por `deepwiki.com` en la URL del navegador [3:18]. Si el repositorio ya está indexado, llegarás directamente a la página con toda la documentación y el chat de Devin.

En una demostración con un proyecto personal creado para una _meetup_ de Supabase, Devin identificó correctamente que se trataba de un proyecto de Next.js creado con **Create Next App**, con _app router_, optimización de fuentes y una única página con el logo de Next.js [3:42].

¿Qué pasa si el repositorio no está indexado?

Cuando un repositorio no ha sido procesado aún, DeepWiki lo indica y ofrece la opción de indexarlo [4:15]. Solo necesitas proporcionar el correo electrónico del dueño del repositorio. El proceso de indexación tarda entre **dos y diez minutos** [5:00], después de los cuales el repositorio queda disponible con toda la funcionalidad del chat.

¿Cómo comparar librerías con DeepWiki para tomar mejores decisiones?

Una de las aplicaciones más poderosas es la **comparación entre herramientas**. Imagina que debes decidir entre dos librerías para tu _backend_ [4:40]. Puedes chatear con ambos repositorios en DeepWiki, analizar sus características y preparar un informe fundamentado sobre cuál implementar.

Esto transforma un proceso que podría tomar horas de lectura de documentación en una conversación directa con el código. ¿Ya probaste DeepWiki con tu proyecto? Indexa tu repositorio y comparte el enlace en los comentarios.

---

Resumen

Trabajar con bases de datos directamente desde el editor de código ya es posible gracias al **Model Context Protocol (MCP)**, un estándar abierto lanzado por Anthropic en noviembre de 2024. Esta integración permite conectar herramientas de inteligencia artificial con servicios de terceros sin cambiar de interfaz, y en este caso se aplica para gestionar tablas en **Supabase** desde **Windsurf** sin abrir el navegador.

¿Qué es MCP y por qué cambia la forma de trabajar con servicios externos?

El **Model Context Protocol** es un protocolo diseñado para que las herramientas de IA se comuniquen con servicios de terceros de forma estandarizada. En lugar de alternar entre el _dashboard_ de Supabase y el editor, MCP permite ejecutar comandos de lectura y escritura directamente desde donde se escribe el código [0:28].

En la práctica, esto significa que operaciones como listar proyectos, consultar tablas o incluso crear nuevas estructuras en la base de datos se realizan sin abandonar Windsurf.

¿Cómo se instala el MCP de Supabase en Windsurf?

El proceso de instalación es directo y se completa en pocos pasos [1:02]:

- Abrir el apartado de **Actions** en Windsurf y acceder al _marketplace_ de MCP.
- Buscar "Supabase" y hacer clic en instalar.
- Generar un _**access token**_ desde la página de Supabase, en la sección de generación de tokens.
- Asignar un nombre al token (por ejemplo, "MCP Windsurf") y definir su tiempo de expiración.
- Copiar el token, pegarlo en Windsurf y guardar.

Una vez configurado, la interfaz cambia: aparecen opciones para eliminar, configurar y activar o desactivar la conexión. También se despliega un listado completo de herramientas disponibles como listar organizaciones, obtener proyectos, consultar costos y crear proyectos [2:25].

¿Cómo verificar que la conexión funciona correctamente?

Hay dos formas de confirmar que el MCP está activo. La primera es visual: en el panel de Actions aparece un **circulito verde** junto al nombre del MCP [3:02]. La segunda es funcional: se puede abrir un nuevo _cascade_ y preguntar directamente "lista los proyectos que tengo en mi Supabase" usando el **modo Ask** para evitar modificaciones en archivos.

El editor se conecta al MCP, ejecuta la función `listar proyectos` y devuelve los resultados. En este ejemplo, detectó nueve proyectos en la cuenta, dos activos, entre ellos **Platzi Fútbol Club** [3:30].

¿Qué información revela el MCP al consultar tablas existentes?

Al pedir que liste las tablas del proyecto Platzi FC, el MCP busca en el **esquema public** y devuelve cada tabla con una descripción generada automáticamente por el editor [4:15]. Esa descripción no existe previamente en Supabase; el modelo la infiere a partir de la lectura del esquema.

Además, el sistema arroja observaciones importantes de seguridad:

- Todas las tablas están vacías.
- Ninguna tabla tiene **Row-Level Security (RLS)** habilitado, lo que representa un riesgo si se exponen vía API pública.
- Supabase habilita cada tabla como un _**endpoint**_ consumible, y sin RLS cualquiera podría acceder a los datos.
- Una tabla de respaldo no tiene llave primaria definida [4:55].

¿Cómo crear tablas nuevas en Supabase desde el editor?

Para generar las tablas del contenido deportivo y estadístico del proyecto, se cambia del **modo Ask** al **modo Code** en el _cascade_ de Windsurf [5:40]. El _prompt_ indica crear las tablas siguiendo el estándar en inglés de las ya existentes, pasando únicamente los nombres.

El modelo interpreta la estructura necesaria sin recibir definiciones explícitas de columnas [6:10]:

- Analiza el patrón de las tablas existentes.
- Define tipos de datos coherentes para cada campo.
- Genera todas las tablas en una **sola migración SQL**.
- Crea campos como fechas de inicio y fin para temporadas, IDs de competición, jornadas de partido e IDs de equipos locales y visitantes.

Al validar en el _dashboard_ de Supabase, las tablas aparecen correctamente creadas con una estructura lógica completa: equipos, _standings_, partidos (_matches_) y más [7:05]. Todo el esquema fue generado por el modelo y enviado a Supabase mediante sentencias **SQL** sin escribir código manualmente ni interactuar con la interfaz del proveedor.

El backend del proyecto queda casi completo, basado en **PostgreSQL** a través de Supabase, con tablas creadas exclusivamente desde el editor. ¿Qué MCP conoces o utilizas en tus proyectos? Compártelo en los comentarios para seguir ampliando la lista de herramientas de IA.

---

Resumen

Revisar código es una de las tareas que más tiempo consume en cualquier equipo de desarrollo, y el problema crece proporcionalmente con cada _pull request_ nuevo que llega al repositorio. Existe una herramienta gratuita creada por Cognition que promete acelerar ese proceso sin sacrificar calidad: se llama **Devin Review** y funciona directamente desde el navegador, sin necesidad de autenticarse ni otorgar permisos especiales cuando el repositorio es público.

¿Cómo funciona Devin Review para analizar un pull request?

El flujo es sorprendentemente simple. Basta con tomar la URL de un _pull request_ en GitHub y **reemplazar "github" por "devin review"** en la barra de direcciones [01:45]. Eso inicializa un chat con Devin, el agente de inteligencia artificial de Cognition, que comienza a leer los metadatos del PR: quién lo creó, el título, la rama de destino, la cantidad de archivos modificados y las estadísticas generales.

Durante el análisis, Devin busca un archivo llamado `review.markdown` con instrucciones personalizadas para mejorar la revisión. Si no lo encuentra, continúa con su flujo estándar: **lee cada archivo modificado, entiende el contexto completo de la tarea y genera un reporte detallado** [02:30].

¿Qué información entrega el reporte de análisis?

El reporte identifica las páginas afectadas, describe los patrones aplicados y señala las decisiones técnicas relevantes. En el ejemplo mostrado, el PR migraba tres páginas —_home_, listado de noticias y detalle de noticia— de **data moqueada a consultas reales contra Supabase** [03:55].

Devin detectó que:

- Se creó un archivo `queries` centralizado para las funciones de consulta a Supabase.
- Cada página se convierte en un _server component_ que invoca esas funciones y pasa los resultados como _props_ a componentes hijo.
- Se agregaron funciones auxiliares como `formatDate` y `formatShortDate` para convertir el _timestamp_ ISO de la base de datos al formato visual del _front-end_ [04:25].
- Se instaló el **SDK oficial de Supabase** para JavaScript como nueva dependencia.

¿Qué tipo de advertencias y bugs puede detectar?

Una de las secciones más valiosas del reporte es la de _flags_ o advertencias. En el ejemplo no se encontraron bugs, algo que según se menciona **suele pasar muy poco** [05:20]. Sin embargo, Devin sí identificó oportunidades de mejora:

- La función `getNewsBySlot` estaba **duplicada** en el proyecto.
- El _locale_ para formateo de fechas variaba entre servidor y cliente, lo que podría generar inconsistencias.
- No existía un patrón de **caché** para las llamadas a Supabase dentro de los _server components_.
- La función `getRelatedNews` hacía una consulta innecesaria a la base de datos cuando los _tags_ venían vacíos [05:50].

¿Se puede interactuar con Devin en lenguaje natural?

Sí, y en español. El chat integrado permite hacer preguntas directas como "¿Qué cosas está haciendo este PR?" o "Dame en un párrafo lo que nos entrega este PR" [06:45]. Devin responde con un resumen claro y contextualizado, lo cual resulta especialmente útil cuando los PRs incluyen muchos archivos y el revisor necesita entender rápidamente el alcance del cambio **sin leer archivo por archivo**.

También es posible preguntarle qué enfoque mejorar o cómo solucionar bugs detectados. Si la herramienta está conectada al repositorio con permisos de escritura, puede incluso **aplicar correcciones directamente** mediante _commits_ [07:30].

¿Cuál es la diferencia entre usar Devin Review con y sin autenticación?

Sin autenticarse ni dar acceso al repositorio, se obtiene el análisis completo, el reporte de bugs y advertencias, y la interacción por chat. Todo esto funciona siempre que el repositorio sea **público**. Al conectar GitHub, se habilitan funciones adicionales como la edición directa del código y la posibilidad de que Devin deje comentarios automáticos en el PR [08:40].

Cuando Devin completa una revisión y encuentra _issues_, los deja como comentarios directamente en el _pull request_ de GitHub. Si no encuentra problemas, puede omitir el comentario, como ocurrió en el ejemplo mostrado.

¿Por qué usar herramientas de IA para revisión de código?

El **cuello de botella en la revisión de PRs** es un problema real en equipos grandes con múltiples desarrolladores lanzando cambios simultáneamente [01:20]. Herramientas como Devin Review no buscan reemplazar al revisor humano, sino **liberar su tiempo para que lo use de manera efectiva**, enfocándose en decisiones de arquitectura y lógica de negocio en lugar de rastrear errores mecánicos.

Si ya has probado Devin Review conectándolo a tu repositorio con GitHub, comparte tu experiencia y cuéntanos qué diferencias encontraste respecto al modo sin autenticación.

---

Resumen

Optimizar el proceso de revisión de código es una de las prioridades en cualquier equipo de desarrollo, y hoy existen herramientas que integran **inteligencia artificial** para hacerlo de forma automática dentro de GitHub. **Code Rabbit** es una de ellas: analiza los _pull requests_, genera comentarios automáticos y ofrece un resumen técnico de los cambios realizados, todo sin salir del repositorio.

¿Cómo se configura Code Rabbit en un repositorio de GitHub?

Code Rabbit cuenta con una **capa gratuita** y ofrece catorce días de prueba en su versión pro al registrarte con tu cuenta de GitHub [0:18]. Una vez dentro del panel, puedes sincronizar tu cuenta y elegir a cuáles repositorios darle acceso.

- Puedes otorgar acceso a **todos los repositorios** o solo a los seleccionados.
- En el ejemplo, se selecciona únicamente el repositorio llamado _AI Tools_ [0:48].
- Al hacer clic en instalar y autorizar, el repositorio queda conectado al panel de Code Rabbit.

Con esta configuración lista, cada vez que se cree un _pull request_ en ese repositorio, el agente de Code Rabbit comenzará a trabajar automáticamente.

¿Qué sucede al crear un pull request?

Al generar un PR con cambios —en este caso, un ajuste en la interfaz—, Code Rabbit inicia su análisis de inmediato [1:06]. En la vista del _pull request_ aparece el _action_ de Code Rabbit indicando que el _review_ está en progreso. Una vez completado, agrega un **comentario detallado** directamente en el PR.

Este comentario incluye:

- Los **commits** involucrados en el _pull request_.
- Los **archivos modificados** (en este ejemplo, dos archivos).
- Un _walkthrough_ o recorrido explicando qué cambió en cada archivo [2:22].
- Un **summary** que describe técnicamente las modificaciones realizadas.

Todo esto es personalizable desde el panel de usuario: puedes configurar qué tan extenso o específico quieres el mensaje, y definir exactamente qué aspectos deseas validar [1:32].

¿Qué son los checks de pre-merge en Code Rabbit?

Además del resumen, Code Rabbit ejecuta unos **checks de pre-merge** antes de que el código se fusione [2:52]. En el ejemplo, dos checks pasaron correctamente y uno falló con un _warning_.

- El _warning_ se generó porque el repositorio no tiene _**test coverage**_ configurado.
- Code Rabbit detectó un **0 % de cobertura**, cuando el _threshold_ requerido por defecto es **80 %** [3:08].
- Esta configuración viene activada por defecto, pero puede desactivarse mientras el proyecto está en fase inicial.

La recomendación es reactivar este check cuando el equipo comience a implementar _**unit tests**_, para asegurar que cada PR cumpla con el mínimo de cobertura establecido [3:22].

Entre los checks que sí aprobaron se encuentran: la validación de que el PR tiene una **descripción**, un _high level summary_ habilitado y un _title check_ [3:38]. El título del PR era "Fix Match Card Alignment", lo que describe con claridad el propósito del cambio.

¿Qué problema resolvía este pull request de ejemplo?

El código original del _frontend_ mostraba un listado de partidos donde los equipos locales estaban alineados a la izquierda y los visitantes a la derecha. Sin embargo, el marcador central se desplazaba dependiendo del **ancho en caracteres** del nombre de cada equipo [3:52]. Por ejemplo, "Deportivo Sur" tiene más caracteres que "Platzi FC", lo que empujaba el marcador hacia la izquierda.

La solución fue cambiar la clase CSS de `justify-between` a **flex centrado**, logrando que todo el contenido quedara visualmente equilibrado [4:12]. Code Rabbit identificó y resumió este cambio de manera precisa en su análisis automático.

Esta herramienta representa una forma práctica de **reducir el tiempo invertido en revisiones de código**, complementando el trabajo del equipo con análisis automatizados. Si conoces alguna otra herramienta similar, compártela en los comentarios para seguir ampliando el repertorio de opciones con inteligencia artificial.

---

Resumen

Llevar un proyecto web a producción es el paso definitivo para que tu trabajo sea visible en internet. Cuando ya tienes el **backend resuelto con Supabase** y el **frontend construido con Next.js**, solo falta publicar esa interfaz en un servicio confiable. Aquí es donde **Vercel** se convierte en la opción más natural, especialmente si trabajas con Next.js, y aún más si puedes automatizar el proceso desde tu propio editor gracias a un **MCP oficial**.

¿Cómo preparar tu cuenta de Vercel para el despliegue?

Antes de cualquier configuración técnica, necesitas una cuenta activa en **vercel.com**. Una vez registrado, accedes a tu panel de proyectos donde puedes ver todos los sitios que ya tienes desplegados. Desde ahí puedes agregar un nuevo proyecto de dos formas principales:

- **Importar desde GitHub:** conectas tu cuenta de GitHub y seleccionas el repositorio. Cada _git push_ posterior generará un despliegue automático [00:42].
- **Usar el MCP de Vercel desde Windsurf:** esta es la ruta que permite hacer todo sin salir del editor, interactuando directamente con el agente de inteligencia artificial [01:12].

El **MCP** (_Model Context Protocol_) de Vercel es un conector oficial disponible en el _marketplace_ de Windsurf. Al instalarlo, el editor te redirige a una pantalla de validación de sesión donde autorizas los permisos necesarios para tu cuenta [01:22].

¿Qué herramientas ofrece el MCP de Vercel?

Una vez instalado, puedes verificar las acciones disponibles desplegando el menú de herramientas. El MCP incluye funcionalidades como:

- **Buscar documentación** de Vercel.
- **Desplegar a Vercel** directamente desde el editor.
- **Listar proyectos** y _deployments_ existentes.
- **Obtener información** de proyectos específicos [01:42].

Estas herramientas permiten que el agente de **Cascade** (el asistente de Windsurf) ejecute cada paso del despliegue como si lo hicieras manualmente desde la terminal o el panel web.

¿Qué sucede durante el proceso de deploy con el agente?

Al pedirle a Cascade que despliegue el proyecto, el agente primero valida la **estructura de archivos**. Luego utiliza la herramienta _list teams_ para identificar tu equipo en Vercel y procede a ejecutar el _deploy_ [02:12].

Si no tienes la **CLI de Vercel** instalada, el agente lo detecta y recomienda ejecutar `npm install -g vercel` para instalarla globalmente. Después lanza el comando `vercel deploy` directamente desde la terminal integrada en el chat [02:32].

¿Cómo resolver errores de estructura en proyectos monorepo?

No todos los proyectos tienen una estructura estándar de Next.js. En este caso, el proyecto utiliza **PNPM** con una estructura de _monorepo_: la carpeta raíz contiene `AI Tools`, dentro está `Platzi FC`, y en el directorio `apps/web` se encuentra el proyecto de Next.js real [03:02].

Cuando el primer _build_ falla, puedes **escribir directamente en la terminal del agente** para guiarlo. Cascade analiza los errores y ajusta la configuración para que el despliegue termine de forma exitosa [03:22].

¿Por qué es crítico configurar las variables de entorno?

Las **variables de entorno** guardan las _keys_ de conexión con servicios externos como Supabase. Sin ellas, el frontend no puede leer datos del backend. El agente recomienda comandos específicos del set de herramientas de Vercel para pasar esas variables al proyecto [03:42].

Vercel ofrece **múltiples entornos**: desarrollo, _staging_ y producción. Es necesario agregar las variables en cada uno para que la conexión funcione correctamente [04:22]. Tras configurarlas, hay que **redesplegar** el proyecto porque las variables se leen en el momento de _build_ [04:42].

¿Cómo verificar que tu proyecto está en producción?

Desde el panel de Vercel puedes confirmar que el despliegue fue exitoso. El proyecto muestra la rama `main` desplegada y genera una **URL pública** que puedes compartir con cualquier persona [05:02].

Para validar la conexión con Supabase, basta con modificar un dato en la base de datos y refrescar la página. Si el cambio se refleja, significa que el **frontend en Vercel** está leyendo correctamente la **data desde Supabase** en tiempo real [05:22].

De esta forma, utilizando herramientas de inteligencia artificial en cada fase —desde la planificación hasta el despliegue— es posible construir un **MVP completo** y funcional. Comparte el enlace de tu proyecto en los comentarios para que la comunidad pueda verlo.

---
