#!/usr/bin/env python3
"""
SKILL 6: PROFESSIONAL CONTENT CREATION
Archivo: content_creation_skills.py
Descripción: Generación de contenido profesional para TikTok, LinkedIn, Twitter/X, YouTube.

Use Cases:
- Scripts de TikTok sobre IA y tecnología
- Posts optimizados para LinkedIn engagement
- Threads de Twitter/X técnicos
- Guiones de YouTube educativos
- Branded content siguiendo guidelines corporativas

Execution Mode: Isolated (API calls to Anthropic for content generation)
"""

import sys
import json
import re
from pathlib import Path
from typing import Dict, Any, List, Optional
from dataclasses import dataclass, asdict
from datetime import datetime
from enum import Enum

class ContentPlatform(Enum):
    """Plataformas soportadas"""
    TIKTOK = "tiktok"
    LINKEDIN = "linkedin"
    TWITTER = "twitter"
    YOUTUBE = "youtube"
    INSTAGRAM = "instagram"

class ContentTone(Enum):
    """Tonos de comunicación"""
    PROFESSIONAL = "professional"
    CASUAL = "casual"
    EDUCATIONAL = "educational"
    INSPIRATIONAL = "inspirational"
    HUMOROUS = "humorous"

@dataclass
class ContentRequest:
    """Solicitud de creación de contenido"""
    platform: str
    topic: str
    tone: str
    language: str = "es"
    target_audience: str = "general tech audience"
    brand_guidelines: Optional[Dict] = None
    length_preference: Optional[str] = None  # "short", "medium", "long"

@dataclass
class ContentOutput:
    """Contenido generado"""
    platform: str
    content_type: str
    main_content: str
    hook: Optional[str] = None
    cta: Optional[str] = None
    hashtags: List[str] = None
    estimated_engagement_score: float = 0.0
    seo_keywords: List[str] = None
    metadata: Dict[str, Any] = None

