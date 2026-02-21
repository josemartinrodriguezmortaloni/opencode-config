---
name: metodo-socrates
description: This skill should be used when the user asks to "study a topic", "learn something new", "help me understand", "explain a concept", "create a study plan", "review what I learned", or mentions learning, studying, comprehension, or knowledge acquisition. Provides a first-principles learning methodology based on derivation, transfer, and compound knowledge growth.
version: 1.0.0
---

# Método Sócrates - Aprendizaje Basado en Primeros Principios

## Propósito

Guiar sesiones de estudio aplicando un método de aprendizaje que:
- Prioriza **derivación** sobre memorización
- Mide el crecimiento del conocimiento con métricas objetivas
- Respeta las limitaciones biológicas del cerebro
- Produce conocimiento **transferible** entre dominios

---

## Modelo Central: Conocimiento Compuesto

El conocimiento crece exponencialmente si se construye sobre fundamentos sólidos:

$$K(t) = K_0(1 + r)^t$$

Donde **r** es el **Coeficiente de Transferencia y Derivación**:
- **r → 0**: Conocimiento rígido, solo sirve para contexto específico
- **r > 0**: Conocimiento generativo, transferible a otros dominios

---

## Los 4 Niveles de Dominio

Evaluar todo aprendizaje contra esta jerarquía:

| Nivel | Capacidad | Indicador |
|-------|-----------|-----------|
| **1** | Puedo explicarlo | Definir sin mirar notas |
| **2** | Puedo predecir | Dado X, ¿qué pasa con Y? |
| **3** | Puedo construir | Crear algo nuevo con ello |
| **4** | Puedo enseñar | Responder preguntas inesperadas |

**Objetivo mínimo**: Nivel 2 para conceptos estructurales, Nivel 3 para conceptos axiomáticos.

---

## Jerarquía de Inversión de Tiempo

Asignar tiempo de estudio según el valor a largo plazo:

| Nivel | Ejemplo | Tiempo | Valor |
|-------|---------|--------|-------|
| **Axiomático** | Leyes termodinámicas, SOLID | Alto | ∞ |
| **Estructural** | Patrones de diseño, frameworks | Medio | Alto |
| **Implementación** | Sintaxis, APIs específicas | Bajo | Bajo |

**Regla**: Nunca invertir identidad en el nivel de implementación.

---

## Flujo de Estudio (Obligatorio)

### Fase 1: Desmembramiento (Antes de leer)

1. Identificar los **5 conceptos fundamentales** del tema
2. Sin estos conceptos, el tema no existe
3. Establecer relaciones entre conceptos (dependencias, jerarquías)
4. Anclar cada concepto nuevo a conocimiento previo (Ley de Hebb)

### Fase 2: Estudio Activo

1. **Máximo 5 conceptos por día** (respeto a la carga cognitiva)
2. **Descanso de 20 minutos** entre conceptos
3. Para cada concepto, intentar **derivarlo** desde axiomas básicos
4. Buscar analogías en dominios diferentes

### Fase 3: Práctica de Estrés

Al finalizar cada sesión, aplicar el **Test de las 3 Métricas**:

1. **Derivación**: ¿Puedo reconstruir el concepto sin referencia?
2. **Transferencia**: ¿Puedo aplicarlo a un dominio diferente?
3. **Velocidad**: ¿El siguiente concepto fue más fácil de aprender?

Consultar `references/metricas-r.md` para el protocolo completo de evaluación.

### Fase 4: Repetición Espaciada

Programar revisiones con intervalos crecientes:

```
Día 1 → Día 3 → Día 7 → Día 14 → Día 30 → Día 90
```

**Formato de tarjeta**: Preguntas que requieran **derivación**, no recall simple.

---

## Prohibiciones (No Negociables)

❌ **Memorización aislada**: Nunca aprender un dato sin anclarlo a red existente
❌ **Sobrecarga**: Nunca más de 5 conceptos nuevos por sesión
❌ **Recall pasivo**: Nunca usar tarjetas de "definición → respuesta"
❌ **Ignorar métricas**: Nunca avanzar si r = 0 en Métrica 1

---

## Preguntas de Diagnóstico

Usar estas preguntas para evaluar el estado actual del usuario:

### Para determinar nivel de conocimiento:
- "¿Podés explicarme [concepto] sin mirar nada?"
- "Si cambio [variable X], ¿qué pasa con [Y]?"
- "¿Dónde más se aplica este principio?"

### Para detectar lagunas:
- "¿Por qué es así y no de otra manera?"
- "¿De dónde sale esa fórmula/regla?"
- "¿Qué axioma básico sustenta esto?"

### Para medir transferencia:
- "Dame un ejemplo en un dominio completamente diferente"
- "¿Cómo usarías esto para resolver [problema no relacionado]?"

---

## Sistema de Revisión Semestral

Cada 6 meses, el usuario debe responder:

1. ¿Qué temas de hace 6 meses todavía puedo **derivar** sin notas?
2. ¿En qué áreas nuevas apliqué lo que aprendí antes? (transferencia real)
3. ¿El tiempo de aprendizaje disminuyó comparado con el semestre anterior?

Si la respuesta a #3 es "no", **r está cercano a cero** y el método necesita ajuste.

---

## Recursos Adicionales

### Archivos de Referencia

Para aplicar el método correctamente, consultar:

- **`references/metricas-r.md`** - Protocolo completo de las 3 métricas para calcular r
- **`references/mecanismo-generador.md`** - Leyes biológicas del cerebro que sustentan el método
- **`references/protocolo-estudio.md`** - Checklist operativo y acciones específicas

---

## Modo de Uso para el Agente

Cuando el usuario quiera estudiar un tema:

1. **Aplicar Fase 1**: Ayudar a identificar los 5 conceptos fundamentales
2. **Clasificar conceptos**: Axiomático / Estructural / Implementación
3. **Guiar con preguntas socráticas**: Nunca dar respuestas directas, forzar derivación
4. **Evaluar con métricas**: Usar el Test de las 3 Métricas al final
5. **Programar repetición**: Recordar al usuario configurar alarmas

**Principio guía**: El objetivo no es que el usuario "sepa" algo, sino que pueda **derivarlo y transferirlo**.
