import React, { useState } from "react";
import { Sparkles, BookOpen, Heart, Lightbulb, RefreshCw } from "lucide-react";

const ZinkingWriter = () => {
  const [input, setInput] = useState("");
  const [output, setOutput] = useState("");
  const [contentType, setContentType] = useState("educativo");
  const [isProcessing, setIsProcessing] = useState(false);

  const zinkingPatterns = {
    openings: [
      "Recuerdo cuando",
      "Hace tiempo, me encontré",
      "Hubo un momento en mi vida en que",
      "Nunca olvidaré aquella vez que",
      "Permíteme contarte algo que aprendí",
    ],
    transitions: [
      "Esa experiencia me enseñó que",
      "Desde entonces entendí que",
      "Lo que descubrí fue simple pero profundo:",
      "Y ahí estaba la lección:",
      "Eso transformó mi forma de ver",
    ],
    validations: [
      "Si alguna vez has sentido",
      "Quizás tú también has experimentado",
      "Sé que esto puede parecer",
      "Es completamente normal",
      "No estás solo en esto",
    ],
    invitations: [
      "Te invito a explorar",
      "¿Qué pasaría si",
      "Prueba esto y observa",
      "Permítete",
      "Considera la posibilidad de",
    ],
    closings: [
      "La magia sucede cuando",
      "Cada paso cuenta",
      "El viaje apenas comienza",
      "Y así, poco a poco",
      "Eso es lo que hace la diferencia",
    ],
  };

  const analogies = [
    {
      concept: "proceso",
      analogy:
        "afinar un instrumento - no lo haces una vez y olvidas; es un ajuste constante que requiere oído atento",
    },
    {
      concept: "simplificar",
      analogy:
        "ir de mochilero en lugar de en casa rodante - te mueves más rápido, llegas a lugares inaccesibles, y la experiencia se vuelve íntima",
    },
    {
      concept: "aprender",
      analogy:
        "cocinar sin receta - al principio necesitas medir todo, pero con el tiempo desarrollas intuición",
    },
    {
      concept: "editar",
      analogy:
        "tallar una escultura - no agregas material, quitas lo que sobra hasta revelar la forma que siempre estuvo ahí",
    },
    {
      concept: "práctica",
      analogy:
        "cultivar un jardín - no ves el crecimiento diario, pero de repente florece algo hermoso",
    },
  ];

  const transformToZinking = (text, type) => {
    if (!text.trim()) return "";

    const lines = text.split("\n").filter((line) => line.trim());
    let transformed = "";

    // 1. APERTURA CON HISTORIA PERSONAL
    const opening =
      zinkingPatterns.openings[
        Math.floor(Math.random() * zinkingPatterns.openings.length)
      ];
    transformed += `${opening} algo que cambió mi perspectiva. `;
    transformed += `Estaba enfrentando exactamente lo que tú podrías estar explorando ahora. `;
    transformed += `Había dudas, incertidumbre... `;

    // Añadir un momento sensorial específico
    const sensorialDetails = [
      "El aroma a café llenaba la habitación.",
      "La luz suave entraba por la ventana.",
      "Podía escuchar el silencio a mi alrededor.",
      "Las manos me temblaban ligeramente.",
      "El aire se sentía denso de posibilidad.",
    ];
    transformed +=
      sensorialDetails[Math.floor(Math.random() * sensorialDetails.length)];
    transformed += "\n\n";

    // 2. TRANSICIÓN REFLEXIVA
    const transition =
      zinkingPatterns.transitions[
        Math.floor(Math.random() * zinkingPatterns.transitions.length)
      ];
    transformed += `${transition} `;

    // 3. CONTENIDO PRINCIPAL CON ANALOGÍA
    const randomAnalogy =
      analogies[Math.floor(Math.random() * analogies.length)];

    // Reformular el contenido original con voz Zinking
    const mainContent = lines
      .map((line) => {
        // Eliminar bullet points y números
        let cleaned = line.replace(/^[\d\-\*\•]+\.?\s*/, "");

        // Hacer más conversacional
        cleaned = cleaned.replace(
          /debes|tienes que|es necesario/gi,
          "podrías considerar",
        );
        cleaned = cleaned.replace(/siempre|nunca/gi, "a menudo");
        cleaned = cleaned.replace(
          /^Los expertos|^Se recomienda/gi,
          "He descubierto que",
        );

        return cleaned;
      })
      .join(". ");

    transformed += `${mainContent}\n\n`;

    // 4. AÑADIR ANALOGÍA
    transformed += `Piénsalo como ${randomAnalogy.analogy}. `;
    transformed += `Así funciona esto también.\n\n`;

    // 5. VALIDACIÓN EMPÁTICA
    const validation =
      zinkingPatterns.validations[
        Math.floor(Math.random() * zinkingPatterns.validations.length)
      ];
    transformed += `${validation} esta sensación de incertidumbre, estás en el camino correcto. `;
    transformed += `La incomodidad es donde sucede el crecimiento.\n\n`;

    // 6. PASOS ACCIONABLES (si es educativo)
    if (type === "educativo" || type === "tutorial") {
      transformed += `**Ahora es tu turno:**\n\n`;
      transformed += `Empieza pequeño. Elige una sola cosa de lo que hemos explorado. `;
      transformed += `No todas. Una. `;
      transformed += `Practícala durante tres días. `;
      transformed += `Observa qué descubres.\n\n`;
    }

    // 7. INVITACIÓN Y CIERRE
    const invitation =
      zinkingPatterns.invitations[
        Math.floor(Math.random() * zinkingPatterns.invitations.length)
      ];
    const closing =
      zinkingPatterns.closings[
        Math.floor(Math.random() * zinkingPatterns.closings.length)
      ];

    transformed += `${invitation} este enfoque con curiosidad, sin presión de perfección. `;
    transformed += `${closing} nos permitimos ser aprendices perpetuos. `;
    transformed += `Cada paso, por pequeño que parezca, te transforma.\n\n`;

    // 8. PREGUNTA REFLEXIVA FINAL
    const reflectiveQuestions = [
      "¿Qué pequeño paso podrías dar hoy?",
      "¿Qué te gustaría descubrir en este camino?",
      "¿Cómo se sentiría permitirte explorar sin juicio?",
      "¿Qué cambiaría si simplificaras un poco más?",
      "¿Dónde está tu atención en este momento?",
    ];
    transformed +=
      reflectiveQuestions[
        Math.floor(Math.random() * reflectiveQuestions.length)
      ];

    return transformed;
  };

  const handleTransform = () => {
    if (!input.trim()) return;

    setIsProcessing(true);

    // Simular procesamiento con un pequeño delay para mejor UX
    setTimeout(() => {
      const result = transformToZinking(input, contentType);
      setOutput(result);
      setIsProcessing(false);
    }, 800);
  };

  const examples = {
    educativo:
      "La gestión del tiempo es importante para la productividad.\nDebes planificar tus tareas.\nUsa listas de pendientes.\nElimina distracciones.",
    inspiracional:
      "El éxito requiere esfuerzo.\nNo te rindas.\nPersigue tus metas.",
    tecnico:
      "Para optimizar el código:\n- Usa variables descriptivas\n- Evita repetición\n- Comenta tu código",
  };

  const loadExample = () => {
    setInput(examples[contentType]);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-amber-50 via-orange-50 to-rose-50 p-8">
      <div className="max-w-6xl mx-auto">
        {/* Header */}
        <div className="text-center mb-12">
          <div className="flex items-center justify-center gap-3 mb-4">
            <Sparkles className="w-10 h-10 text-orange-600" />
            <h1 className="text-5xl font-bold text-gray-800">Zinking Writer</h1>
          </div>
          <p className="text-xl text-gray-600 max-w-2xl mx-auto">
            Transforma cualquier contenido en una experiencia de conexión humana
          </p>
          <p className="text-sm text-gray-500 mt-2 italic">
            "La magia sucede cuando la estructura se vuelve invisible y solo
            queda la verdad"
          </p>
        </div>

        {/* Tipo de Contenido */}
        <div className="bg-white rounded-2xl shadow-lg p-6 mb-6">
          <label className="block text-sm font-semibold text-gray-700 mb-3">
            Tipo de Contenido
          </label>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-3">
            {[
              {
                value: "educativo",
                icon: BookOpen,
                label: "Educativo/Tutorial",
              },
              { value: "inspiracional", icon: Heart, label: "Inspiracional" },
              {
                value: "tecnico",
                icon: Lightbulb,
                label: "Técnico/Explicativo",
              },
            ].map(({ value, icon: Icon, label }) => (
              <button
                key={value}
                onClick={() => setContentType(value)}
                className={`flex items-center gap-2 p-4 rounded-xl transition-all ${
                  contentType === value
                    ? "bg-orange-500 text-white shadow-md"
                    : "bg-gray-100 text-gray-700 hover:bg-gray-200"
                }`}
              >
                <Icon className="w-5 h-5" />
                <span className="font-medium">{label}</span>
              </button>
            ))}
          </div>
        </div>

        {/* Input y Output */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          {/* Input */}
          <div className="bg-white rounded-2xl shadow-lg p-6">
            <div className="flex items-center justify-between mb-4">
              <h2 className="text-lg font-semibold text-gray-800">
                Contenido Original
              </h2>
              <button
                onClick={loadExample}
                className="text-sm text-orange-600 hover:text-orange-700 underline"
              >
                Cargar ejemplo
              </button>
            </div>
            <textarea
              value={input}
              onChange={(e) => setInput(e.target.value)}
              placeholder="Escribe o pega tu contenido aquí...&#10;&#10;Puede ser técnico, frío, o simplemente información sin alma.&#10;&#10;Zinking lo transformará en una experiencia de conexión."
              className="w-full h-80 p-4 border-2 border-gray-200 rounded-xl focus:border-orange-400 focus:outline-none resize-none font-mono text-sm"
            />
            <button
              onClick={handleTransform}
              disabled={!input.trim() || isProcessing}
              className={`w-full mt-4 py-3 rounded-xl font-semibold transition-all flex items-center justify-center gap-2 ${
                !input.trim() || isProcessing
                  ? "bg-gray-300 text-gray-500 cursor-not-allowed"
                  : "bg-orange-500 text-white hover:bg-orange-600 shadow-lg hover:shadow-xl"
              }`}
            >
              {isProcessing ? (
                <>
                  <RefreshCw className="w-5 h-5 animate-spin" />
                  Transformando...
                </>
              ) : (
                <>
                  <Sparkles className="w-5 h-5" />
                  Transformar con Zinking
                </>
              )}
            </button>
          </div>

          {/* Output */}
          <div className="bg-white rounded-2xl shadow-lg p-6">
            <h2 className="text-lg font-semibold text-gray-800 mb-4">
              Versión Zinking
            </h2>
            <div className="w-full h-80 p-4 border-2 border-orange-200 rounded-xl overflow-y-auto bg-gradient-to-br from-amber-50 to-orange-50">
              {output ? (
                <div className="prose prose-sm max-w-none">
                  {output.split("\n").map((paragraph, idx) => {
                    if (!paragraph.trim()) return null;
                    if (paragraph.startsWith("**")) {
                      return (
                        <p key={idx} className="font-bold text-orange-800 mt-4">
                          {paragraph.replace(/\*\*/g, "")}
                        </p>
                      );
                    }
                    return (
                      <p
                        key={idx}
                        className="text-gray-700 leading-relaxed mb-3"
                      >
                        {paragraph}
                      </p>
                    );
                  })}
                </div>
              ) : (
                <div className="h-full flex items-center justify-center text-gray-400 text-center">
                  <div>
                    <Heart className="w-12 h-12 mx-auto mb-3 opacity-50" />
                    <p>Tu contenido transformado aparecerá aquí...</p>
                    <p className="text-sm mt-2">
                      Con calidez, autenticidad y alma.
                    </p>
                  </div>
                </div>
              )}
            </div>
            {output && (
              <button
                onClick={() => {
                  navigator.clipboard.writeText(output);
                  alert("¡Copiado al portapapeles!");
                }}
                className="w-full mt-4 py-2 bg-gray-100 text-gray-700 rounded-xl hover:bg-gray-200 transition-all font-medium"
              >
                Copiar texto
              </button>
            )}
          </div>
        </div>

        {/* Principios Zinking */}
        <div className="mt-8 bg-white rounded-2xl shadow-lg p-6">
          <h3 className="text-lg font-semibold text-gray-800 mb-4">
            Principios de Transformación
          </h3>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            {[
              {
                title: "Vulnerabilidad",
                desc: "Compartir procesos, no solo éxitos",
              },
              {
                title: "Analogías",
                desc: "Comparar con experiencias universales",
              },
              {
                title: "Validación",
                desc: "Reconocer lo que el receptor siente",
              },
              { title: "Simplificación", desc: "Reducir al núcleo esencial" },
              { title: "Presencia", desc: "Invitar al momento presente" },
              {
                title: "Gratitud",
                desc: "Enmarcar como privilegio, no derecho",
              },
            ].map((principle, idx) => (
              <div key={idx} className="p-4 bg-orange-50 rounded-xl">
                <h4 className="font-semibold text-orange-800 mb-1">
                  {principle.title}
                </h4>
                <p className="text-sm text-gray-600">{principle.desc}</p>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};

export default ZinkingWriter;