class ContentCreator:
    """
    Generador profesional de contenido para redes sociales.
    Especializado en contenido de IA, tecnología y empresa.
    """

    def __init__(self):
        self.platform_configs = self._load_platform_configs()
        self.brand_voice = {}

    def _load_platform_configs(self) -> Dict[str, Dict]:
        """
        Configuraciones específicas por plataforma.
        """
        return {
            "tiktok": {
                "max_script_length": 300,  # palabras
                "optimal_duration": "60-90 seconds",
                "hook_critical": True,
                "vertical_video": True,
                "trending_formats": ["storytelling", "how-to", "myth-busting", "day-in-life"]
            },
            "linkedin": {
                "max_post_length": 3000,  # caracteres
                "optimal_length": "1200-1500",
                "professional_tone": True,
                "hashtags_limit": 5,
                "formats": ["insight", "case-study", "thought-leadership", "announcement"]
            },
            "twitter": {
                "max_tweet_length": 280,
                "thread_optimal": "5-8 tweets",
                "hashtags_limit": 3,
                "formats": ["hot-take", "thread", "poll", "announcement"]
            },
            "youtube": {
                "script_types": ["tutorial", "explainer", "news-analysis", "review"],
                "optimal_length": "8-12 minutes",
                "include_chapters": True,
                "include_b_roll_notes": True
            }
        }

    def create_tiktok_script(
        self,
        topic: str,
        tone: str = "educational",
        language: str = "es",
        duration_seconds: int = 60
    ) -> ContentOutput:
        """
        Genera script profesional para TikTok sobre IA y tecnología.

        Estructura:
        1. Hook (3s): Captura atención inmediata
        2. Problema/Contexto (10s)
        3. Desarrollo/Solución (40s)
        4. CTA/Cierre (7s)
        """
        # Generar hook impactante
        hook = self._generate_tiktok_hook(topic, language)

        # Estructura del script
        script_sections = {
            "hook": hook,
            "context": self._generate_context(topic, platform="tiktok", language=language),
            "main_content": self._generate_main_content(
                topic,
                platform="tiktok",
                tone=tone,
                language=language
            ),
            "cta": self._generate_cta(platform="tiktok", language=language)
        }

        # Ensamblar script completo
        full_script = f"""🎬 SCRIPT TIKTOK - {topic.upper()}
⏱️ Duración: ~{duration_seconds}s

[HOOK - 0:00-0:03]
{script_sections['hook']}

[CONTEXTO - 0:03-0:13]
{script_sections['context']}

[DESARROLLO - 0:13-0:53]
{script_sections['main_content']}

[CTA - 0:53-1:00]
{script_sections['cta']}

---
📝 NOTAS DE PRODUCCIÓN:
- B-Roll: Gráficos animados sobre {topic}
- Texto en pantalla: Puntos clave destacados
- Música: Upbeat tech/energética
- Transiciones: Rápidas (0.5s)
"""

        # Hashtags optimizados
        hashtags = self._generate_hashtags(topic, platform="tiktok", language=language)

        return ContentOutput(
            platform="tiktok",
            content_type="script",
            main_content=full_script,
            hook=hook,
            cta=script_sections['cta'],
            hashtags=hashtags,
            estimated_engagement_score=self._estimate_engagement(full_script, "tiktok"),
            metadata={
                "duration_seconds": duration_seconds,
                "word_count": len(full_script.split()),
                "tone": tone,
                "language": language
            }
        )

    def create_linkedin_post(
        self,
        topic: str,
        post_type: str = "thought-leadership",
        language: str = "es"
    ) -> ContentOutput:
        """
        Genera post optimizado para LinkedIn con alto engagement.

        Tipos:
        - thought-leadership: Opinión + insight
        - case-study: Ejemplo real + aprendizajes
        - announcement: Lanzamiento + valor
        - how-to: Tutorial + tips
        """
        # Estructura según tipo
        if post_type == "thought-leadership":
            content = self._generate_thought_leadership(topic, language)
        elif post_type == "case-study":
            content = self._generate_case_study(topic, language)
        else:
            content = self._generate_generic_linkedin(topic, language)

        # Optimizar para algoritmo de LinkedIn
        optimized_content = self._optimize_for_linkedin_algorithm(content)

        # Hashtags estratégicos
        hashtags = self._generate_hashtags(topic, platform="linkedin", language=language)

        return ContentOutput(
            platform="linkedin",
            content_type=post_type,
            main_content=optimized_content,
            hashtags=hashtags,
            estimated_engagement_score=self._estimate_engagement(optimized_content, "linkedin"),
            seo_keywords=self._extract_keywords(topic),
            metadata={
                "post_type": post_type,
                "char_count": len(optimized_content),
                "reading_time_seconds": len(optimized_content.split()) * 0.5,
                "language": language
            }
        )

    def create_twitter_thread(
        self,
        topic: str,
        num_tweets: int = 6,
        language: str = "es"
    ) -> ContentOutput:
        """
        Genera thread de Twitter/X optimizado.

        Estructura:
        1. Tweet gancho (viral)
        2-N. Desarrollo (un punto por tweet)
        N+1. Conclusión + CTA
        """
        tweets = []

        # Tweet 1: Hook
        hook_tweet = self._generate_twitter_hook(topic, language)
        tweets.append(f"1/ {hook_tweet}")

        # Tweets 2-N: Desarrollo
        main_points = self._generate_twitter_points(topic, num_tweets - 2, language)
        for i, point in enumerate(main_points, start=2):
            tweets.append(f"{i}/ {point}")

        # Último tweet: Cierre
        final_tweet = self._generate_twitter_finale(topic, language)
        tweets.append(f"{num_tweets}/ {final_tweet}")

        # Ensamblar thread
        full_thread = "\n\n".join(tweets)

        # Hashtags (solo en primer y último tweet)
        hashtags = self._generate_hashtags(topic, platform="twitter", language=language)

        return ContentOutput(
            platform="twitter",
            content_type="thread",
            main_content=full_thread,
            hook=hook_tweet,
            hashtags=hashtags,
            estimated_engagement_score=self._estimate_engagement(full_thread, "twitter"),
            metadata={
                "num_tweets": num_tweets,
                "avg_chars_per_tweet": sum(len(t) for t in tweets) / len(tweets),
                "language": language
            }
        )

    def create_youtube_script(
        self,
        topic: str,
        video_type: str = "tutorial",
        duration_minutes: int = 10,
        language: str = "es"
    ) -> ContentOutput:
        """
        Genera guión completo para video de YouTube.

        Incluye:
        - Intro/Hook
        - Chapters/Timestamps
        - Main content
        - B-Roll suggestions
        - Outro/CTA
        """
        script_parts = {
            "intro": self._generate_youtube_intro(topic, language),
            "chapters": self._generate_youtube_chapters(topic, duration_minutes),
            "main_script": self._generate_youtube_main_script(topic, video_type, language),
            "outro": self._generate_youtube_outro(topic, language)
        }

        # Ensamblar guión completo
        full_script = f"""📹 GUIÓN YOUTUBE - {topic.upper()}
🎯 Tipo: {video_type}
⏱️ Duración estimada: {duration_minutes} minutos
🌐 Idioma: {language.upper()}

═══════════════════════════════════════════════════

[INTRO - 0:00-0:30]
{script_parts['intro']}

═══════════════════════════════════════════════════

[CONTENIDO PRINCIPAL]

{script_parts['main_script']}

═══════════════════════════════════════════════════

[OUTRO - {duration_minutes-1}:30-{duration_minutes}:00]
{script_parts['outro']}

═══════════════════════════════════════════════════

📌 TIMESTAMPS (para descripción):
{script_parts['chapters']}

═══════════════════════════════════════════════════

🎬 NOTAS DE PRODUCCIÓN:
- Grabación: Cámara principal + captura de pantalla
- Iluminación: 3-point lighting setup
- Audio: Micrófono lavalier
- Edición: Jump cuts cada 3-5 segundos
- Gráficos: Lower thirds para stats
- Música: Background suave (royalty-free)
"""

        # Keywords para SEO de YouTube
        keywords = self._extract_keywords(topic)
        keywords.extend(["tutorial", "explicado", "2026", "español"])

        return ContentOutput(
            platform="youtube",
            content_type=video_type,
            main_content=full_script,
            hook=script_parts['intro'],
            cta=script_parts['outro'],
            seo_keywords=keywords,
            estimated_engagement_score=self._estimate_engagement(full_script, "youtube"),
            metadata={
                "duration_minutes": duration_minutes,
                "word_count": len(full_script.split()),
                "video_type": video_type,
                "chapters": script_parts['chapters'],
                "language": language
            }
        )

    def create_branded_content(
        self,
        topic: str,
        brand_name: str,
        brand_guidelines: Dict[str, Any],
        platform: str = "linkedin"
    ) -> ContentOutput:
        """
        Crea contenido siguiendo brand guidelines específicas.

        Brand Guidelines esperadas:
        {
            "tone_of_voice": ["professional", "innovative", "approachable"],
            "key_messages": ["...", "..."],
            "visual_identity": {...},
            "forbidden_words": ["..."],
            "preferred_formats": ["..."]
        }
        """
        # Aplicar tone of voice
        tone = brand_guidelines.get("tone_of_voice", ["professional"])[0]

        # Generar contenido base
        if platform == "linkedin":
            base_content = self.create_linkedin_post(topic, tone, "es")
        elif platform == "twitter":
            base_content = self.create_twitter_thread(topic, 5, "es")
        else:
            raise ValueError(f"Platform {platform} not supported for branded content")

        # Adaptar a brand voice
        branded_content = self._apply_brand_voice(
            base_content.main_content,
            brand_guidelines
        )

        # Agregar disclaimer de marca
        branded_content += f"\n\n---\n📢 Contenido creado siguiendo las guidelines de {brand_name}"

        return ContentOutput(
            platform=platform,
            content_type="branded",
            main_content=branded_content,
            hashtags=base_content.hashtags,
            metadata={
                "brand": brand_name,
                "guidelines_applied": True,
                "tone": tone
            }
        )

    # ========================================================================
    # MÉTODOS AUXILIARES DE GENERACIÓN
    # ========================================================================

    def _generate_tiktok_hook(self, topic: str, language: str) -> str:
        """Genera hook viral para TikTok (primeros 3 segundos)"""
        hooks_templates = [
            f"¿Sabías que {topic} cambió todo en 2026?",
            f"Todos hablan de {topic}, pero nadie te dice esto...",
            f"3 cosas sobre {topic} que no te enseñan en la universidad",
            f"Si usas {topic} y no sabes esto, estás perdiendo dinero"
        ]
        # En producción, usar LLM para generar hook personalizado
        return hooks_templates[0]

    def _generate_context(self, topic: str, platform: str, language: str) -> str:
        """Genera contexto/problema"""
        return f"El problema con {topic} es que la mayoría no entiende su verdadero potencial. Déjame explicarte..."

    def _generate_main_content(self, topic: str, platform: str, tone: str, language: str) -> str:
        """Genera contenido principal según plataforma y tono"""
        if platform == "tiktok":
            return f"""Punto 1: {topic} no es solo una tendencia
→ Es una revolución en cómo trabajamos

Punto 2: Las empresas que lo adoptan ahora
→ Tienen 3x más ventaja competitiva

Punto 3: Tú puedes empezar hoy
→ Sin necesidad de ser experto técnico"""

        return f"Contenido sobre {topic}..."

    def _generate_cta(self, platform: str, language: str) -> str:
        """Genera Call-to-Action optimizado"""
        ctas = {
            "tiktok": "👉 Guarda este video y compártelo con alguien que necesite verlo. Sígueme para más contenido de IA y tecnología.",
            "linkedin": "¿Qué opinas? Déjame tu experiencia en los comentarios 👇",
            "twitter": "Si te sirvió este thread, un RT ayuda a más personas a verlo 🚀",
            "youtube": "👍 Dale like si aprendiste algo nuevo y suscríbete para más tutoriales de tecnología cada semana"
        }
        return ctas.get(platform, "Comparte tu opinión en los comentarios")

    def _generate_hashtags(self, topic: str, platform: str, language: str) -> List[str]:
        """Genera hashtags optimizados por plataforma"""
        # Base hashtags
        base = ["IA", "Tecnología", "Innovación"]

        # Platform-specific
        if platform == "tiktok":
            return ["#" + tag for tag in base + ["TikTokTech", "AprendeEnTikTok", "IAParaTodos"]]
        elif platform == "linkedin":
            return ["#" + tag for tag in base + ["DigitalTransformation", "TechLeadership"]]
        elif platform == "twitter":
            return ["#" + tag for tag in base[:3]]  # Max 3 para Twitter

        return ["#" + tag for tag in base]

    def _estimate_engagement(self, content: str, platform: str) -> float:
        """Estima score de engagement (0-100)"""
        score = 50.0  # Base

        # Factores positivos
        if len(content) > 100:
            score += 10
        if "?" in content:
            score += 5  # Preguntas aumentan engagement
        if any(emoji in content for emoji in ["🚀", "💡", "👉", "✅"]):
            score += 10

        # Ajuste por plataforma
        if platform == "tiktok" and len(content.split()) < 300:
            score += 15
        elif platform == "linkedin" and 1200 <= len(content) <= 1500:
            score += 20

        return min(score, 100.0)

    def _extract_keywords(self, topic: str) -> List[str]:
        """Extrae keywords relevantes"""
        # Simplificado - en producción usar NLP
        words = re.findall(r'\b\w+\b', topic.lower())
        return [w for w in words if len(w) > 4][:10]

    def _generate_thought_leadership(self, topic: str, language: str) -> str:
        """Genera post de thought leadership para LinkedIn"""
        return f"""🤔 Una reflexión sobre {topic} que cambió mi perspectiva:

Hace 6 meses pensaba X.
Hoy entiendo Y.

¿La diferencia? [Insight clave]

Aquí te comparto 3 lecciones que aprendí:

1️⃣ [Primera lección con ejemplo]

2️⃣ [Segunda lección con dato]

3️⃣ [Tercera lección aplicable]

La pregunta no es "¿cuándo empezar con {topic}?"
La pregunta real es: "¿Puedes permitirte NO empezar?"

¿Tú qué opinas? 👇"""

    def _generate_case_study(self, topic: str, language: str) -> str:
        """Genera case study para LinkedIn"""
        return f"""📊 CASO DE ESTUDIO: Cómo {topic} transformó [Empresa]

🎯 Desafío inicial:
→ [Problema específico]

💡 Solución implementada:
→ Aplicamos {topic} en 3 fases

📈 Resultados en 90 días:
• +X% en métrica clave
• $Y ahorrados en costos
• Z horas recuperadas por semana

🔑 Lecciones aprendidas:
1. [Lección 1]
2. [Lección 2]
3. [Lección 3]

¿Te gustaría implementar algo similar? DM abierto para compartir el framework."""

    def _generate_generic_linkedin(self, topic: str, language: str) -> str:
        """Post genérico de LinkedIn"""
        return f"Insights sobre {topic} que todo profesional debería conocer en 2026..."

    def _optimize_for_linkedin_algorithm(self, content: str) -> str:
        """Optimiza contenido para algoritmo de LinkedIn"""
        # Agregar line breaks cada 2-3 líneas (mejor legibilidad)
        # Agregar emojis estratégicos
        # Asegurar pregunta al final
        optimized = content
        if "?" not in content:
            optimized += "\n\n¿Qué opinas sobre esto?"
        return optimized

    def _generate_twitter_hook(self, topic: str, language: str) -> str:
        """Hook para thread de Twitter"""
        return f"🧵 Todo lo que necesitas saber sobre {topic} en 2026 (thread con datos que te van a sorprender)"

    def _generate_twitter_points(self, topic: str, num_points: int, language: str) -> List[str]:
        """Genera puntos para thread"""
        return [
            f"Punto {i+1} sobre {topic}: [Insight específico con dato]"
            for i in range(num_points)
        ]

    def _generate_twitter_finale(self, topic: str, language: str) -> str:
        """Tweet final de thread"""
        return f"Si este thread sobre {topic} te sirvió, un RT ayuda a que más personas lo vean 🚀\n\nSígueme @usuario para más hilos de IA y tecnología cada semana"

    def _generate_youtube_intro(self, topic: str, language: str) -> str:
        """Intro de video YouTube"""
        return f"""[Música intro]

Hola, bienvenidos de vuelta al canal. Hoy vamos a hablar de {topic},
y te voy a mostrar exactamente cómo funciona, paso a paso, sin tecnicismos.

Si es tu primera vez aquí, este canal trata sobre IA y tecnología
explicada de forma simple. Suscríbete y activa la campanita 🔔

Vamos al tema..."""

    def _generate_youtube_chapters(self, topic: str, duration: int) -> str:
        """Genera timestamps para YouTube"""
        return f"""0:00 - Intro
0:30 - ¿Qué es {topic}?
2:00 - Cómo funciona (explicación técnica)
5:00 - Casos de uso reales
7:30 - Tutorial práctico
{duration-2}:00 - Conclusiones
{duration-1}:00 - Próximos pasos"""

    def _generate_youtube_main_script(self, topic: str, video_type: str, language: str) -> str:
        """Script principal de YouTube"""
        return f"""[SECCIÓN 1: Explicación]
Empecemos por entender qué es {topic}...
[Mostrar gráfico explicativo]

[SECCIÓN 2: Demostración]
Ahora déjame mostrarte cómo se usa en la práctica...
[Captura de pantalla]

[SECCIÓN 3: Tips avanzados]
Aquí van 3 trucos que los profesionales usan...
[B-roll de ejemplos]"""

    def _generate_youtube_outro(self, topic: str, language: str) -> str:
        """Outro de YouTube"""
        return f"""Y eso es todo por hoy sobre {topic}.

Espero que este tutorial te haya servido. Si aprendiste algo nuevo,
dale like 👍 y compártelo con alguien que lo necesite.

En el próximo video vamos a ver [tema relacionado], así que
suscríbete para no perdértelo.

Nos vemos en el siguiente. ¡Hasta luego!

[Música outro + pantallas finales]"""

    def _apply_brand_voice(self, content: str, guidelines: Dict) -> str:
        """Aplica brand voice según guidelines"""
        # Simplificado - en producción usar LLM con guidelines inyectadas
        branded = content

        # Reemplazar palabras prohibidas
        for forbidden in guidelines.get("forbidden_words", []):
            branded = branded.replace(forbidden, "[REDACTED]")

        # Agregar key messages si es relevante
        key_messages = guidelines.get("key_messages", [])
        if key_messages:
            branded += f"\n\n💡 Recuerda: {key_messages[0]}"

        return branded

# ============================================================================
# ISOLATED AGENT MODE
# ============================================================================

def run_isolated_content_creation(params: Dict[str, Any]) -> Dict[str, Any]:
    """
    Ejecuta creación de contenido en modo aislado.
    """
    creator = ContentCreator()

    platform = params.get('platform', 'tiktok')
    topic = params.get('topic', 'Inteligencia Artificial')
    tone = params.get('tone', 'educational')
    language = params.get('language', 'es')

    # Ejecutar según plataforma
    if platform == 'tiktok':
        result = creator.create_tiktok_script(
            topic,
            tone,
            language,
            params.get('duration_seconds', 60)
        )
    elif platform == 'linkedin':
        result = creator.create_linkedin_post(
            topic,
            params.get('post_type', 'thought-leadership'),
            language
        )
    elif platform == 'twitter':
        result = creator.create_twitter_thread(
            topic,
            params.get('num_tweets', 6),
            language
        )
    elif platform == 'youtube':
        result = creator.create_youtube_script(
            topic,
            params.get('video_type', 'tutorial'),
            params.get('duration_minutes', 10),
            language
        )
    elif platform == 'branded':
        result = creator.create_branded_content(
            topic,
            params.get('brand_name', 'TechCorp'),
            params.get('brand_guidelines', {}),
            params.get('target_platform', 'linkedin')
        )
    else:
        raise ValueError(f"Unknown platform: {platform}")

    return asdict(result)

def main():
    """Entry point for isolated execution"""
    if len(sys.argv) != 3:
        print("Usage: content_creation_skills.py <input.json> <output.json>", file=sys.stderr)
        sys.exit(1)

    input_file = Path(sys.argv[1])
    output_file = Path(sys.argv[2])

    try:
        with open(input_file, 'r') as f:
            params = json.load(f)

        result = run_isolated_content_creation(params)

        with open(output_file, 'w') as f:
            json.dump({
                "status": "success",
                "result": result,
                "metadata": {
                    "agent": "content_creator",
                    "version": "1.0",
                    "supported_platforms": ["tiktok", "linkedin", "twitter", "youtube", "branded"]
                }
            }, f, indent=2)

    except Exception as e:
        with open(output_file, 'w') as f:
            json.dump({
                "status": "error",
                "result": None,
                "metadata": {
                    "error": str(e),
                    "agent": "content_creator"
                }
            }, f, indent=2)
        sys.exit(1)

if __name__ == "__main__":
    main()
